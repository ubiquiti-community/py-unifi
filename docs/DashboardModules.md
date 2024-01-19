# DashboardModules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**module_id** | **str** |  | [optional] 
**restrictions** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.dashboard_modules import DashboardModules

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardModules from a JSON string
dashboard_modules_instance = DashboardModules.from_json(json)
# print the JSON string representation of the object
print DashboardModules.to_json()

# convert the object into a dict
dashboard_modules_dict = dashboard_modules_instance.to_dict()
# create an instance of DashboardModules from a dict
dashboard_modules_form_dict = dashboard_modules.from_dict(dashboard_modules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


