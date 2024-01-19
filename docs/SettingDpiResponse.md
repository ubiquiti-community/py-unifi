# SettingDpiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingDpi]**](SettingDpi.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from unifi_client.models.setting_dpi_response import SettingDpiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingDpiResponse from a JSON string
setting_dpi_response_instance = SettingDpiResponse.from_json(json)
# print the JSON string representation of the object
print SettingDpiResponse.to_json()

# convert the object into a dict
setting_dpi_response_dict = setting_dpi_response_instance.to_dict()
# create an instance of SettingDpiResponse from a dict
setting_dpi_response_form_dict = setting_dpi_response.from_dict(setting_dpi_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


