# DpiAppResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DpiApp]**](DpiApp.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from unifi_client.models.dpi_app_response import DpiAppResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DpiAppResponse from a JSON string
dpi_app_response_instance = DpiAppResponse.from_json(json)
# print the JSON string representation of the object
print DpiAppResponse.to_json()

# convert the object into a dict
dpi_app_response_dict = dpi_app_response_instance.to_dict()
# create an instance of DpiAppResponse from a dict
dpi_app_response_form_dict = dpi_app_response.from_dict(dpi_app_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


