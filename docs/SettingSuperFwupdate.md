# SettingSuperFwupdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**controller_channel** | **str** |  | [optional] 
**firmware_channel** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**sso_enabled** | **bool** |  | [optional] 

## Example

```python
from unifi_client.models.setting_super_fwupdate import SettingSuperFwupdate

# TODO update the JSON string below
json = "{}"
# create an instance of SettingSuperFwupdate from a JSON string
setting_super_fwupdate_instance = SettingSuperFwupdate.from_json(json)
# print the JSON string representation of the object
print SettingSuperFwupdate.to_json()

# convert the object into a dict
setting_super_fwupdate_dict = setting_super_fwupdate_instance.to_dict()
# create an instance of SettingSuperFwupdate from a dict
setting_super_fwupdate_form_dict = setting_super_fwupdate.from_dict(setting_super_fwupdate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


