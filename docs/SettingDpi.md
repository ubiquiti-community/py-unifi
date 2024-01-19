# SettingDpi


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**fingerprinting_enabled** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.setting_dpi import SettingDpi

# TODO update the JSON string below
json = "{}"
# create an instance of SettingDpi from a JSON string
setting_dpi_instance = SettingDpi.from_json(json)
# print the JSON string representation of the object
print SettingDpi.to_json()

# convert the object into a dict
setting_dpi_dict = setting_dpi_instance.to_dict()
# create an instance of SettingDpi from a dict
setting_dpi_form_dict = setting_dpi.from_dict(setting_dpi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


