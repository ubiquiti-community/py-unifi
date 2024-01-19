# RADIUSProfileAcctServers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**x_secret** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.radius_profile_acct_servers import RADIUSProfileAcctServers

# TODO update the JSON string below
json = "{}"
# create an instance of RADIUSProfileAcctServers from a JSON string
radius_profile_acct_servers_instance = RADIUSProfileAcctServers.from_json(json)
# print the JSON string representation of the object
print RADIUSProfileAcctServers.to_json()

# convert the object into a dict
radius_profile_acct_servers_dict = radius_profile_acct_servers_instance.to_dict()
# create an instance of RADIUSProfileAcctServers from a dict
radius_profile_acct_servers_form_dict = radius_profile_acct_servers.from_dict(radius_profile_acct_servers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


