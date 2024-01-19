# MediaFileUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.media_file_update_request import MediaFileUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MediaFileUpdateRequest from a JSON string
media_file_update_request_instance = MediaFileUpdateRequest.from_json(json)
# print the JSON string representation of the object
print MediaFileUpdateRequest.to_json()

# convert the object into a dict
media_file_update_request_dict = media_file_update_request_instance.to_dict()
# create an instance of MediaFileUpdateRequest from a dict
media_file_update_request_form_dict = media_file_update_request.from_dict(media_file_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


