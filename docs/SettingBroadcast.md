# SettingBroadcast


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**sound_after_enabled** | **bool** |  | [optional] 
**sound_after_resource** | **str** |  | [optional] 
**sound_after_type** | **str** |  | [optional] 
**sound_before_enabled** | **bool** |  | [optional] 
**sound_before_resource** | **str** |  | [optional] 
**sound_before_type** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.setting_broadcast import SettingBroadcast

# TODO update the JSON string below
json = "{}"
# create an instance of SettingBroadcast from a JSON string
setting_broadcast_instance = SettingBroadcast.from_json(json)
# print the JSON string representation of the object
print SettingBroadcast.to_json()

# convert the object into a dict
setting_broadcast_dict = setting_broadcast_instance.to_dict()
# create an instance of SettingBroadcast from a dict
setting_broadcast_form_dict = setting_broadcast.from_dict(setting_broadcast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


