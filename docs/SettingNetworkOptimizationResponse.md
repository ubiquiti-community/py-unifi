# SettingNetworkOptimizationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingNetworkOptimization]**](SettingNetworkOptimization.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from unifi_client.models.setting_network_optimization_response import SettingNetworkOptimizationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingNetworkOptimizationResponse from a JSON string
setting_network_optimization_response_instance = SettingNetworkOptimizationResponse.from_json(json)
# print the JSON string representation of the object
print SettingNetworkOptimizationResponse.to_json()

# convert the object into a dict
setting_network_optimization_response_dict = setting_network_optimization_response_instance.to_dict()
# create an instance of SettingNetworkOptimizationResponse from a dict
setting_network_optimization_response_form_dict = setting_network_optimization_response.from_dict(setting_network_optimization_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


