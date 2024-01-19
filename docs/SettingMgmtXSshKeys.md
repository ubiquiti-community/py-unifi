# SettingMgmtXSshKeys


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**fingerprint** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.setting_mgmt_x_ssh_keys import SettingMgmtXSshKeys

# TODO update the JSON string below
json = "{}"
# create an instance of SettingMgmtXSshKeys from a JSON string
setting_mgmt_x_ssh_keys_instance = SettingMgmtXSshKeys.from_json(json)
# print the JSON string representation of the object
print SettingMgmtXSshKeys.to_json()

# convert the object into a dict
setting_mgmt_x_ssh_keys_dict = setting_mgmt_x_ssh_keys_instance.to_dict()
# create an instance of SettingMgmtXSshKeys from a dict
setting_mgmt_x_ssh_keys_form_dict = setting_mgmt_x_ssh_keys.from_dict(setting_mgmt_x_ssh_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


