# FirewallRuleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FirewallRule]**](FirewallRule.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.firewall_rule_response import FirewallRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallRuleResponse from a JSON string
firewall_rule_response_instance = FirewallRuleResponse.from_json(json)
# print the JSON string representation of the object
print FirewallRuleResponse.to_json()

# convert the object into a dict
firewall_rule_response_dict = firewall_rule_response_instance.to_dict()
# create an instance of FirewallRuleResponse from a dict
firewall_rule_response_form_dict = firewall_rule_response.from_dict(firewall_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


