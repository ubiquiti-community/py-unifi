# SettingMgmt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**advanced_feature_enabled** | **bool** |  | [optional] 
**alert_enabled** | **bool** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**auto_upgrade** | **bool** |  | [optional] 
**auto_upgrade_hour** | **int** |  | [optional] 
**boot_sound** | **bool** |  | [optional] 
**debug_tools_enabled** | **bool** |  | [optional] 
**direct_connect_enabled** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**led_enabled** | **bool** |  | [optional] 
**outdoor_mode_enabled** | **bool** |  | [optional] 
**site_id** | **str** |  | [optional] 
**unifi_idp_enabled** | **bool** |  | [optional] 
**wifiman_enabled** | **bool** |  | [optional] 
**x_mgmt_key** | **str** |  | [optional] 
**x_ssh_auth_password_enabled** | **bool** |  | [optional] 
**x_ssh_bind_wildcard** | **bool** |  | [optional] 
**x_ssh_enabled** | **bool** |  | [optional] 
**x_ssh_keys** | [**List[SettingMgmtXSshKeys]**](SettingMgmtXSshKeys.md) |  | [optional] 
**x_ssh_md5passwd** | **str** |  | [optional] 
**x_ssh_password** | **str** |  | [optional] 
**x_ssh_sha512passwd** | **str** |  | [optional] 
**x_ssh_username** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.setting_mgmt import SettingMgmt

# TODO update the JSON string below
json = "{}"
# create an instance of SettingMgmt from a JSON string
setting_mgmt_instance = SettingMgmt.from_json(json)
# print the JSON string representation of the object
print SettingMgmt.to_json()

# convert the object into a dict
setting_mgmt_dict = setting_mgmt_instance.to_dict()
# create an instance of SettingMgmt from a dict
setting_mgmt_form_dict = setting_mgmt.from_dict(setting_mgmt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


