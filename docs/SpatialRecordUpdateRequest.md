# SpatialRecordUpdateRequest


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
from unifi_client.models.spatial_record_update_request import SpatialRecordUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SpatialRecordUpdateRequest from a JSON string
spatial_record_update_request_instance = SpatialRecordUpdateRequest.from_json(json)
# print the JSON string representation of the object
print SpatialRecordUpdateRequest.to_json()

# convert the object into a dict
spatial_record_update_request_dict = spatial_record_update_request_instance.to_dict()
# create an instance of SpatialRecordUpdateRequest from a dict
spatial_record_update_request_form_dict = spatial_record_update_request.from_dict(spatial_record_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


