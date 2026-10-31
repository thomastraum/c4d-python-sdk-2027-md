<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/examples/plugins/py_io_ies_meta/py_io_ies_meta_loader.pyp.html -->

Local source: [examples/plugins/py_io_ies_meta/py_io_ies_meta_loader.pyp](../../../../examples/plugins/py_io_ies_meta/py_io_ies_meta_loader.pyp)

# py_io_ies_meta_loader <a id="py-io-ies-meta-loader"></a>

Demonstrates a scene loader plugin for IES Meta data.

Demonstrates how to implement a scene saver plugin that exports all IES Meta information from the current document to a txt file, iterating through all objects in the scene.

## DETAILS

The scene saver walks the document and its object caches to collect IES light data, then writes the result to a text file.

To run this example, place the file in the Cinema 4D plugins folder and restart Cinema 4D.

Topics:

- Traversing object caches to find IES lights
- Writing scene metadata with a SceneSaverData plugin

## Files <a id="files"></a>

### `py_io_ies_meta_loader.pyp` <a id="py-io-ies-meta-loader-pyp"></a>

```python
"""Demonstrates a scene loader plugin for IES Meta data.

The loader complements the IES Meta exporter and uses resource descriptions to present import options to the user.

To run this example, place the file in the Cinema 4D plugins folder and restart Cinema 4D.

Topics:
    - Identifying and loading a custom scene file
    - Presenting import options through resource descriptions
"""
__copyright__ = "Copyright 2026, MAXON Computer"
__author__ = "Manuel MAGALHAES"
__date__ = "25/08/2026"
__license__ = "Apache-2.0 license"
__version__ = "12.0.0"

import c4d

# SceneLoader are registered earlier than Cinema 4D Resource parser.
# To have all the constant defined in fies_loader.h, you need to manually parse them
import os
import mxutils

mxutils.ImportSymbols(os.path.join(os.path.dirname(__file__), "res"))

PLUGIN_ID = 1059408

class ExampleDialog(c4d.gui.GeDialog):

    def CreateLayout(self):
        """
        This Method is called automatically when Cinema 4D creates the Layout of the Dialog.
        Returns:
            bool: False if there was an error, otherwise True.
        """
        # Defines the title of the Dialog
        self.SetTitle("This is an example Dialog")

        # Creates a Ok and Cancel Button
        self.AddDlgGroup(c4d.DLG_OK | c4d.DLG_CANCEL)

        return True

    def Command(self, messageId, bc):
        """
        This Method is called automatically when the user clicks on a gadget and/or changes
        its value this function will be called. It is also called when a string menu item is selected.

        Args:
            messageId (int): The ID of the gadget that triggered the event.
            bc (c4d.BaseContainer): The original message container.

        Returns:
            bool: False if there was an error, otherwise True.
        """
        # User click on Ok buttonG
        if messageId == c4d.DLG_OK:
            print("User Click on Ok")
            return True

        # User click on Cancel button
        elif messageId == c4d.DLG_CANCEL:
            print("User Click on Cancel")

            # Close the Dialog
            self.Close()
            return True

        return True

class IESMetaLoader(c4d.plugins.SceneLoaderData):
    """IESMeta Loader"""
    dialog = None

    def Init(self, node, isCloneInit=False):
        """
        Called when a new instance of this object is created. In this context, this allow to define
        the option by default for the SceneLoaderPlugin that will be displayed to the user.

        Args:
            node (c4d.GeListNode): The instance of the SceneLoaderData.
            isCloneInit (bool): True if the scene loader data is a copy of another one.

        Returns:
            bool: False if there was an error, otherwise True.
        """
        # Define the default value for the parameters.
        self.InitAttr(node, bool, IES_IMPORT_PRINT_TO_CONSOLE)

        if not isCloneInit:
            node[IES_IMPORT_PRINT_TO_CONSOLE] = True
        return True

    def Identify(self, node, name, probe, size):
        """
        Cinema 4D calls this function for every registered scene loader plugin. This function
        should return True only if this plugin can handle the file. The parameter 'probe' contain a
        small part of the file, usually the 1024 first characters. This allow to check if the header
        of the file starts as expected, validating the fact this file can be read by the load
        function.
        Args:
            node (c4d.BaseList2D): The node object.
            name (str): The name of the loader.
            probe (memoryview): The start of a small chunk of data from the start of the file for
            testing this file type. Usually the probe size is 1024 bytes. Never call the buffer
            outside this method!
            size (int): The size of the chunk for testing this file type.
        Returns:
            bool: True if the SceneLoaderData can load this kind of files.
        """
        # Check if the last three character are equal to 'txt'
        if "txt" in name[-3:]:
            # Check if the txt file start with the correct header.
            if bytes(probe[0:17]).decode().upper() == "IES Meta Exporter".upper():
                return True
        return False

    def Load(self, node, name, doc, filterflags, error, bt):
        """
        Called by Cinema 4D to load the file. This method is only called if the identify function
        returned True. The parameter 'node' allows to retrieve the options the user defined for this
        import.

        Args:
            node (c4d.BaseList2D): The node object representing the exporter.
            name (str): The filename of the file to save.
            doc (c4d.documents.BaseDocument): The document that should be saved.
            filterflags (SCENEFILTER): Options for the exporter.
            error (None): Not supported.
            bt (c4d.threading.BaseThread): The calling thread.

        Returns:
            FILEERROR: Status of the import process.
        """
        dialogAllowed = bool(filterflags & c4d.SCENEFILTER_DIALOGSALLOWED)
        isMainThread = c4d.threading.GeIsMainThread()

        print("is main thread  {}".format(isMainThread))
        print("is dialog allowed? {}".format(dialogAllowed))
        # GUI operation are not allowed if they are not executed from the main thread, always check
        # if this is the main thread. Check also if the flag is set to SCENEFILTER_DIALOGSALLOWED to
        # sure dialog can be displayed.
        if isMainThread:
            if dialogAllowed:
                # Open a GeDialog
                if self.dialog is None:
                    self.dialog = ExampleDialog()
                self.dialog.Open(dlgtype=c4d.DLG_TYPE_ASYNC,
                                 pluginid=PLUGIN_ID,
                                 defaultw=400,
                                 defaulth=32
                                 )

                # Create and display a Popup Menu
                menu = c4d.BaseContainer()
                menu.InsData(1001, 'Item 1')
                menu.InsData(1002, 'Item 2')
                menu.InsData(0, '')  # Append separator
                c4d.gui.ShowPopupDialog(cd=None, bc=menu, x=c4d.MOUSEPOS, y=c4d.MOUSEPOS)

        # Display the content of the file if the user check the option in the import options.
        # Opens the file in read mode and print all the lines
        if node[IES_IMPORT_PRINT_TO_CONSOLE]:
            with open(name, "r") as f:
                for line in f:
                    print(line)
        return c4d.FILEERROR_NONE

if __name__ == '__main__':
    c4d.plugins.RegisterSceneLoaderPlugin(id=PLUGIN_ID,
                                          str="Py SDK - IES Meta (*.txt)",
                                          info=0,
                                          g=IESMetaLoader,
                                          description="fies_loader",
                                          )
```

