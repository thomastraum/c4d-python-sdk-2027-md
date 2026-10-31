<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/functions/maxon.UpdateAssetUsage.html -->

# maxon.UpdateAssetUsage <a id="maxon-updateassetusage"></a>

## `maxon.UpdateAssetUsage(asset, incCount=True, updateDate=True)` <a id="maxon.UpdateAssetUsage"></a>

Mark the asset as used and increment the usage counter.

This function will update the `maxon.ASSETMETADATA.Uage` meta data by increasing the count and date

**Parameters:**

- **asset** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to mark.
- **incCount** (*bool*) – True to update the count.
- **updateDate** (*bool*) – True to update the usage count.
