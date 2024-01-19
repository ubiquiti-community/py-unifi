# BroadcastGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**member_table** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.broadcast_group import BroadcastGroup

# TODO update the JSON string below
json = "{}"
# create an instance of BroadcastGroup from a JSON string
broadcast_group_instance = BroadcastGroup.from_json(json)
# print the JSON string representation of the object
print BroadcastGroup.to_json()

# convert the object into a dict
broadcast_group_dict = broadcast_group_instance.to_dict()
# create an instance of BroadcastGroup from a dict
broadcast_group_form_dict = broadcast_group.from_dict(broadcast_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


