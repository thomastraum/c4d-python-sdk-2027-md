<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/motiontracker/Mt2dTrackData/index.html -->

# c4d.modules.motiontracker.Mt2dTrackData <a id="c4d-modules-motiontracker-mt2dtrackdata"></a>

## *class* `c4d.modules.motiontracker.Mt2dTrackData` <a id="c4d.modules.motiontracker.Mt2dTrackData"></a>

*New in version R18.020.*

## Overview <a id="overview"></a>

**Collection Overview**

- [`Mt2dTrackData.GetTrackCount()`](#c4d.modules.motiontracker.Mt2dTrackData.GetTrackCount): Retrieves the number of tracks.
- [`Mt2dTrackData.GetTrackIndices()`](#c4d.modules.motiontracker.Mt2dTrackData.GetTrackIndices): Retrieves the indices of all tracks.

**Track Lookup**

- [`Mt2dTrackData.GetTrackByGid()`](#c4d.modules.motiontracker.Mt2dTrackData.GetTrackByGid): Retrieves the track with the given global ID.
- [`Mt2dTrackData.GetTrackByIndex()`](#c4d.modules.motiontracker.Mt2dTrackData.GetTrackByIndex): Retrieves the track with the given *index*.
- [`Mt2dTrackData.GetTrackByName()`](#c4d.modules.motiontracker.Mt2dTrackData.GetTrackByName): Retrieves the track with the given name.

## Members <a id="members"></a>

### Collection Overview <a id="c4d.modules.motiontracker.Mt2dTrackData-method-Collection-Overview"></a>

#### `Mt2dTrackData.GetTrackCount(self)` <a id="c4d.modules.motiontracker.Mt2dTrackData.GetTrackCount"></a>

Retrieves the number of tracks.

**Return type:** int

**Returns:** The number of tracks.

#### `Mt2dTrackData.GetTrackIndices(self, userTracks=True, autoTracks=True)` <a id="c4d.modules.motiontracker.Mt2dTrackData.GetTrackIndices"></a>

Retrieves the indices of all tracks.

**Parameters:**

- **userTracks** (*bool*) – **True** to include User created tracks, otherwise **False**.
- **autoTracks** (*bool*) – **True** to include Automatic tracks, otherwise **False**.

**Return type:** [`c4d.BaseSelect`](../../../c4d/BaseSelect/index.md#c4d.BaseSelect)

**Returns:** The indices of all tracks.

### Track Lookup <a id="c4d.modules.motiontracker.Mt2dTrackData-method-Track-Lookup"></a>

#### `Mt2dTrackData.GetTrackByGid(self, trkGid)` <a id="c4d.modules.motiontracker.Mt2dTrackData.GetTrackByGid"></a>

Retrieves the track with the given global ID.

**Parameters:** **trkGid** ([*c4d.modules.motiontracker.MtTrkGid*](../MtTrkGid/index.md#c4d.modules.motiontracker.MtTrkGid)) – The track global ID.

**Return type:** [c4d.modules.motiontracker.Mt2dTrack](../Mt2dTrack/index.md#c4d.modules.motiontracker.Mt2dTrack)

**Returns:** The track.

#### `Mt2dTrackData.GetTrackByIndex(self, index)` <a id="c4d.modules.motiontracker.Mt2dTrackData.GetTrackByIndex"></a>

Retrieves the track with the given *index*.

**Parameters:** **index** (*int*) – The track index.

**Return type:** [c4d.modules.motiontracker.Mt2dTrack](../Mt2dTrack/index.md#c4d.modules.motiontracker.Mt2dTrack)

**Returns:** The track.

#### `Mt2dTrackData.GetTrackByName(self, name)` <a id="c4d.modules.motiontracker.Mt2dTrackData.GetTrackByName"></a>

Retrieves the track with the given name.

**Parameters:** **name** (*str*) – The name of the track to search for.

**Return type:** [c4d.modules.motiontracker.Mt2dTrack](../Mt2dTrack/index.md#c4d.modules.motiontracker.Mt2dTrack)

**Returns:** The track.
