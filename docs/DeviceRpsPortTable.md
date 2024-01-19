# DeviceRpsPortTable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**port_idx** | **int** |  | [optional] 
**port_mode** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.device_rps_port_table import DeviceRpsPortTable

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceRpsPortTable from a JSON string
device_rps_port_table_instance = DeviceRpsPortTable.from_json(json)
# print the JSON string representation of the object
print DeviceRpsPortTable.to_json()

# convert the object into a dict
device_rps_port_table_dict = device_rps_port_table_instance.to_dict()
# create an instance of DeviceRpsPortTable from a dict
device_rps_port_table_form_dict = device_rps_port_table.from_dict(device_rps_port_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


