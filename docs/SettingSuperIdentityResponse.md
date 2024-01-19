# SettingSuperIdentityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingSuperIdentity]**](SettingSuperIdentity.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from unifi_client.models.setting_super_identity_response import SettingSuperIdentityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingSuperIdentityResponse from a JSON string
setting_super_identity_response_instance = SettingSuperIdentityResponse.from_json(json)
# print the JSON string representation of the object
print SettingSuperIdentityResponse.to_json()

# convert the object into a dict
setting_super_identity_response_dict = setting_super_identity_response_instance.to_dict()
# create an instance of SettingSuperIdentityResponse from a dict
setting_super_identity_response_form_dict = setting_super_identity_response.from_dict(setting_super_identity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


