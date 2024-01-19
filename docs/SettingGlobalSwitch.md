# SettingGlobalSwitch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**dhcp_snoop** | **bool** |  | [optional] 
**dot1x_fallback_networkconf_id** | **str** |  | [optional] 
**dot1x_portctrl_enabled** | **bool** |  | [optional] 
**flowctrl_enabled** | **bool** |  | [optional] 
**jumboframe_enabled** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**radiusprofile_id** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**stp_version** | **str** |  | [optional] 
**switch_exclusions** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.setting_global_switch import SettingGlobalSwitch

# TODO update the JSON string below
json = "{}"
# create an instance of SettingGlobalSwitch from a JSON string
setting_global_switch_instance = SettingGlobalSwitch.from_json(json)
# print the JSON string representation of the object
print SettingGlobalSwitch.to_json()

# convert the object into a dict
setting_global_switch_dict = setting_global_switch_instance.to_dict()
# create an instance of SettingGlobalSwitch from a dict
setting_global_switch_form_dict = setting_global_switch.from_dict(setting_global_switch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


