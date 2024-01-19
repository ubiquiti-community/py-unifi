# BroadcastGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BroadcastGroup]**](BroadcastGroup.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.broadcast_group_response import BroadcastGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BroadcastGroupResponse from a JSON string
broadcast_group_response_instance = BroadcastGroupResponse.from_json(json)
# print the JSON string representation of the object
print BroadcastGroupResponse.to_json()

# convert the object into a dict
broadcast_group_response_dict = broadcast_group_response_instance.to_dict()
# create an instance of BroadcastGroupResponse from a dict
broadcast_group_response_form_dict = broadcast_group_response.from_dict(broadcast_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


