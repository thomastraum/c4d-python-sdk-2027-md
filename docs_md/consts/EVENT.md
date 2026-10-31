<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/EVENT.html -->

# EVENT <a id="event"></a>

|   |   |
|---|---|
| *EVENT_NONE* | None. |
| *EVENT_FORCEREDRAW* | Force a complete redraw. |
| *EVENT_ANIMATE* | Animate document. |
| *EVENT_NOEXPRESSION* | Do not execute expressions. |
| *EVENT_GLHACK* | Private. |
| *EVENT_CAMERAEXPRESSION* | If set(and not *EVENT_NOEXPRESSION*) the event will only update camera dependent expressions (for faster speed). |
| *EVENT_ENQUEUE_REDRAW* | *New in version R17.032:* \| Do not stop the current redraw if [`DrawViews()`](../modules/c4d/index.md#c4d.DrawViews) is running at the moment. \| In that case enqueue the redraw after the current draw is done. |
