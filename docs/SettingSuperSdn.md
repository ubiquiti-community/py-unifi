# SettingSuperSdn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**auth_token** | **str** |  | [optional] 
**device_id** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**migrated** | **bool** |  | [optional] 
**site_id** | **str** |  | [optional] 
**sso_login_enabled** | **str** |  | [optional] 
**ubic_uuid** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.setting_super_sdn import SettingSuperSdn

# TODO update the JSON string below
json = "{}"
# create an instance of SettingSuperSdn from a JSON string
setting_super_sdn_instance = SettingSuperSdn.from_json(json)
# print the JSON string representation of the object
print SettingSuperSdn.to_json()

# convert the object into a dict
setting_super_sdn_dict = setting_super_sdn_instance.to_dict()
# create an instance of SettingSuperSdn from a dict
setting_super_sdn_form_dict = setting_super_sdn.from_dict(setting_super_sdn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


