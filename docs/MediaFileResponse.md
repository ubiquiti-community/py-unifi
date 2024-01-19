# MediaFileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MediaFile]**](MediaFile.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from unifi_client.models.media_file_response import MediaFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MediaFileResponse from a JSON string
media_file_response_instance = MediaFileResponse.from_json(json)
# print the JSON string representation of the object
print MediaFileResponse.to_json()

# convert the object into a dict
media_file_response_dict = media_file_response_instance.to_dict()
# create an instance of MediaFileResponse from a dict
media_file_response_form_dict = media_file_response.from_dict(media_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


