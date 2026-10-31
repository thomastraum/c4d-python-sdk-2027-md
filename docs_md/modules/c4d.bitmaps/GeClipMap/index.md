<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.bitmaps/GeClipMap/index.html -->

# c4d.bitmaps.GeClipMap <a id="c4d-bitmaps-geclipmap"></a>

## *class* `c4d.bitmaps.GeClipMap` <a id="c4d.bitmaps.GeClipMap"></a>

This class stores and manipulates a bitmap, providing more advanced drawing tools than [`BaseBitmap`](../BaseBitmap/index.md#c4d.bitmaps.BaseBitmap).  
Just like for *bitmaps x = y = 0* is the top left corner.  
Be sure to call `GeClipMap.Init()`, `GeClipMap.InitWith()` or `GeClipMap.InitWithBitmap()` before you attempt to use a newly allocated clip map.

> **Note:**
>
> Though clip maps support other bit depths than 32, the functionality is severely limited.  
> It is recommended that the clip map class is only used for 32 bit bitmaps.  
> Please note that the default bit depth for BaseBitmap is 24. You need to manually set it to 32 if you use `Init` to initialize the clip map.

## Overview <a id="overview"></a>

- [`GeClipMap.EnumerateFonts()`](#c4d.bitmaps.GeClipMap.EnumerateFonts): Enumerates all fonts and returns them in a container.
- [`GeClipMap.GetDefaultFont()`](#c4d.bitmaps.GeClipMap.GetDefaultFont): Retrieves Cinema 4D’s default font.
- [`GeClipMap.GetFontDescription()`](#c4d.bitmaps.GeClipMap.GetFontDescription): Retrieves a font description.
- [`GeClipMap.GetFontName()`](#c4d.bitmaps.GeClipMap.GetFontName): Retrieves the font name from a font description.
- [`GeClipMap.GetFontSize()`](#c4d.bitmaps.GeClipMap.GetFontSize): Retrieves the font size for a given font.
- [`GeClipMap.SetFontSize()`](#c4d.bitmaps.GeClipMap.SetFontSize): Sets the font size for a given font.

**Bitmap Operations**

- [`GeClipMap.Blit()`](#c4d.bitmaps.GeClipMap.Blit): Blits from *s_dp* to this clip map.
- [`GeClipMap.GetBh()`](#c4d.bitmaps.GeClipMap.GetBh): Retrieves the pixel height of the clip map.
- [`GeClipMap.GetBitmap()`](#c4d.bitmaps.GeClipMap.GetBitmap): Returns the internal bitmap object.
- [`GeClipMap.GetBw()`](#c4d.bitmaps.GeClipMap.GetBw): Retrieves the pixel width of the clip map.
- [`GeClipMap.GetDim()`](#c4d.bitmaps.GeClipMap.GetDim): Retrieves the pixel dimensions of the clip map.

**Clipping Checks**

- [`GeClipMap.ClipArea()`](#c4d.bitmaps.GeClipMap.ClipArea): Checks if a rectangle is inside the clip region.
- [`GeClipMap.ClipPoint()`](#c4d.bitmaps.GeClipMap.ClipPoint): Checks if a point is inside the clip region.

**Color And Pixels**

- [`GeClipMap.GetPixelRGBA()`](#c4d.bitmaps.GeClipMap.GetPixelRGBA): Retrieves the color of the pixel at (x,y).
- [`GeClipMap.SetColor()`](#c4d.bitmaps.GeClipMap.SetColor): Sets the draw color.
- [`GeClipMap.SetPixel()`](#c4d.bitmaps.GeClipMap.SetPixel): Sets the pixel at (*x,y*) to the draw color.
- [`GeClipMap.SetPixelRGBA()`](#c4d.bitmaps.GeClipMap.SetPixelRGBA): Sets the pixel at (*x,y*) to the specified color.

**Drawing Configuration**

- [`GeClipMap.SetDrawMode()`](#c4d.bitmaps.GeClipMap.SetDrawMode): Sets the draw mode for the following drawing operations.
- [`GeClipMap.SetOffset()`](#c4d.bitmaps.GeClipMap.SetOffset): Offsets all the following draw commands by this amount.

**Drawing Sessions**

- [`GeClipMap.BeginDraw()`](#c4d.bitmaps.GeClipMap.BeginDraw): Must be called before any drawing commands.
- [`GeClipMap.EndDraw()`](#c4d.bitmaps.GeClipMap.EndDraw): Must be called after any drawing commands.

**Font Management**

- [`GeClipMap.GetFont()`](#c4d.bitmaps.GeClipMap.GetFont): Returns the current font description.
- [`GeClipMap.SetFont()`](#c4d.bitmaps.GeClipMap.SetFont): Sets the current font.

**Initialization And Cleanup**

- [`GeClipMap.Destroy()`](#c4d.bitmaps.GeClipMap.Destroy): Resets the clip map to its initial state and frees allocated memory.
- [`GeClipMap.Init()`](#c4d.bitmaps.GeClipMap.Init): Initializes the clip map bitmap to the given dimensions and depth.
- [`GeClipMap.InitWith()`](#c4d.bitmaps.GeClipMap.InitWith): Loads the clip map bitmap from the file specified by *name*.
- [`GeClipMap.InitWithBitmap()`](#c4d.bitmaps.GeClipMap.InitWithBitmap): Loads the clip map bitmap from *bm*.

**Magic Methods**

- [`GeClipMap.__init__()`](#c4d.bitmaps.GeClipMap.__init__): Creates a new instance of [`GeClipMap`](#c4d.bitmaps.GeClipMap).

**Shape Drawing**

- [`GeClipMap.Arc()`](#c4d.bitmaps.GeClipMap.Arc): Fills a rectangle from (*x1,y1*) to (*x2,y2*) with the draw color.
- [`GeClipMap.Ellipse()`](#c4d.bitmaps.GeClipMap.Ellipse): Draws an ellipse within the rectangle from (*x1,y1*) to (*x2,y2*) with the draw color.
- [`GeClipMap.FillArc()`](#c4d.bitmaps.GeClipMap.FillArc): Draws an arc within the rectangle from (*x1,y1*) to (*x2,y2*) with the draw color.
- [`GeClipMap.FillEllipse()`](#c4d.bitmaps.GeClipMap.FillEllipse): Fills an ellipse within the rectangle from (*x1,y1*) to (*x2,y2*) with the draw color.
- [`GeClipMap.FillPolygon()`](#c4d.bitmaps.GeClipMap.FillPolygon): Fills the polygon line specified by the *p* with the draw color.
- [`GeClipMap.FillRect()`](#c4d.bitmaps.GeClipMap.FillRect): Fills a rectangle from (*x1,y1*) to (*x2,y2*) with the draw color.
- [`GeClipMap.Line()`](#c4d.bitmaps.GeClipMap.Line): Draws a line from (*x1,y1*) to (*x2,y2*) with the draw color.
- [`GeClipMap.PolyLine()`](#c4d.bitmaps.GeClipMap.PolyLine): Draws the polygon line specified by the *p* with the draw color.
- [`GeClipMap.Rect()`](#c4d.bitmaps.GeClipMap.Rect): Draws the outline of a rectangle from (*x1,y1*) to (*x2,y2*) with the draw color.

**Text Rendering**

- [`GeClipMap.TextAscent()`](#c4d.bitmaps.GeClipMap.TextAscent): Calculates the ascent in the current font.
- [`GeClipMap.TextAt()`](#c4d.bitmaps.GeClipMap.TextAt): Prints the string txt with the top left corner at (*x,y*) in the current draw color.
- [`GeClipMap.TextHeight()`](#c4d.bitmaps.GeClipMap.TextHeight): Calculates the maximum height of a string in the current font.
- [`GeClipMap.TextWidth()`](#c4d.bitmaps.GeClipMap.TextWidth): Calculates the width of the string *txt* in the current font.

## Members <a id="members"></a>

### Font Management <a id="c4d.bitmaps.GeClipMap-staticmethod-Font-Management"></a>

#### *static* `GeClipMap.EnumerateFonts(sort_mode)` <a id="c4d.bitmaps.GeClipMap.EnumerateFonts"></a>

Enumerates all fonts and returns them in a container.  
For each font a container (font description) will be inserted. They can be used for [`SetFont()`](#c4d.bitmaps.GeClipMap.SetFont) and [`GetFontName()`](#c4d.bitmaps.GeClipMap.GetFontName).

*New in version R17.032.*

**Parameters:**

**sort_mode** (*str*) –

The sort mode:

|   |   |
|---|---|
| *GE_CM_FONTSORT_FLAT* | One [`BaseContainer`](../../c4d/BaseContainer/index.md#c4d.BaseContainer) per font, no order guaranteed. |
| *GE_CM_FONTSORT_HIERARCHICAL* | For each font family a [`BaseContainer`](../../c4d/BaseContainer/index.md#c4d.BaseContainer) is stored and will hold a description for each font of the family (one container per font). The font families are sorted alphabetically. |

**Return type:** [c4d.BaseContainer](../../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:** The font list.

#### *static* `GeClipMap.GetDefaultFont(type)` <a id="c4d.bitmaps.GeClipMap.GetDefaultFont"></a>

Retrieves Cinema 4D’s default font.

*New in version R17.032.*

**Parameters:**

**type** (*int*) –

The default font type:

|   |   |
|---|---|
| *GE_FONT_DEFAULT_SYSTEM* | The *Cinema 4D* system font. |
| *GE_FONT_DEFAULT_MONOSPACED* | The *Cinema 4D* monospaced font. |

**Return type:** [c4d.BaseContainer](../../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:** The default font description.

#### *static* `GeClipMap.GetFontDescription(name, type)` <a id="c4d.bitmaps.GeClipMap.GetFontDescription"></a>

Retrieves a font description.

*New in version R17.032.*

**Parameters:**

- **name** (*str*) – The font name.

- **type** (*int*) –

  The type of font name:

  |   |   |
  |---|---|
  | *GE_FONT_NAME_DISPLAY* | Human readable font name (e.g. “Helvetica Bold”). |
  | *GE_FONT_NAME_FAMILY* | Font family name (e.g. “Helvetica”). |
  | *GE_FONT_NAME_STYLE* | Font style name (e.g. “Bold”). |
  | *GE_FONT_NAME_POSTSCRIPT* | Font postscript name (e.g. “Helvetica-Bold”). |

**Return type:** [c4d.BaseContainer](../../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:** The font description.

#### *static* `GeClipMap.GetFontName(font_description, type)` <a id="c4d.bitmaps.GeClipMap.GetFontName"></a>

Retrieves the font name from a font description.

*New in version R17.032.*

**Parameters:**

- **font_description** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The font description.

- **type** (*int*) –

  The type of font name:

  |   |   |
  |---|---|
  | *GE_FONT_NAME_DISPLAY* | Human readable font name (e.g. “Helvetica Bold”). |
  | *GE_FONT_NAME_FAMILY* | Font family name (e.g. “Helvetica”). |
  | *GE_FONT_NAME_STYLE* | Font style name (e.g. “Bold”). |
  | *GE_FONT_NAME_POSTSCRIPT* | Font postscript name (e.g. “Helvetica-Bold”). |

**Return type:** str

**Returns:** The font name.

#### *static* `GeClipMap.GetFontSize(font_description, type)` <a id="c4d.bitmaps.GeClipMap.GetFontSize"></a>

Retrieves the font size for a given font.

*New in version R17.032.*

**Parameters:**

- **font_description** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The font description.

- **type** (*int*) –

  The type of font size:

  |   |   |
  |---|---|
  | *GE_FONT_SIZE_INTERNAL* | The unit of the font size is not specified (OS or context dependent). It is not guaranteed to be pixels or points or whatever. Use it only to compare the size of two font descriptions. |

**Return type:** float

**Returns:** The font size.

#### *static* `GeClipMap.SetFontSize(font_description, type, size)` <a id="c4d.bitmaps.GeClipMap.SetFontSize"></a>

Sets the font size for a given font.

*New in version R17.032.*

**Parameters:**

- **font_description** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The font description.

- **type** (*int*) –

  The type of font size:

  |   |   |
  |---|---|
  | *GE_FONT_SIZE_INTERNAL* | The unit of the font size is not specified (OS or context dependent). It is not guaranteed to be pixels or points or whatever. Use it only to compare the size of two font descriptions. |

- **size** (*float*) – The font size to set.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Bitmap Operations <a id="c4d.bitmaps.GeClipMap-method-Bitmap-Operations"></a>

#### `GeClipMap.Blit(self, dx, dy, s_dp, sx1, sy1, sx2, sy2, rop)` <a id="c4d.bitmaps.GeClipMap.Blit"></a>

Blits from *s_dp* to this clip map. The region (*sx1*, *sy1*) to (*sx2*, *sy2*) from the source will be copied into the region with the top left corner at (*dx*, *dy*) in the destination.

Additionally you can specify a raster operation with *rop*.

**Parameters:**

- **dx** (*int*) – Top left destination X coordinate.

- **dy** (*int*) – Top left destination Y coordinate.

- **s_dp** ([*c4d.bitmaps.GeClipMap*](#c4d.bitmaps.GeClipMap)) – Source.

- **sx1** (*int*) – Top left source X coordinate.

- **sy1** (*int*) – Top left source Y coordinate.

- **sx2** (*int*) – Bottom right source X coordinate.

- **sy2** (*int*) – Bottom right source Y coordinate.

- **rop** (*int*) –

  Raster operation:

  |   |   |
  |---|---|
  | *GE_CM_BLIT_COPY* | Source overwrites destination. |
  | *GE_CM_BLIT_COL* | Source overwrites destination everywhere where source doe not equal the background color. |
  | *GE_CM_BLIT_FG* | Sets pixels to the foreground color if the color is not the background color. |

#### `GeClipMap.GetBh(self)` <a id="c4d.bitmaps.GeClipMap.GetBh"></a>

Retrieves the pixel height of the clip map.

**Return type:** int

**Returns:** The height.

#### `GeClipMap.GetBitmap(self)` <a id="c4d.bitmaps.GeClipMap.GetBitmap"></a>

Returns the internal bitmap object.

> **Warning:** The clip map alpha channel won’t be encoded in this bitmap. This is a limitation.

**Return type:** [c4d.bitmaps.BaseBitmap](../BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)

**Returns:** The bitmap.

#### `GeClipMap.GetBw(self)` <a id="c4d.bitmaps.GeClipMap.GetBw"></a>

Retrieves the pixel width of the clip map.

**Return type:** int

**Returns:** The width.

#### `GeClipMap.GetDim(self)` <a id="c4d.bitmaps.GeClipMap.GetDim"></a>

Retrieves the pixel dimensions of the clip map.

```python
w, h = clmap.GetDim()
```

**Return type:** Tuple[int, int]

**Returns:** The width and height dimensions of the clip map.

### Clipping Checks <a id="c4d.bitmaps.GeClipMap-method-Clipping-Checks"></a>

#### `GeClipMap.ClipArea(self, x1, y1, x2, y2)` <a id="c4d.bitmaps.GeClipMap.ClipArea"></a>

Checks if a rectangle is inside the clip region.

**Parameters:**

- **x1** (*int*) – Top left X coordinate.
- **y1** (*int*) – Top left Y coordinate.
- **x2** (*int*) – Bottom right X coordinate.
- **y2** (*int*) – Bottom right Y coordinate.

**Return type:** int

**Returns:** The result.

#### `GeClipMap.ClipPoint(self, x, y)` <a id="c4d.bitmaps.GeClipMap.ClipPoint"></a>

Checks if a point is inside the clip region.

**Parameters:**

- **x** (*int*) – X coordinate.
- **y** (*int*) – Y coordinate.

**Return type:** bool

**Returns:** **True** if the point is inside the region, otherwise **False**.

### Color And Pixels <a id="c4d.bitmaps.GeClipMap-method-Color-And-Pixels"></a>

#### `GeClipMap.GetPixelRGBA(self, x, y)` <a id="c4d.bitmaps.GeClipMap.GetPixelRGBA"></a>

Retrieves the color of the pixel at (x,y).

```python
r, g, b, a = clmap.GetPixelRGBA(5, 5)
```

> **Note:**
>
> Currently this method does no range check of *x* and *y*.  
> This might be added in the future.  
> Please do the check on your own.

**Parameters:**

- **x** (*int*) – X coordinate.
- **y** (*int*) – Y coordinate.

**Return type:** List[int]

**Returns:** The color of the pixel.

#### `GeClipMap.SetColor(self, r, g, b, alpha=255)` <a id="c4d.bitmaps.GeClipMap.SetColor"></a>

Sets the draw color.

**Parameters:**

- **r** (*int*) – Red. (Between 0 and 255.).
- **g** (*int*) – Green. (Between 0 and 255.)
- **b** (*int*) – Blue. (Between 0 and 255.)
- **alpha** (*int*) – Alpha value. (Between 0 and 255.)

#### `GeClipMap.SetPixel(self, x, y)` <a id="c4d.bitmaps.GeClipMap.SetPixel"></a>

Sets the pixel at (*x,y*) to the draw color.

> **Note:**
>
> Currently this method does no range check of *x* and *y*.  
> This might be added in the future.  
> Please do the check on your own.

**Parameters:**

- **x** (*int*) – X coordinate.
- **y** (*int*) – Y coordinate.

#### `GeClipMap.SetPixelRGBA(self, x, y, r, g, b, a=255)` <a id="c4d.bitmaps.GeClipMap.SetPixelRGBA"></a>

Sets the pixel at (*x,y*) to the specified color.

> **Note:**
>
> Currently this method does no range check of *x* and *y*.  
> This might be added in the future.  
> Please do the check on your own.

**Parameters:**

- **x** (*int*) – X coordinate.
- **y** (*int*) – Y coordinate.
- **r** (*int*) – Red. (Between 0 and 255.)
- **g** (*int*) – Green. (Between 0 and 255.)
- **b** (*int*) – Blue. (Between 0 and 255.)
- **a** (*int*) – Alpha value. (Between 0 and 255.)

### Drawing Configuration <a id="c4d.bitmaps.GeClipMap-method-Drawing-Configuration"></a>

#### `GeClipMap.SetDrawMode(self, mode, par)` <a id="c4d.bitmaps.GeClipMap.SetDrawMode"></a>

Sets the draw mode for the following drawing operations.

**Parameters:**

- **mode** (*int*) –

  Mode:

  |   |   |
  |---|---|
  | *GE_CM_DRAWMODE_COPY* | New pixels overwrite old ones. |
  | *GE_CM_DRAWMODE_BLEND* | New pixels blend with old ones, taking the alpha value of the new pixels in account as well as the blend factor specified by the parameter. The value specified by the parameter is the opacity of the source (bitmap). It ranges from *0* to *256*, where *256* equals *1.0* and means opaque. |
  | *GE_CM_DRAWMODE_MASK* | New pixels overwrite the old ones at the bits where the mask specified by the parameter equals *1*. |

- **par** (*int*) – Parameter (Depends on *mode*)

#### `GeClipMap.SetOffset(self, off_x, off_y)` <a id="c4d.bitmaps.GeClipMap.SetOffset"></a>

Offsets all the following draw commands by this amount.

> **Note:** The clip region is not offset.

**Parameters:**

- **off_x** (*int*) – X distance in pixels.
- **off_y** (*int*) – Y distance in pixels.

### Drawing Sessions <a id="c4d.bitmaps.GeClipMap-method-Drawing-Sessions"></a>

#### `GeClipMap.BeginDraw(self)` <a id="c4d.bitmaps.GeClipMap.BeginDraw"></a>

Must be called before any drawing commands.

> **Note:** After you call a sequence of drawing commands you should call `GeClipMap.EndDraw()`.

#### `GeClipMap.EndDraw(self)` <a id="c4d.bitmaps.GeClipMap.EndDraw"></a>

Must be called after any drawing commands.

> **Note:** Before you call a sequence of drawing commands you should call `GeClipMap.BeginDraw()`.

### Font Management <a id="c4d.bitmaps.GeClipMap-method-Font-Management"></a>

#### `GeClipMap.GetFont(self, font_description)` <a id="c4d.bitmaps.GeClipMap.GetFont"></a>

Returns the current font description.

**Parameters:** **font_description** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – Assigned the current font description.

**Return type:** float

**Returns:** The font size.

#### `GeClipMap.SetFont(self, font_description, font_size)` <a id="c4d.bitmaps.GeClipMap.SetFont"></a>

Sets the current font.

**Parameters:**

- **font_description** (*Optional*[[*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)]) – The font description. Can be **None** for the default font.
- **font_size** (*float*) – Font size, or 0.0 for the default height.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Initialization And Cleanup <a id="c4d.bitmaps.GeClipMap-method-Initialization-And-Cleanup"></a>

#### `GeClipMap.Destroy(self)` <a id="c4d.bitmaps.GeClipMap.Destroy"></a>

Resets the clip map to its initial state and frees allocated memory.

> **Warning:** Requires a new call to [`Init()`](#c4d.bitmaps.GeClipMap.Init) before the clip map can be used again.

#### `GeClipMap.Init(self, w, h, bits=32)` <a id="c4d.bitmaps.GeClipMap.Init"></a>

Initializes the clip map bitmap to the given dimensions and depth. Any previous data is lost.

**Parameters:**

- **w** (*int*) – Width
- **h** (*int*) – height
- **bits** (*int*) – 32

**Return type:** bool

**Returns:** **True** if the initialization was successful.

#### `GeClipMap.InitWith(self, name, frame)` <a id="c4d.bitmaps.GeClipMap.InitWith"></a>

Loads the clip map bitmap from the file specified by *name*.

> **Note:**
>
> The file can be either a movie or a picture.  
> The file format is automatically detected.  
> Any previous data is lost.
>
> ```python
> result, isMovie = clmap.InitWith(path)
> if result == c4d.IMAGERESULT_OK: #int check
>     # picture loaded
>     if isMovie: #bool check
>         pass # file is a movie
>     else:
>         pass # file is no movie
> ```

**Parameters:**

- **name** (*Union*[*str*, [*c4d.storage.MemoryFileStruct*](../../c4d.storage/MemoryFileStruct/index.md#c4d.storage.MemoryFileStruct)]) – The path to the image.
- **frame** (*int*) – The frame number to load in a movie.

**Return type:** Tuple[int, bool]

**Returns:** The image result and a boolean value if the file is a movie.

#### `GeClipMap.InitWithBitmap(self, bm, alpha_channel=None)` <a id="c4d.bitmaps.GeClipMap.InitWithBitmap"></a>

Loads the clip map bitmap from *bm*.  
Any previous data is lost.

**Parameters:**

- **bm** ([*c4d.bitmaps.BaseBitmap*](../BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) – The bitmap to initialize the clip map with.
- **alpha_channel** (*Optional*[[*c4d.bitmaps.BaseBitmap*](../BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)]) – The alpha channel to use in *bm*.

**Return type:** bool

**Returns:** **True** if the clip map was initialized, otherwise **False**.

### Magic Methods <a id="c4d.bitmaps.GeClipMap-method-Magic-Methods"></a>

#### `GeClipMap.__init__(self)` <a id="c4d.bitmaps.GeClipMap.__init__"></a>

Creates a new instance of [`GeClipMap`](#c4d.bitmaps.GeClipMap).

### Shape Drawing <a id="c4d.bitmaps.GeClipMap-method-Shape-Drawing"></a>

#### `GeClipMap.Arc(self, x1, y1, x2, y2, seg)` <a id="c4d.bitmaps.GeClipMap.Arc"></a>

Fills a rectangle from (*x1,y1*) to (*x2,y2*) with the draw color.

**Parameters:**

- **x1** (*int*) – Top left X coordinate.

- **y1** (*int*) – Top left Y coordinate.

- **x2** (*int*) – Bottom right X coordinate.

- **y2** (*int*) – Bottom right Y coordinate.

- **seg** –

  The arc is drawn in the direction given by:

  |   |   |
  |---|---|
  | 0 | (*x1,y1*) -> (*x2,y1*) -> (*x2,y2*) |
  | 1 | (*x2,y1*) -> (*x2,y2*) -> (*x1,y2*) |
  | 2 | (*x2,y2*) -> (*x1,y2*) -> (*x1,y1*) |
  | 3 | (*x1,y2*) -> (*x1,y1*) -> (*x2,y1*) |

#### `GeClipMap.Ellipse(self, x1, y1, x2, y2)` <a id="c4d.bitmaps.GeClipMap.Ellipse"></a>

Draws an ellipse within the rectangle from (*x1,y1*) to (*x2,y2*) with the draw color.

**Parameters:**

- **x1** (*int*) – Top left X coordinate.
- **y1** (*int*) – Top left Y coordinate.
- **x2** (*int*) – Bottom right X coordinate.
- **y2** (*int*) – Bottom right Y coordinate.

#### `GeClipMap.FillArc(self, x1, y1, x2, y2, seg)` <a id="c4d.bitmaps.GeClipMap.FillArc"></a>

Draws an arc within the rectangle from (*x1,y1*) to (*x2,y2*) with the draw color.

**Parameters:**

- **x1** (*int*) – Top left X coordinate.

- **y1** (*int*) – Top left Y coordinate.

- **x2** (*int*) – Bottom right X coordinate.

- **y2** (*int*) – Bottom right Y coordinate.

- **seg** –

  The arc is drawn in the direction given by:

  |   |   |
  |---|---|
  | 0 | (*x1,y1*) -> (*x2,y1*) -> (*x2,y2*) |
  | 1 | (*x2,y1*) -> (*x2,y2*) -> (*x1,y2*) |
  | 2 | (*x2,y2*) -> (*x1,y2*) -> (*x1,y1*) |
  | 3 | (*x1,y2*) -> (*x1,y1*) -> (*x2,y1*) |

#### `GeClipMap.FillEllipse(self, x1, y1, x2, y2)` <a id="c4d.bitmaps.GeClipMap.FillEllipse"></a>

Fills an ellipse within the rectangle from (*x1,y1*) to (*x2,y2*) with the draw color.

**Parameters:**

- **x1** (*int*) – Top left X coordinate.
- **y1** (*int*) – Top left Y coordinate.
- **x2** (*int*) – Bottom right X coordinate.
- **y2** (*int*) – Bottom right Y coordinate.

#### `GeClipMap.FillPolygon(self, p)` <a id="c4d.bitmaps.GeClipMap.FillPolygon"></a>

Fills the polygon line specified by the *p* with the draw color.

*New in version 24.*

> **Warning:** This function must be enclosed between `GeClipMap.BeginDraw()` and `GeClipMap.EndDraw()`.

**Parameters:** **p** (*Tuple*[*int*, *int*]) – The points in the polygon, a list of list made of 2 int representing the X and Y coordinate.

#### `GeClipMap.FillRect(self, x1, y1, x2, y2)` <a id="c4d.bitmaps.GeClipMap.FillRect"></a>

Fills a rectangle from (*x1,y1*) to (*x2,y2*) with the draw color.

**Parameters:**

- **x1** (*int*) – Top left X coordinate.
- **y1** (*int*) – Top left Y coordinate.
- **x2** (*int*) – Bottom right X coordinate.
- **y2** (*int*) – Bottom right Y coordinate.

#### `GeClipMap.Line(self, x1, y1, x2, y2)` <a id="c4d.bitmaps.GeClipMap.Line"></a>

Draws a line from (*x1,y1*) to (*x2,y2*) with the draw color.

**Parameters:**

- **x1** (*int*) – First X coordinate.
- **y1** (*int*) – First Y coordinate.
- **x2** (*int*) – Second X coordinate.
- **y2** (*int*) – Second Y coordinate.

#### `GeClipMap.PolyLine(self, p)` <a id="c4d.bitmaps.GeClipMap.PolyLine"></a>

Draws the polygon line specified by the *p* with the draw color.

*New in version 24.*

> **Warning:** This function must be enclosed between `GeClipMap.BeginDraw()` and `GeClipMap.EndDraw()`.

**Parameters:** **p** (*Tuple*[*int*, *int*]) – The points in the polygon line, a list of list made of 2 int representing the X and Y coordinate.

#### `GeClipMap.Rect(self, x1, y1, x2, y2)` <a id="c4d.bitmaps.GeClipMap.Rect"></a>

Draws the outline of a rectangle from (*x1,y1*) to (*x2,y2*) with the draw color.

**Parameters:**

- **x1** (*int*) – Top left X coordinate.
- **y1** (*int*) – Top left Y coordinate.
- **x2** (*int*) – Bottom right X coordinate.
- **y2** (*int*) – Bottom right Y coordinate.

### Text Rendering <a id="c4d.bitmaps.GeClipMap-method-Text-Rendering"></a>

#### `GeClipMap.TextAscent(self)` <a id="c4d.bitmaps.GeClipMap.TextAscent"></a>

Calculates the ascent in the current font. This is the distance from the baseline to the ascended line and usually represents the height of capital letters.

#### `GeClipMap.TextAt(self, x, y, txt)` <a id="c4d.bitmaps.GeClipMap.TextAt"></a>

Prints the string txt with the top left corner at (*x,y*) in the current draw color.

**Parameters:**

- **x** (*int*) – Top left X coordinate.
- **y** (*int*) – Top left Y coordinate.
- **txt** (*str*) – Text to print.

#### `GeClipMap.TextHeight(self)` <a id="c4d.bitmaps.GeClipMap.TextHeight"></a>

Calculates the maximum height of a string in the current font.

#### `GeClipMap.TextWidth(self, txt)` <a id="c4d.bitmaps.GeClipMap.TextWidth"></a>

Calculates the width of the string *txt* in the current font.

**Parameters:** **txt** (*str*) – The string.

**Return type:** int

**Returns:** Calculates the maximum height of a string in the current font.
