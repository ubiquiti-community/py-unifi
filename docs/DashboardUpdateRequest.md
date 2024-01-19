# DashboardUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**controller_version** | **str** |  | [optional] 
**desc** | **str** |  | [optional] 
**is_public** | **bool** |  | [optional] 
**modules** | [**List[DashboardModules]**](DashboardModules.md) |  | [optional] 
**name** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.dashboard_update_request import DashboardUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardUpdateRequest from a JSON string
dashboard_update_request_instance = DashboardUpdateRequest.from_json(json)
# print the JSON string representation of the object
print DashboardUpdateRequest.to_json()

# convert the object into a dict
dashboard_update_request_dict = dashboard_update_request_instance.to_dict()
# create an instance of DashboardUpdateRequest from a dict
dashboard_update_request_form_dict = dashboard_update_request.from_dict(dashboard_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


