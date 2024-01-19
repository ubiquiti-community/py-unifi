# DeviceEthernetOverrides


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ifname** | **str** |  | [optional] 
**networkgroup** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.device_ethernet_overrides import DeviceEthernetOverrides

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceEthernetOverrides from a JSON string
device_ethernet_overrides_instance = DeviceEthernetOverrides.from_json(json)
# print the JSON string representation of the object
print DeviceEthernetOverrides.to_json()

# convert the object into a dict
device_ethernet_overrides_dict = device_ethernet_overrides_instance.to_dict()
# create an instance of DeviceEthernetOverrides from a dict
device_ethernet_overrides_form_dict = device_ethernet_overrides.from_dict(device_ethernet_overrides_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


