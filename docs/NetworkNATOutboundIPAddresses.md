# NetworkNATOutboundIPAddresses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** |  | [optional] 
**wan_network_group** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.network_nat_outbound_ip_addresses import NetworkNATOutboundIPAddresses

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkNATOutboundIPAddresses from a JSON string
network_nat_outbound_ip_addresses_instance = NetworkNATOutboundIPAddresses.from_json(json)
# print the JSON string representation of the object
print NetworkNATOutboundIPAddresses.to_json()

# convert the object into a dict
network_nat_outbound_ip_addresses_dict = network_nat_outbound_ip_addresses_instance.to_dict()
# create an instance of NetworkNATOutboundIPAddresses from a dict
network_nat_outbound_ip_addresses_form_dict = network_nat_outbound_ip_addresses.from_dict(network_nat_outbound_ip_addresses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


