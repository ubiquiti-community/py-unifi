# SettingNetworkOptimization


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

## Example

```python
from unifi_client.models.setting_network_optimization import SettingNetworkOptimization

# TODO update the JSON string below
json = "{}"
# create an instance of SettingNetworkOptimization from a JSON string
setting_network_optimization_instance = SettingNetworkOptimization.from_json(json)
# print the JSON string representation of the object
print SettingNetworkOptimization.to_json()

# convert the object into a dict
setting_network_optimization_dict = setting_network_optimization_instance.to_dict()
# create an instance of SettingNetworkOptimization from a dict
setting_network_optimization_form_dict = setting_network_optimization.from_dict(setting_network_optimization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


