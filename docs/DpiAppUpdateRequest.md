# DpiAppUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**apps** | **List[int]** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**blocked** | **bool** |  | [optional] 
**cats** | **List[int]** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**log** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**qos_rate_max_down** | **int** |  | [optional] 
**qos_rate_max_up** | **int** |  | [optional] 
**site_id** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.dpi_app_update_request import DpiAppUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DpiAppUpdateRequest from a JSON string
dpi_app_update_request_instance = DpiAppUpdateRequest.from_json(json)
# print the JSON string representation of the object
print DpiAppUpdateRequest.to_json()

# convert the object into a dict
dpi_app_update_request_dict = dpi_app_update_request_instance.to_dict()
# create an instance of DpiAppUpdateRequest from a dict
dpi_app_update_request_form_dict = dpi_app_update_request.from_dict(dpi_app_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


