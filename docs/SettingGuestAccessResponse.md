# SettingGuestAccessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingGuestAccess]**](SettingGuestAccess.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from unifi_client.models.setting_guest_access_response import SettingGuestAccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingGuestAccessResponse from a JSON string
setting_guest_access_response_instance = SettingGuestAccessResponse.from_json(json)
# print the JSON string representation of the object
print SettingGuestAccessResponse.to_json()

# convert the object into a dict
setting_guest_access_response_dict = setting_guest_access_response_instance.to_dict()
# create an instance of SettingGuestAccessResponse from a dict
setting_guest_access_response_form_dict = setting_guest_access_response.from_dict(setting_guest_access_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


