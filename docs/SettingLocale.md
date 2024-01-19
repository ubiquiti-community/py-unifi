# SettingLocale


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.setting_locale import SettingLocale

# TODO update the JSON string below
json = "{}"
# create an instance of SettingLocale from a JSON string
setting_locale_instance = SettingLocale.from_json(json)
# print the JSON string representation of the object
print SettingLocale.to_json()

# convert the object into a dict
setting_locale_dict = setting_locale_instance.to_dict()
# create an instance of SettingLocale from a dict
setting_locale_form_dict = setting_locale.from_dict(setting_locale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