[Example on GitHub](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/plugins/py_io_ies_meta/py_io_ies_meta_loader.pyp)

### `py_io_ies_meta.pyp` <a id="py-io-ies-meta-pyp"></a>

```python
"""Demonstrates how to implement a scene saver plugin that exports all IES Meta information from the current document to a txt file, iterating through all objects in the scene.

The scene saver walks the document and its object caches to collect IES light data, then writes the result to a text file.

To run this example, place the file in the Cinema 4D plugins folder and restart Cinema 4D.

Topics:
    - Traversing object caches to find IES lights
    - Writing scene metadata with a SceneSaverData plugin
"""
__copyright__ = "Copyright 2026, MAXON Computer"
__author__ = "Maxime Adam"
__date__ = "25/08/2026"
__license__ = "Apache-2.0 license"
__version__ = "12.0.0"

import c4d
import os
import datetime

# Separate c4d_strings definitions
IDS_MANUFAC = 1001
IDS_LUMCAT = 1002
IDS_LUMINAIRE = 1003

IDS_LAMPCAT = 1004
IDS_LAMP = 1005
IDS_FOUND_IES = 1006
IDS_FOUND_LIGHTS = 1007
IDS_IES_META_CREATED = 1008
IDS_IES_HEADER = 1009

# Be sure to use a unique ID obtained from developers.maxon.net
PLUGIN_ID = 1025281

class IESMeta(object):

    def __init__(self, ieslight):
        self.count = 1
        self._manufac = ieslight[c4d.LIGHT_PHOTOMETRIC_INFO_MANUFAC]
        self._lumcat = ieslight[c4d.LIGHT_PHOTOMETRIC_INFO_LUMCAT]
        self._luminaire = ieslight[c4d.LIGHT_PHOTOMETRIC_INFO_LUMINAIRE]
        self._lampcat = ieslight[c4d.LIGHT_PHOTOMETRIC_INFO_LAMPCAT]
        self._lamp = ieslight[c4d.LIGHT_PHOTOMETRIC_INFO_LAMP]

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __str__(self):
        lbl_manufac = c4d.plugins.GeLoadString(IDS_MANUFAC)
        lbl_lumcat = c4d.plugins.GeLoadString(IDS_LUMCAT)
        lbl_luminaire = c4d.plugins.GeLoadString(IDS_LUMINAIRE)
        lbl_lampcat = c4d.plugins.GeLoadString(IDS_LAMPCAT)
        lbl_lamp = c4d.plugins.GeLoadString(IDS_LAMP)

        return "%s: %s\n%s: %s\n%s: %s\n%s: %s\n%s: %s\n" % (
            lbl_manufac, self._manufac, lbl_lumcat, self._lumcat, lbl_luminaire, self._luminaire, lbl_lampcat, self._lampcat, lbl_lamp, self._lamp)

    def __repr__(self):
        """Just used if two meta information are equal, see __eq__"""
        return "%s,%s,%s,%s,%s" % (self._manufac, self._lumcat,
                                   self._luminaire, self._lampcat, self._lamp)

class IESMetaSaverHelper(object):

    @staticmethod
    def HierarchyIterator(obj):
        """A Generator to iterate over the Hierarchy.

        Args:
            obj: The starting object of the generator (will be the first result)

        Returns:
            All objects under and next of the `obj`
        """
        while obj:
            yield obj
            for opChild in IESMetaSaverHelper.HierarchyIterator(obj.GetDown()):
                yield opChild
            obj = obj.GetNext()

    @staticmethod
    def CacheIterator(op):
        """A Python Generator to iterate over all final objects (PolygonObject, CameraObject, Light....) of the passed BaseObject.

        Args:
            op: The BaseObject to retrieve all objects cached.
        """
        if not isinstance(op, c4d.BaseObject):
            raise TypeError("Expected a BaseObject or derived class got {0}".format(
                op.__class__.__name__))

        # Tries to retrieve the deformed cache of the object
        temp = op.GetDeformCache()
        if temp is not None:
            # If there is a deformed cache we iterate over him, a deformed cache can also contain deformed cache
            # e.g. in case of a nested deformer
            for obj in IESMetaSaverHelper.CacheIterator(temp):
                yield obj

        # Tries to retrieve the cache of the Object
        temp = op.GetCache()
        if temp is not None:
            # If there is a cache iterates over its, a cache can also contain deformed cache.
            # e.g. an instance, have a cache of its linked object but if this object
            # is deformed, then you have a deformed cache as well
            for obj in IESMetaSaverHelper.CacheIterator(temp):
                yield obj

        # If op is not a generator / modifier
        if not op.GetBit(c4d.BIT_CONTROLOBJECT):
            yield op

        # Then finally iterates over the child of the current object to retrieve all objects.
        # e.g. in a cloner set to Instance mode, every clone is a new object.
        temp = op.GetDown()
        while temp:
            for obj in IESMetaSaverHelper.CacheIterator(temp):
                yield obj
            temp = temp.GetNext()

class IESMetaSaver(c4d.plugins.SceneSaverData, IESMetaSaverHelper):
    """IESMeta Exporter"""

    def Save(self, node, name, doc, filterflags):
        """Called by Cinema 4D when the document is asked to be saved in this format.

        Args:
            node (c4d.BaseList2D): The node object representing the exporter.
            name (str): The filename of the file to save.
            doc (c4d.documents.BaseDocument): The document that should be saved.
            filterflags (SCENEFILTER): Options for the exporter.

        Returns:
            FILEERROR: Status of the export process.
        """
        # If there is no object in the scene, nothing to export.
        firstObj = doc.GetFirstObject()
        if firstObj is None:
            return c4d.FILEERROR_NONE

        # IESLightTotal stores the total amount of IES light found, while
        # iesMetaList only store once an IES files
        IESLightTotal = 0
        iesMetaList = []

        # Iterates each object in the Scene
        for obj in IESMetaSaverHelper.HierarchyIterator(firstObj):

            # Iterates each object present in the cache that are not generator
            # (PolygonObject, LightObject, CameraObject...)
            for cachedObj in IESMetaSaverHelper.CacheIterator(obj):

                # If the cached object is not a light, go to the next object.
                if not cachedObj.IsInstanceOf(c4d.Olight):
                    continue

                # If the light is not a photometric one or their is no ies file loaded, go
                # to the next object.
                if cachedObj[c4d.LIGHT_TYPE] != c4d.LIGHT_TYPE_PHOTOMETRIC or not cachedObj[c4d.LIGHT_PHOTOMETRIC_FILE]:
                    continue

                minfo = IESMeta(cachedObj)
                if minfo is None:
                    raise MemoryError("Failed to create a IESMeta.")

                # Increment the total IES count, we are sure to log the IES if we are here
                IESLightTotal += 1

                # If there is already a meta file for this file in our list, increment the
                # usage count
                try:
                    iesId = iesMetaList.index(minfo)
                    iesMetaList[iesId].count += 1
                except ValueError:
                    # If ValueError is thrown, that means the value was not found so we adds
                    iesMetaList.append(minfo)

        # If there is no IES files logged, there is nothing to export
        if len(iesMetaList) == 0:
            # Defines the warning method according if we are allowed to displayed Dialog box or not
            displayFn = c4d.gui.MessageDialog if filterflags & c4d.SCENEFILTER_DIALOGSALLOWED else __builtins__[
                "print"]
            displayFn("There is no IES file to export in the current document")
            return c4d.FILEERROR_NONE

        # Opens the file in write mode
        with open(name, "w") as f:
            # Retrieves Data for the Header
            title = c4d.plugins.GeLoadString(IDS_IES_HEADER)
            created = c4d.plugins.GeLoadString(IDS_IES_META_CREATED)
            now = datetime.datetime.now()
            time = now.ctime()
            docpath = doc.GetDocumentPath()
            docname = doc.GetDocumentName()

            # Write the Header
            header = "%s\n%s: %s - %s\n\n" % (title, created, time, os.path.join(docpath, docname))
            f.write(header)

            # Write total light founds
            f.write("%s\n" % (c4d.plugins.GeLoadString(
                IDS_FOUND_IES, len(iesMetaList), IESLightTotal),))
            f.write("=" * 65 + "\n\n")

            # Write each Ies Meta
            for meta in iesMetaList:
                f.write("%s\n%s\n" % (c4d.plugins.GeLoadString(
                    IDS_FOUND_LIGHTS, meta.count), str(meta),))
                f.write("-" * 65 + "\n")

        return c4d.FILEERROR_NONE

if __name__ == '__main__':
    c4d.plugins.RegisterSceneSaverPlugin(id=PLUGIN_ID,
                                         str="Py SDK - IES Meta (*.txt)",
                                         info=0,
                                         g=IESMetaSaver,
                                         description="",
                                         suffix="txt")
```

