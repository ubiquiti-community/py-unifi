# DeviceRpsOverride


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**power_management_mode** | **str** |  | [optional] 
**rps_port_table** | [**List[DeviceRpsPortTable]**](DeviceRpsPortTable.md) |  | [optional] 

## Example

```python
from openapi_client.models.device_rps_override import DeviceRpsOverride

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceRpsOverride from a JSON string
device_rps_override_instance = DeviceRpsOverride.from_json(json)
# print the JSON string representation of the object
print DeviceRpsOverride.to_json()

# convert the object into a dict
device_rps_override_dict = device_rps_override_instance.to_dict()
# create an instance of DeviceRpsOverride from a dict
device_rps_override_form_dict = device_rps_override.from_dict(device_rps_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


