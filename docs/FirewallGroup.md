# FirewallGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**group_members** | **List[str]** |  | [optional] 
**group_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.firewall_group import FirewallGroup

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallGroup from a JSON string
firewall_group_instance = FirewallGroup.from_json(json)
# print the JSON string representation of the object
print FirewallGroup.to_json()

# convert the object into a dict
firewall_group_dict = firewall_group_instance.to_dict()
# create an instance of FirewallGroup from a dict
firewall_group_form_dict = firewall_group.from_dict(firewall_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


