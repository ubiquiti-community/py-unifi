# RADIUSProfileAuthServers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**x_secret** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.radius_profile_auth_servers import RADIUSProfileAuthServers

# TODO update the JSON string below
json = "{}"
# create an instance of RADIUSProfileAuthServers from a JSON string
radius_profile_auth_servers_instance = RADIUSProfileAuthServers.from_json(json)
# print the JSON string representation of the object
print RADIUSProfileAuthServers.to_json()

# convert the object into a dict
radius_profile_auth_servers_dict = radius_profile_auth_servers_instance.to_dict()
# create an instance of RADIUSProfileAuthServers from a dict
radius_profile_auth_servers_form_dict = radius_profile_auth_servers.from_dict(radius_profile_auth_servers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


