# UserGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**qos_rate_max_down** | **int** |  | [optional] 
**qos_rate_max_up** | **int** |  | [optional] 
**site_id** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.user_group import UserGroup

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroup from a JSON string
user_group_instance = UserGroup.from_json(json)
# print the JSON string representation of the object
print UserGroup.to_json()

# convert the object into a dict
user_group_dict = user_group_instance.to_dict()
# create an instance of UserGroup from a dict
user_group_form_dict = user_group.from_dict(user_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


