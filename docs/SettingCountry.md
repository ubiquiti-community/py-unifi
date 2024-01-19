# SettingCountry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**code** | **int** |  | [optional] 
**key** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.setting_country import SettingCountry

# TODO update the JSON string below
json = "{}"
# create an instance of SettingCountry from a JSON string
setting_country_instance = SettingCountry.from_json(json)
# print the JSON string representation of the object
print SettingCountry.to_json()

# convert the object into a dict
setting_country_dict = setting_country_instance.to_dict()
# create an instance of SettingCountry from a dict
setting_country_form_dict = setting_country.from_dict(setting_country_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


