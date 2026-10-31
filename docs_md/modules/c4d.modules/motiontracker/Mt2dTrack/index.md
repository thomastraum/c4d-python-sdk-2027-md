<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/motiontracker/Mt2dTrack/index.html -->

# c4d.modules.motiontracker.Mt2dTrack <a id="c4d-modules-motiontracker-mt2dtrack"></a>

## *class* `c4d.modules.motiontracker.Mt2dTrack` <a id="c4d.modules.motiontracker.Mt2dTrack"></a>

*New in version R18.020.*

## Overview <a id="overview"></a>

**Motion Data**

- [`Mt2dTrack.GetDataForCurrentFrame()`](#c4d.modules.motiontracker.Mt2dTrack.GetDataForCurrentFrame): Retrieves the track data for the current frame.
- [`Mt2dTrack.GetDataForFrame()`](#c4d.modules.motiontracker.Mt2dTrack.GetDataForFrame): Retrieves the motion tracking data for the given frame.
- [`Mt2dTrack.GetFramesWithTrackData()`](#c4d.modules.motiontracker.Mt2dTrack.GetFramesWithTrackData): Retrieves the frames on which the track has data.

**Track Metadata**

- [`Mt2dTrack.GetId()`](#c4d.modules.motiontracker.Mt2dTrack.GetId): Retrieves the global ID of the track.
- [`Mt2dTrack.GetName()`](#c4d.modules.motiontracker.Mt2dTrack.GetName): Retrieves the name of the track.
- [`Mt2dTrack.GetStatus()`](#c4d.modules.motiontracker.Mt2dTrack.GetStatus): Retrieves the track status.

## Members <a id="members"></a>

### Motion Data <a id="c4d.modules.motiontracker.Mt2dTrack-method-Motion-Data"></a>

#### `Mt2dTrack.GetDataForCurrentFrame(self)` <a id="c4d.modules.motiontracker.Mt2dTrack.GetDataForCurrentFrame"></a>

Retrieves the track data for the current frame.

**Return type:** Optional[[c4d.modules.motiontracker.MtData](../MtData/index.md#c4d.modules.motiontracker.MtData)]

**Returns:** The tracking data for the current frame, or **None** if it does not exist.

#### `Mt2dTrack.GetDataForFrame(self, frameNum)` <a id="c4d.modules.motiontracker.Mt2dTrack.GetDataForFrame"></a>

Retrieves the motion tracking data for the given frame.

**Parameters:** **frameNum** (*int*) – The frame number.

**Return type:** Optional[[c4d.modules.motiontracker.MtData](../MtData/index.md#c4d.modules.motiontracker.MtData)]

**Returns:** The tracking data, or **None** if it does not exist for the requested frame.

#### `Mt2dTrack.GetFramesWithTrackData(self)` <a id="c4d.modules.motiontracker.Mt2dTrack.GetFramesWithTrackData"></a>

Retrieves the frames on which the track has data.

**Return type:** [`c4d.BaseSelect`](../../../c4d/BaseSelect/index.md#c4d.BaseSelect)

**Returns:** The frames with track data.

### Track Metadata <a id="c4d.modules.motiontracker.Mt2dTrack-method-Track-Metadata"></a>

#### `Mt2dTrack.GetId(self)` <a id="c4d.modules.motiontracker.Mt2dTrack.GetId"></a>

Retrieves the global ID of the track.

**Return type:** [c4d.modules.motiontracker.MtTrkGid](../MtTrkGid/index.md#c4d.modules.motiontracker.MtTrkGid)

**Returns:** The global ID of the track.

#### `Mt2dTrack.GetName(self)` <a id="c4d.modules.motiontracker.Mt2dTrack.GetName"></a>

Retrieves the name of the track.

**Return type:** str

**Returns:** The name of the track.

#### `Mt2dTrack.GetStatus(self)` <a id="c4d.modules.motiontracker.Mt2dTrack.GetStatus"></a>

Retrieves the track status.

**Return type:** int

**Returns:**

The track status:

|   |   |
|---|---|
| *INVALID_TRACK* | Not a valid track. |
| *UNTRACKED* | Has not yet been tracked. |
| *TRACKED_VALID* | Has been tracked, and is up to date. |
| *TRACKED_STALE* | Has been tracked, but needs updating. (Changes have been made, but has not yet been retracked.) |
