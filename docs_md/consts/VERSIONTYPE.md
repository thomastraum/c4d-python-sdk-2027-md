<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/VERSIONTYPE.html -->

# VERSIONTYPE <a id="versiontype"></a>

*Changed in version R21.*

| Symbol ID | Description |
|---|---|
| VERSIONTYPE_UNKNOWN | Unknown version. |
| VERSIONTYPE_LITE | Cinema 4D Lite. Lite is feature-restricted in many ways and does not allow for loading of plugins. |
| VERSIONTYPE_BENCHMARK | Cinebench. Cinebench is restricted to a subset of libraries. |
| VERSIONTYPE_UPDATER | Online updater. The Online updater only loads a limited subset of libraries. |
| VERSIONTYPE_TEAMRENDER_CLIENT | Cinema 4D Teamrender client. |
| VERSIONTYPE_TEAMRENDER_SERVER | Cinema 4D Teamrender server. |
| VERSIONTYPE_CINEMA4D | Cinema 4D Cinema 4D. |
| VERSIONTYPE_COMMANDLINE | Command line application. Note that this is different from c4d.GeGetCinemaInfo(c4d.CINEMAINFO_FORBID_GUI). The regular app can run without UI, but is not necessarily a special command line executable. |
| VERSIONTYPE_CINEWARE | CineWare - The renderer used in AfterEffects, Vectorworks, Archicad and Allplan. Runs without UI and does not allow for plugins. |
| VERSIONTYPE_CPYTHON | Python - The python executable. Runs without UI. |
| VERSIONTYPE_CPYTHON3 | Python 3 - The python executable. Runs without UI. |
