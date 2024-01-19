# SettingElementAdopt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**x_element_essid** | **str** |  | [optional] 
**x_element_psk** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.setting_element_adopt import SettingElementAdopt

# TODO update the JSON string below
json = "{}"
# create an instance of SettingElementAdopt from a JSON string
setting_element_adopt_instance = SettingElementAdopt.from_json(json)
# print the JSON string representation of the object
print SettingElementAdopt.to_json()

# convert the object into a dict
setting_element_adopt_dict = setting_element_adopt_instance.to_dict()
# create an instance of SettingElementAdopt from a dict
setting_element_adopt_form_dict = setting_element_adopt.from_dict(setting_element_adopt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


