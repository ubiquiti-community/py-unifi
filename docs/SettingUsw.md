# SettingUsw


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**dhcp_snoop** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.setting_usw import SettingUsw

# TODO update the JSON string below
json = "{}"
# create an instance of SettingUsw from a JSON string
setting_usw_instance = SettingUsw.from_json(json)
# print the JSON string representation of the object
print SettingUsw.to_json()

# convert the object into a dict
setting_usw_dict = setting_usw_instance.to_dict()
# create an instance of SettingUsw from a dict
setting_usw_form_dict = setting_usw.from_dict(setting_usw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