[Example on GitHub](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/plugins/py_io_ies_meta/py_io_ies_meta.pyp)

### `res/c4d_symbols.h` <a id="res-c4d-symbols-h"></a>

```cpp
enum
{
	IDS_MANUFAC = 1001,
	IDS_LUMCAT = 1002,
	IDS_LUMINAIRE = 1003,
	IDS_LAMPCAT = 1004,
	IDS_LAMP = 1005,
	
	IDS_FOUND_IES	 = 1006,
	
	IDS_FOUND_LIGHTS = 1007,
	
	IDS_IES_META_CREATED = 1008,
	IDS_IES_HEADER = 1009,
	
	// End of symbol definition
	_DUMMY_ELEMENT_
};
```

[Example on GitHub](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/plugins/py_io_ies_meta/res/c4d_symbols.h)

### `res/description/fies_loader.h` <a id="res-description-fies-loader-h"></a>

```cpp
#ifndef _FIES_LOADER_H__
#define _FIES_LOADER_H__

enum 
{
	
	fies_loader = 10000,
	IES_IMPORT_PRINT_TO_CONSOLE,
	IES_IMPORT_GROUP

};

#endif
```

[Example on GitHub](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/plugins/py_io_ies_meta/res/description/fies_loader.h)

### `res/description/fies_loader.res` <a id="res-description-fies-loader-res"></a>

