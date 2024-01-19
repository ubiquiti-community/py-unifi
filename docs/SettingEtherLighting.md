# SettingEtherLighting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**network_overrides** | [**List[SettingEtherLightingNetworkOverrides]**](SettingEtherLightingNetworkOverrides.md) |  | [optional] 
**site_id** | **str** |  | [optional] 
**speed_overrides** | [**List[SettingEtherLightingSpeedOverrides]**](SettingEtherLightingSpeedOverrides.md) |  | [optional] 

## Example

```python
from openapi_client.models.setting_ether_lighting import SettingEtherLighting

# TODO update the JSON string below
json = "{}"
# create an instance of SettingEtherLighting from a JSON string
setting_ether_lighting_instance = SettingEtherLighting.from_json(json)
# print the JSON string representation of the object
print SettingEtherLighting.to_json()

# convert the object into a dict
setting_ether_lighting_dict = setting_ether_lighting_instance.to_dict()
# create an instance of SettingEtherLighting from a dict
setting_ether_lighting_form_dict = setting_ether_lighting.from_dict(setting_ether_lighting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


