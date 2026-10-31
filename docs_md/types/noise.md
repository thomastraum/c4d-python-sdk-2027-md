<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/types/noise.html -->

The next code was used to generate the next picture of noises.

```python
import c4d

width = 300
height = 300
noisetype = c4d.NOISE_DISPL_TURB
bmp =  c4d.bitmaps.BaseBitmap()
bmp.Init(width, height, 24)

# Create and initialize the noise instance
noise = c4d.utils.noise.C4DNoise(1234)
noise.InitFbm(21, 2.1, 0.5)

rw = float(width-1)
rh = float(height-1)

# Iterate through the bitmap and set the noise value per pixel
for x in range(width):
    for y in range(height):
        r = noise.Noise(noisetype, False, c4d.Vector(x/rw, y/rh, 0) * 7.0, octaves=5)
        o = int(c4d.utils.Clamp(0, 255, 255.0*r))
        bmp[x, y] = (o, o, o)

c4d.bitmaps.ShowBitmap(bmp)
```

# Noise Types <a id="noise-types"></a>

## BoxNoise <a id="boxnoise"></a>

> **Type:** NOISE_BOX_NOISE
>
> ![../_images/c4dnoise_boxnoise.jpg](../_images/c4dnoise_boxnoise.jpg)

## Blistered Turbulence <a id="blistered-turbulence"></a>

> **Type:** NOISE_BLIST_TURB
>
> ![../_images/c4dnoise_blisteredturbulence.jpg](../_images/c4dnoise_blisteredturbulence.jpg)

## Buya <a id="buya"></a>

> **Type:** NOISE_BUYA
>
> ![../_images/c4dnoise_buya.jpg](../_images/c4dnoise_buya.jpg)

## Cell Noise <a id="cell-noise"></a>

> **Type:** NOISE_CELL_NOISE
>
> ![../_images/c4dnoise_cellnoise.jpg](../_images/c4dnoise_cellnoise.jpg)

## Cell Voronoi <a id="cell-voronoi"></a>

> **Type:** NOISE_CELL_VORONOI
>
> ![../_images/c4dnoise_cellvoronoi.jpg](../_images/c4dnoise_cellvoronoi.jpg)

## Cranal <a id="cranal"></a>

> **Type:** NOISE_CRANAL
>
> ![../_images/c4dnoise_cranal.jpg](../_images/c4dnoise_cranal.jpg)

## Dents <a id="dents"></a>

> **Type:** NOISE_DENTS
>
> ![../_images/c4dnoise_dents.jpg](../_images/c4dnoise_dents.jpg)

## Displaced Turbulence <a id="displaced-turbulence"></a>

> **Type:** NOISE_DISPL_TURB
>
> ![../_images/c4dnoise_displacedturbulence.jpg](../_images/c4dnoise_displacedturbulence.jpg)

## Electric <a id="electric"></a>

> **Type:** NOISE_ELECTRIC
>
> ![../_images/c4dnoise_electric.jpg](../_images/c4dnoise_electric.jpg)

## FBM <a id="fbm"></a>

> **Type:** NOISE_FBM
>
> ![../_images/c4dnoise_fbm.jpg](../_images/c4dnoise_fbm.jpg)

## Fire <a id="fire"></a>

> **Type:** NOISE_FIRE
>
> ![../_images/c4dnoise_fire.jpg](../_images/c4dnoise_fire.jpg)

## Gas <a id="gas"></a>

> **Type:** NOISE_GASEOUS
>
> ![../_images/c4dnoise_gaseous.jpg](../_images/c4dnoise_gaseous.jpg)

## Hama <a id="hama"></a>

> **Type:** NOISE_HAMA
>
> ![../_images/c4dnoise_hama.jpg](../_images/c4dnoise_hama.jpg)

## Luka <a id="luka"></a>

> **Type:** NOISE_LUKA
>
> ![../_images/c4dnoise_luka.jpg](../_images/c4dnoise_luka.jpg)

## Mod Noise <a id="mod-noise"></a>

> **Type:** NOISE_MOD_NOISE
>
> ![../_images/c4dnoise_modnoise.jpg](../_images/c4dnoise_modnoise.jpg)

## Naki <a id="naki"></a>

> **Type:** NOISE_NAKI
>
> ![../_images/c4dnoise_naki.jpg](../_images/c4dnoise_naki.jpg)

## Noise <a id="noise"></a>

> **Type:** NOISE_NOISE
>
> ![../_images/c4dnoise_noise.jpg](../_images/c4dnoise_noise.jpg)

## None <a id="none"></a>

> **Type:** NOISE_NONE
>
> ![../_images/c4dnoise_none.jpg](../_images/c4dnoise_none.jpg)

## Nutous <a id="nutous"></a>

> **Type:** NOISE_NUTOUS
>
> ![../_images/c4dnoise_nutous.jpg](../_images/c4dnoise_nutous.jpg)

## Ober <a id="ober"></a>

> **Type:** NOISE_OBER
>
> ![../_images/c4dnoise_ober.jpg](../_images/c4dnoise_ober.jpg)

## Pezo <a id="pezo"></a>

> **Type:** NOISE_PEZO
>
> ![../_images/c4dnoise_pezo.jpg](../_images/c4dnoise_pezo.jpg)

## Poxo <a id="poxo"></a>

> **Type:** NOISE_POXO
>
> ![../_images/c4dnoise_poxo.jpg](../_images/c4dnoise_poxo.jpg)

## Sema <a id="sema"></a>

> **Type:** NOISE_SEMA
>
> ![../_images/c4dnoise_sema.jpg](../_images/c4dnoise_sema.jpg)

## Sparse Convolution <a id="sparse-convolution"></a>

> **Type:** NOISE_SPARSE_CONV
>
> ![../_images/c4dnoise_sparseconvolution.jpg](../_images/c4dnoise_sparseconvolution.jpg)

## Stupl <a id="stupl"></a>

> **Type:** NOISE_STUPL
>
> ![../_images/c4dnoise_stupl.jpg](../_images/c4dnoise_stupl.jpg)

## Turbulence <a id="turbulence"></a>

> **Type:** NOISE_TURBULENCE
>
> ![../_images/c4dnoise_turbulence.jpg](../_images/c4dnoise_turbulence.jpg)

## VLNoise <a id="vlnoise"></a>

> **Type:** NOISE_VL_NOISE
>
> ![../_images/c4dnoise_vlnoise.jpg](../_images/c4dnoise_vlnoise.jpg)

## Voronoi 1 <a id="voronoi-1"></a>

> **Type:** NOISE_VORONOI_1
>
> ![../_images/c4dnoise_voronoi1.jpg](../_images/c4dnoise_voronoi1.jpg)

## Voronoi 2 <a id="voronoi-2"></a>

> **Type:** NOISE_VORONOI_2
>
> ![../_images/c4dnoise_voronoi2.jpg](../_images/c4dnoise_voronoi2.jpg)

## Voronoi 3 <a id="voronoi-3"></a>

> **Type:** NOISE_VORONOI_3
>
> ![../_images/c4dnoise_voronoi3.jpg](../_images/c4dnoise_voronoi3.jpg)

## Wavy Turbulence <a id="wavy-turbulence"></a>

> **Type:** NOISE_WAVY_TURB
>
> ![../_images/c4dnoise_wavyturbulence.jpg](../_images/c4dnoise_wavyturbulence.jpg)

## Zada <a id="zada"></a>

> **Type:** NOISE_ZADA
>
> ![../_images/c4dnoise_zada.jpg](../_images/c4dnoise_zada.jpg)
