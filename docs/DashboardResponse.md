# DashboardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Dashboard]**](Dashboard.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.dashboard_response import DashboardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardResponse from a JSON string
dashboard_response_instance = DashboardResponse.from_json(json)
# print the JSON string representation of the object
print DashboardResponse.to_json()

# convert the object into a dict
dashboard_response_dict = dashboard_response_instance.to_dict()
# create an instance of DashboardResponse from a dict
dashboard_response_form_dict = dashboard_response.from_dict(dashboard_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


