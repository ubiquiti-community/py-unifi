# RADIUSProfileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RADIUSProfile]**](RADIUSProfile.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.radius_profile_response import RADIUSProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RADIUSProfileResponse from a JSON string
radius_profile_response_instance = RADIUSProfileResponse.from_json(json)
# print the JSON string representation of the object
print RADIUSProfileResponse.to_json()

# convert the object into a dict
radius_profile_response_dict = radius_profile_response_instance.to_dict()
# create an instance of RADIUSProfileResponse from a dict
radius_profile_response_form_dict = radius_profile_response.from_dict(radius_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


