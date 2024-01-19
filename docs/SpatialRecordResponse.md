# SpatialRecordResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SpatialRecord]**](SpatialRecord.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from unifi_client.models.spatial_record_response import SpatialRecordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SpatialRecordResponse from a JSON string
spatial_record_response_instance = SpatialRecordResponse.from_json(json)
# print the JSON string representation of the object
print SpatialRecordResponse.to_json()

# convert the object into a dict
spatial_record_response_dict = spatial_record_response_instance.to_dict()
# create an instance of SpatialRecordResponse from a dict
spatial_record_response_form_dict = spatial_record_response.from_dict(spatial_record_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


