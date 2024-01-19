# SettingLocaleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingLocale]**](SettingLocale.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.setting_locale_response import SettingLocaleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingLocaleResponse from a JSON string
setting_locale_response_instance = SettingLocaleResponse.from_json(json)
# print the JSON string representation of the object
print SettingLocaleResponse.to_json()

# convert the object into a dict
setting_locale_response_dict = setting_locale_response_instance.to_dict()
# create an instance of SettingLocaleResponse from a dict
setting_locale_response_form_dict = setting_locale_response.from_dict(setting_locale_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


