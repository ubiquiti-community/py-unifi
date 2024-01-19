# PortProfileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PortProfile]**](PortProfile.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from unifi_client.models.port_profile_response import PortProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PortProfileResponse from a JSON string
port_profile_response_instance = PortProfileResponse.from_json(json)
# print the JSON string representation of the object
print PortProfileResponse.to_json()

# convert the object into a dict
port_profile_response_dict = port_profile_response_instance.to_dict()
# create an instance of PortProfileResponse from a dict
port_profile_response_form_dict = port_profile_response.from_dict(port_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


