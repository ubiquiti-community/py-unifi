# SettingCountryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingCountry]**](SettingCountry.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.setting_country_response import SettingCountryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingCountryResponse from a JSON string
setting_country_response_instance = SettingCountryResponse.from_json(json)
# print the JSON string representation of the object
print SettingCountryResponse.to_json()

# convert the object into a dict
setting_country_response_dict = setting_country_response_instance.to_dict()
# create an instance of SettingCountryResponse from a dict
setting_country_response_form_dict = setting_country_response.from_dict(setting_country_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


