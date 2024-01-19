# SettingEtherLightingNetworkOverrides


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**raw_color_hex** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.setting_ether_lighting_network_overrides import SettingEtherLightingNetworkOverrides

# TODO update the JSON string below
json = "{}"
# create an instance of SettingEtherLightingNetworkOverrides from a JSON string
setting_ether_lighting_network_overrides_instance = SettingEtherLightingNetworkOverrides.from_json(json)
# print the JSON string representation of the object
print SettingEtherLightingNetworkOverrides.to_json()

# convert the object into a dict
setting_ether_lighting_network_overrides_dict = setting_ether_lighting_network_overrides_instance.to_dict()
# create an instance of SettingEtherLightingNetworkOverrides from a dict
setting_ether_lighting_network_overrides_form_dict = setting_ether_lighting_network_overrides.from_dict(setting_ether_lighting_network_overrides_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


