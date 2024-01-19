# TagUpdateRequest


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
from openapi_client.models.tag_update_request import TagUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TagUpdateRequest from a JSON string
tag_update_request_instance = TagUpdateRequest.from_json(json)
# print the JSON string representation of the object
print TagUpdateRequest.to_json()

# convert the object into a dict
tag_update_request_dict = tag_update_request_instance.to_dict()
# create an instance of TagUpdateRequest from a dict
tag_update_request_form_dict = tag_update_request.from_dict(tag_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


