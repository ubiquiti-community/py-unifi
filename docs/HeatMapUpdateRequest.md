# HeatMapUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**map_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.heat_map_update_request import HeatMapUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HeatMapUpdateRequest from a JSON string
heat_map_update_request_instance = HeatMapUpdateRequest.from_json(json)
# print the JSON string representation of the object
print HeatMapUpdateRequest.to_json()

# convert the object into a dict
heat_map_update_request_dict = heat_map_update_request_instance.to_dict()
# create an instance of HeatMapUpdateRequest from a dict
heat_map_update_request_form_dict = heat_map_update_request.from_dict(heat_map_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


