# BroadcastGroupUpdateRequest


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
from unifi_client.models.broadcast_group_update_request import BroadcastGroupUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BroadcastGroupUpdateRequest from a JSON string
broadcast_group_update_request_instance = BroadcastGroupUpdateRequest.from_json(json)
# print the JSON string representation of the object
print BroadcastGroupUpdateRequest.to_json()

# convert the object into a dict
broadcast_group_update_request_dict = broadcast_group_update_request_instance.to_dict()
# create an instance of BroadcastGroupUpdateRequest from a dict
broadcast_group_update_request_form_dict = broadcast_group_update_request.from_dict(broadcast_group_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


