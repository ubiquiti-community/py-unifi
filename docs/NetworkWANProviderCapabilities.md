# NetworkWANProviderCapabilities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_kilobits_per_second** | **int** |  | [optional] 
**upload_kilobits_per_second** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.network_wan_provider_capabilities import NetworkWANProviderCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkWANProviderCapabilities from a JSON string
network_wan_provider_capabilities_instance = NetworkWANProviderCapabilities.from_json(json)
# print the JSON string representation of the object
print NetworkWANProviderCapabilities.to_json()

# convert the object into a dict
network_wan_provider_capabilities_dict = network_wan_provider_capabilities_instance.to_dict()
# create an instance of NetworkWANProviderCapabilities from a dict
network_wan_provider_capabilities_form_dict = network_wan_provider_capabilities.from_dict(network_wan_provider_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


