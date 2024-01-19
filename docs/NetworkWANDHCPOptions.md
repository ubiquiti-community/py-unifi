# NetworkWANDHCPOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option_number** | **int** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.network_wandhcp_options import NetworkWANDHCPOptions

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkWANDHCPOptions from a JSON string
network_wandhcp_options_instance = NetworkWANDHCPOptions.from_json(json)
# print the JSON string representation of the object
print NetworkWANDHCPOptions.to_json()

# convert the object into a dict
network_wandhcp_options_dict = network_wandhcp_options_instance.to_dict()
# create an instance of NetworkWANDHCPOptions from a dict
network_wandhcp_options_form_dict = network_wandhcp_options.from_dict(network_wandhcp_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


