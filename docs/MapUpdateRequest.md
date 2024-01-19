# MapUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**lat** | **str** |  | [optional] 
**lng** | **str** |  | [optional] 
**map_type_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**offset_left** | **float** |  | [optional] 
**offset_top** | **float** |  | [optional] 
**opacity** | **float** |  | [optional] 
**selected** | **bool** |  | [optional] 
**site_id** | **str** |  | [optional] 
**tilt** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 
**upp** | **float** |  | [optional] 
**zoom** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.map_update_request import MapUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MapUpdateRequest from a JSON string
map_update_request_instance = MapUpdateRequest.from_json(json)
# print the JSON string representation of the object
print MapUpdateRequest.to_json()

# convert the object into a dict
map_update_request_dict = map_update_request_instance.to_dict()
# create an instance of MapUpdateRequest from a dict
map_update_request_form_dict = map_update_request.from_dict(map_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


