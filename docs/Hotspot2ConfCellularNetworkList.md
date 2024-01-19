# Hotspot2ConfCellularNetworkList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mcc** | **int** |  | [optional] 
**mnc** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.hotspot2_conf_cellular_network_list import Hotspot2ConfCellularNetworkList

# TODO update the JSON string below
json = "{}"
# create an instance of Hotspot2ConfCellularNetworkList from a JSON string
hotspot2_conf_cellular_network_list_instance = Hotspot2ConfCellularNetworkList.from_json(json)
# print the JSON string representation of the object
print Hotspot2ConfCellularNetworkList.to_json()

# convert the object into a dict
hotspot2_conf_cellular_network_list_dict = hotspot2_conf_cellular_network_list_instance.to_dict()
# create an instance of Hotspot2ConfCellularNetworkList from a dict
hotspot2_conf_cellular_network_list_form_dict = hotspot2_conf_cellular_network_list.from_dict(hotspot2_conf_cellular_network_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


