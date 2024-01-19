# SpatialRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**devices** | [**List[SpatialRecordDevices]**](SpatialRecordDevices.md) |  | [optional] 
**name** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.spatial_record import SpatialRecord

# TODO update the JSON string below
json = "{}"
# create an instance of SpatialRecord from a JSON string
spatial_record_instance = SpatialRecord.from_json(json)
# print the JSON string representation of the object
print SpatialRecord.to_json()

# convert the object into a dict
spatial_record_dict = spatial_record_instance.to_dict()
# create an instance of SpatialRecord from a dict
spatial_record_form_dict = spatial_record.from_dict(spatial_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


