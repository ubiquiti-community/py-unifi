# SettingTeleport


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
**subnet_cidr** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.setting_teleport import SettingTeleport

# TODO update the JSON string below
json = "{}"
# create an instance of SettingTeleport from a JSON string
setting_teleport_instance = SettingTeleport.from_json(json)
# print the JSON string representation of the object
print SettingTeleport.to_json()

# convert the object into a dict
setting_teleport_dict = setting_teleport_instance.to_dict()
# create an instance of SettingTeleport from a dict
setting_teleport_form_dict = setting_teleport.from_dict(setting_teleport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


