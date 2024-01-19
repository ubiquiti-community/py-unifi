# FirewallRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**action** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**contiguous** | **bool** |  | [optional] 
**dst_address** | **str** |  | [optional] 
**dst_address_ipv6** | **str** |  | [optional] 
**dst_firewallgroup_ids** | **List[str]** |  | [optional] 
**dst_networkconf_id** | **str** |  | [optional] 
**dst_networkconf_type** | **str** |  | [optional] 
**dst_port** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**icmp_typename** | **str** |  | [optional] 
**icmpv6_typename** | **str** |  | [optional] 
**ipsec** | **str** |  | [optional] 
**logging** | **bool** |  | [optional] 
**monthdays** | **str** |  | [optional] 
**monthdays_negate** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**protocol_match_excepted** | **bool** |  | [optional] 
**protocol_v6** | **str** |  | [optional] 
**rule_index** | **int** |  | [optional] 
**ruleset** | **str** |  | [optional] 
**setting_preference** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**src_address** | **str** |  | [optional] 
**src_address_ipv6** | **str** |  | [optional] 
**src_firewallgroup_ids** | **List[str]** |  | [optional] 
**src_mac_address** | **str** |  | [optional] 
**src_networkconf_id** | **str** |  | [optional] 
**src_networkconf_type** | **str** |  | [optional] 
**src_port** | **str** |  | [optional] 
**startdate** | **str** |  | [optional] 
**starttime** | **str** |  | [optional] 
**state_established** | **bool** |  | [optional] 
**state_invalid** | **bool** |  | [optional] 
**state_new** | **bool** |  | [optional] 
**state_related** | **bool** |  | [optional] 
**stopdate** | **str** |  | [optional] 
**stoptime** | **str** |  | [optional] 
**utc** | **bool** |  | [optional] 
**weekdays** | **str** |  | [optional] 
**weekdays_negate** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.firewall_rule import FirewallRule

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallRule from a JSON string
firewall_rule_instance = FirewallRule.from_json(json)
# print the JSON string representation of the object
print FirewallRule.to_json()

# convert the object into a dict
firewall_rule_dict = firewall_rule_instance.to_dict()
# create an instance of FirewallRule from a dict
firewall_rule_form_dict = firewall_rule.from_dict(firewall_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


