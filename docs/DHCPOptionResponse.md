# DHCPOptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DHCPOption]**](DHCPOption.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.dhcp_option_response import DHCPOptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DHCPOptionResponse from a JSON string
dhcp_option_response_instance = DHCPOptionResponse.from_json(json)
# print the JSON string representation of the object
print DHCPOptionResponse.to_json()

# convert the object into a dict
dhcp_option_response_dict = dhcp_option_response_instance.to_dict()
# create an instance of DHCPOptionResponse from a dict
dhcp_option_response_form_dict = dhcp_option_response.from_dict(dhcp_option_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


