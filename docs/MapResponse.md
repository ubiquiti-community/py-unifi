# MapResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Map]**](Map.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from unifi_client.models.map_response import MapResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MapResponse from a JSON string
map_response_instance = MapResponse.from_json(json)
# print the JSON string representation of the object
print MapResponse.to_json()

# convert the object into a dict
map_response_dict = map_response_instance.to_dict()
# create an instance of MapResponse from a dict
map_response_form_dict = map_response.from_dict(map_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


