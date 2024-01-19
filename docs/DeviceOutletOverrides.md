# DeviceOutletOverrides


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cycle_enabled** | **bool** |  | [optional] 
**index** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**relay_state** | **bool** |  | [optional] 

## Example

```python
from unifi_client.models.device_outlet_overrides import DeviceOutletOverrides

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceOutletOverrides from a JSON string
device_outlet_overrides_instance = DeviceOutletOverrides.from_json(json)
# print the JSON string representation of the object
print DeviceOutletOverrides.to_json()

# convert the object into a dict
device_outlet_overrides_dict = device_outlet_overrides_instance.to_dict()
# create an instance of DeviceOutletOverrides from a dict
device_outlet_overrides_form_dict = device_outlet_overrides.from_dict(device_outlet_overrides_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


