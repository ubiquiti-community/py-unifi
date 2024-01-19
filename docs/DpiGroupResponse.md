# DpiGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DpiGroup]**](DpiGroup.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.dpi_group_response import DpiGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DpiGroupResponse from a JSON string
dpi_group_response_instance = DpiGroupResponse.from_json(json)
# print the JSON string representation of the object
print DpiGroupResponse.to_json()

# convert the object into a dict
dpi_group_response_dict = dpi_group_response_instance.to_dict()
# create an instance of DpiGroupResponse from a dict
dpi_group_response_form_dict = dpi_group_response.from_dict(dpi_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


