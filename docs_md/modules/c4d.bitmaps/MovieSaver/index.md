<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.bitmaps/MovieSaver/index.html -->

# c4d.bitmaps.MovieSaver <a id="c4d-bitmaps-moviesaver"></a>

## *class* `c4d.bitmaps.MovieSaver` <a id="c4d.bitmaps.MovieSaver"></a>

The movie saver class is used for reading and writing movie streams.

## Overview <a id="overview"></a>

**Magic Methods**

- [`MovieSaver.__init__()`](#c4d.bitmaps.MovieSaver.__init__)

**Movie File Operations**

- [`MovieSaver.Choose()`](#c4d.bitmaps.MovieSaver.Choose): Opens the standard compression chooser for movie formats.
- [`MovieSaver.Close()`](#c4d.bitmaps.MovieSaver.Close): Close the movie file.
- [`MovieSaver.Open()`](#c4d.bitmaps.MovieSaver.Open): Opens a movie stream to the file *name*.
- [`MovieSaver.Write()`](#c4d.bitmaps.MovieSaver.Write): Adds another frame to the end of the movie stream.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.bitmaps.MovieSaver-method-Magic-Methods"></a>

#### `MovieSaver.__init__(self)` <a id="c4d.bitmaps.MovieSaver.__init__"></a>

### Movie File Operations <a id="c4d.bitmaps.MovieSaver-method-Movie-File-Operations"></a>

#### `MovieSaver.Choose(self, format, bc)` <a id="c4d.bitmaps.MovieSaver.Choose"></a>

Opens the standard compression chooser for movie formats.

> **Note:** The arguments might change in the future.

The new settings are stored in **bc** if the user clicks ok.

```python
data = c4d.BaseContainer()
action = ms.Choose(c4d.FILTER_AVI, data)

# If the user canceled the dialog
if action is False:
    return True

ms.Open(..., data, ...)
```

**Parameters:**

- **format** (*int*) – The file format. Valid values are either *FILTER_AVI* or *FILTER_MOVIE*.
- **bc** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – Used to pass the default settings, and to read the settings the user has chosen.

#### `MovieSaver.Close(self)` <a id="c4d.bitmaps.MovieSaver.Close"></a>

Close the movie file.

#### `MovieSaver.Open(self, name, bm, fps, format, data, savebits)` <a id="c4d.bitmaps.MovieSaver.Open"></a>

Opens a movie stream to the file *name*.  
The resolution and bit depth are defined by the first frame in *bm*.  
The framerate is specified by *fps*.

**Parameters:**

- **name** (*Union*[*str*, [*c4d.storage.MemoryFileStruct*](../../c4d.storage/MemoryFileStruct/index.md#c4d.storage.MemoryFileStruct)]) – A file.

- **bm** ([*c4d.bitmaps.BaseBitmap*](../BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) – A typical frame of the movie, used for dimensions.

- **fps** (*int*) – The frame rate in frames per second

- **format** (*int*) – The file format. Valid values are either *FILTER_AVI* or *FILTER_MOVIE*.

- **data** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) –

  Additional settings for the file format.

  (Please see the documentation for the AVI and Quicktime formats for more information.)

  |   |   |
  |---|---|
  | *AVISAVER_FCCTYPE* | Unknown. |
  | *AVISAVER_FCCHANDLER* | Unknown. |
  | *AVISAVER_LKEY* | Unknown. |
  | *AVISAVER_LDATARATE* | Unknown. |
  | *AVISAVER_LQ* | Unknown. |

  |   |   |
  |---|---|
  | *QTSAVER_COMPRESSOR* | Unknown. |
  | *QTSAVER_QUALITY* | Unknown. |
  | *QTSAVER_TEMPQUAL* | Unknown. |
  | *QTSAVER_FRAMERATE* | Unknown. |
  | *QTSAVER_KEYFRAMES* | Unknown. |
  | *QTSAVER_PLANES* | Unknown. |
  | *QTSAVER_DATARATE* | Unknown. |
  | *QTSAVER_FRAMEDURATION* | Unknown. |
  | *QTSAVER_MINQUALITY* | Unknown. |
  | *QTSAVER_MINTEMPQUAL* | Unknown. |
  | *QTSAVER_FIXEDFRAMERATE* | Unknown. |

- **savebits** (*int*) –

  Can be a combination of the following flags:

  | Symbol ID | Description |
  |---|---|
  | SAVEBIT_NONE | None. |
  | SAVEBIT_ALPHA | Save the alpha channel(s) in the file. (For filter plugins, do not save an alpha channel if this is not set.) |
  | SAVEBIT_MULTILAYER | Save multiple layers. |
  | SAVEBIT_USESELECTEDLAYERS | Use selected layers. |
  | SAVEBIT_USE16BITCHANNELS | Use *16*-bit channels. |
  | SAVEBIT_GREYSCALE | Save in grayscale mode. |
  | SAVEBIT_INTERNALNET | Private. |
  | SAVEBIT_DONTMERGE | Avoid merging of layers in BodyPaint 3D files. |
  | SAVEBIT_USE32BITCHANNELS | Use *32*-bit channels. |
  | SAVEBIT_SAVERENDERRESULT | Private. |
  | SAVEBIT_FIRSTALPHA_ONLY | Private. |
  | SAVEBIT_KEEP_COLOR_MODE | Private. |

#### `MovieSaver.Write(self, bm)` <a id="c4d.bitmaps.MovieSaver.Write"></a>

Adds another frame to the end of the movie stream.

**Parameters:** **bm** ([*c4d.bitmaps.BaseBitmap*](../BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) – The frame to add

**Return type:** int

**Returns:**

The result. Possible values are:

|   |   |
|---|---|
| *IMAGERESULT_OK* | Image loaded/created. |
| *IMAGERESULT_NOTEXISTING* | Image does not exist. |
| *IMAGERESULT_WRONGTYPE* | Image has the wrong type. |
| *IMAGERESULT_OUTOFMEMORY* | Not enough memory. |
| *IMAGERESULT_FILEERROR* | File error. |
| *IMAGERESULT_FILESTRUCTURE* | Invalid file structure. |
| *IMAGERESULT_MISC_ERROR* | Unknown error. |
| *IMAGERESULT_PARAM_ERROR* | Parameter error. |
| *IMAGERESULT_THREADCANCELED* | Thread canceled while working. |
