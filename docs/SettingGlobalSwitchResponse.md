# SettingGlobalSwitchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingGlobalSwitch]**](SettingGlobalSwitch.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.setting_global_switch_response import SettingGlobalSwitchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingGlobalSwitchResponse from a JSON string
setting_global_switch_response_instance = SettingGlobalSwitchResponse.from_json(json)
# print the JSON string representation of the object
print SettingGlobalSwitchResponse.to_json()

# convert the object into a dict
setting_global_switch_response_dict = setting_global_switch_response_instance.to_dict()
# create an instance of SettingGlobalSwitchResponse from a dict
setting_global_switch_response_form_dict = setting_global_switch_response.from_dict(setting_global_switch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


