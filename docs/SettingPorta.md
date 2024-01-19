# SettingPorta


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
**ugw3_wan2_enabled** | **bool** |  | [optional] 

## Example

```python
from unifi_client.models.setting_porta import SettingPorta

# TODO update the JSON string below
json = "{}"
# create an instance of SettingPorta from a JSON string
setting_porta_instance = SettingPorta.from_json(json)
# print the JSON string representation of the object
print SettingPorta.to_json()

# convert the object into a dict
setting_porta_dict = setting_porta_instance.to_dict()
# create an instance of SettingPorta from a dict
setting_porta_form_dict = setting_porta.from_dict(setting_porta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


