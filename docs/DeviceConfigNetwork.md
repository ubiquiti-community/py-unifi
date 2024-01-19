# DeviceConfigNetwork


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bonding_enabled** | **bool** |  | [optional] 
**dns1** | **str** |  | [optional] 
**dns2** | **str** |  | [optional] 
**dnssuffix** | **str** |  | [optional] 
**gateway** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**netmask** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.device_config_network import DeviceConfigNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceConfigNetwork from a JSON string
device_config_network_instance = DeviceConfigNetwork.from_json(json)
# print the JSON string representation of the object
print DeviceConfigNetwork.to_json()

# convert the object into a dict
device_config_network_dict = device_config_network_instance.to_dict()
# create an instance of DeviceConfigNetwork from a dict
device_config_network_form_dict = device_config_network.from_dict(device_config_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


