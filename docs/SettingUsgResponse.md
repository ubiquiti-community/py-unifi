# SettingUsgResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingUsg]**](SettingUsg.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.setting_usg_response import SettingUsgResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingUsgResponse from a JSON string
setting_usg_response_instance = SettingUsgResponse.from_json(json)
# print the JSON string representation of the object
print SettingUsgResponse.to_json()

# convert the object into a dict
setting_usg_response_dict = setting_usg_response_instance.to_dict()
# create an instance of SettingUsgResponse from a dict
setting_usg_response_form_dict = setting_usg_response.from_dict(setting_usg_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


