# DynamicDNSResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DynamicDNS]**](DynamicDNS.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from unifi_client.models.dynamic_dns_response import DynamicDNSResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicDNSResponse from a JSON string
dynamic_dns_response_instance = DynamicDNSResponse.from_json(json)
# print the JSON string representation of the object
print DynamicDNSResponse.to_json()

# convert the object into a dict
dynamic_dns_response_dict = dynamic_dns_response_instance.to_dict()
# create an instance of DynamicDNSResponse from a dict
dynamic_dns_response_form_dict = dynamic_dns_response.from_dict(dynamic_dns_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


