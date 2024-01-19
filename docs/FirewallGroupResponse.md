# FirewallGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FirewallGroup]**](FirewallGroup.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.firewall_group_response import FirewallGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallGroupResponse from a JSON string
firewall_group_response_instance = FirewallGroupResponse.from_json(json)
# print the JSON string representation of the object
print FirewallGroupResponse.to_json()

# convert the object into a dict
firewall_group_response_dict = firewall_group_response_instance.to_dict()
# create an instance of FirewallGroupResponse from a dict
firewall_group_response_form_dict = firewall_group_response.from_dict(firewall_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


