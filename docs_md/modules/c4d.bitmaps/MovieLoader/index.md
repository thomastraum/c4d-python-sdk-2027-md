<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.bitmaps/MovieLoader/index.html -->

# c4d.bitmaps.MovieLoader <a id="c4d-bitmaps-movieloader"></a>

## *class* `c4d.bitmaps.MovieLoader` <a id="c4d.bitmaps.MovieLoader"></a>

The movie loader class is used for reading movie streams.

## Overview <a id="overview"></a>

**File Lifecycle**

- [`MovieLoader.Close()`](#c4d.bitmaps.MovieLoader.Close): Close the movie file.
- [`MovieLoader.Open()`](#c4d.bitmaps.MovieLoader.Open): Open a movie file.

**Frame Data**

- [`MovieLoader.GetInfo()`](#c4d.bitmaps.MovieLoader.GetInfo): Return information about the movie.
- [`MovieLoader.Read()`](#c4d.bitmaps.MovieLoader.Read): Read an image from the movie.

**Magic Methods**

- [`MovieLoader.__init__()`](#c4d.bitmaps.MovieLoader.__init__)

## Members <a id="members"></a>

### File Lifecycle <a id="c4d.bitmaps.MovieLoader-method-File-Lifecycle"></a>

#### `MovieLoader.Close(self)` <a id="c4d.bitmaps.MovieLoader.Close"></a>

Close the movie file.

#### `MovieLoader.Open(self, fn)` <a id="c4d.bitmaps.MovieLoader.Open"></a>

Open a movie file.

**Parameters:** **fn** (*Union*[*str*, [*c4d.storage.MemoryFileStruct*](../../c4d.storage/MemoryFileStruct/index.md#c4d.storage.MemoryFileStruct)]) – The file.

### Frame Data <a id="c4d.bitmaps.MovieLoader-method-Frame-Data"></a>

#### `MovieLoader.GetInfo(self)` <a id="c4d.bitmaps.MovieLoader.GetInfo"></a>

Return information about the movie.

```python
framecount, fps = ml.GetInfo()
```

**Return type:** Tuple[int, float]

**Returns:** Frame and FPS

#### `MovieLoader.Read(self, new_frame_idx)` <a id="c4d.bitmaps.MovieLoader.Read"></a>

Read an image from the movie.

```python
framecount, fps = ml.GetInfo()
for frame in range(framecount):
    result, image = ml.Read(frame)
    #when result is not IMAGERESULT_OK...
    #...image is None.
    if result != c4d.IMAGERESULT_OK:
        break

    pass
```

**Parameters:** **new_frame_idx** (*int*) – The frame number of the frame to be read.

**Return type:** Optional[Tuple[int, [c4d.bitmaps.BaseBitmap](../BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)]]

**Returns:** The [IMAGERESULT](../../../consts/IMAGERESULT.md) and the bitmap or **None**.

### Magic Methods <a id="c4d.bitmaps.MovieLoader-method-Magic-Methods"></a>

#### `MovieLoader.__init__(self)` <a id="c4d.bitmaps.MovieLoader.__init__"></a>