```c4dres
CONTAINER fies_loader
{
	INCLUDE Fbase;
	NAME fies_loader;
	
	GROUP IES_IMPORT_GROUP
	{
		DEFAULT 1;
		
		BOOL IES_IMPORT_PRINT_TO_CONSOLE {}

	}
}
```

[Example on GitHub](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/plugins/py_io_ies_meta/res/description/fies_loader.res)

### `res/strings_us/c4d_strings.str` <a id="res-strings-us-c4d-strings-str"></a>

```c4dstr
STRINGTABLE
{
	IDS_MANUFAC						"Luminaire manufacturer";
	IDS_LUMCAT						"Luminaire catalog number";
	IDS_LUMINAIRE					"Luminaire description";
	IDS_LAMPCAT						"Lamp catalog number";
	IDS_LAMP							"Lamp description";
	
	IDS_FOUND_IES					"Found # different IES lights, in total #.";
	IDS_FOUND_LIGHTS			"Found # IES lights of:";
	
	IDS_IES_META_CREATED	"Created on";
	IDS_IES_HEADER				"IES Meta Exporter";
}
```

[Example on GitHub](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/plugins/py_io_ies_meta/res/strings_us/c4d_strings.str)

### `res/strings_us/description/fies_loader.str` <a id="res-strings-us-description-fies-loader-str"></a>

```c4dstr
STRINGTABLE fies_loader
{
	fies_loader										    "IES Import Settings";
  IES_IMPORT_GROUP                  "IES option group";
	IES_IMPORT_PRINT_TO_CONSOLE			  "Print to console?";

}
```

[Example on GitHub](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/plugins/py_io_ies_meta/res/strings_us/description/fies_loader.str)
