# DeviceRadioTable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**antenna_gain** | **int** |  | [optional] 
**antenna_id** | **int** |  | [optional] 
**backup_channel** | **str** |  | [optional] 
**channel** | **str** |  | [optional] 
**channel_optimization_enabled** | **bool** |  | [optional] 
**hard_noise_floor_enabled** | **bool** |  | [optional] 
**ht** | **int** |  | [optional] 
**loadbalance_enabled** | **bool** |  | [optional] 
**maxsta** | **int** |  | [optional] 
**min_rssi** | **int** |  | [optional] 
**min_rssi_enabled** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**radio** | **str** |  | [optional] 
**radio_identifiers** | [**List[DeviceRadioIDentifiers]**](DeviceRadioIDentifiers.md) |  | [optional] 
**sens_level** | **int** |  | [optional] 
**sens_level_enabled** | **bool** |  | [optional] 
**tx_power** | **str** |  | [optional] 
**tx_power_mode** | **str** |  | [optional] 
**vwire_enabled** | **bool** |  | [optional] 

## Example

```python
from unifi_client.models.device_radio_table import DeviceRadioTable

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceRadioTable from a JSON string
device_radio_table_instance = DeviceRadioTable.from_json(json)
# print the JSON string representation of the object
print DeviceRadioTable.to_json()

# convert the object into a dict
device_radio_table_dict = device_radio_table_instance.to_dict()
# create an instance of DeviceRadioTable from a dict
device_radio_table_form_dict = device_radio_table.from_dict(device_radio_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


