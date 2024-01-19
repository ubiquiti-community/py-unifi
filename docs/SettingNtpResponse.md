# SettingNtpResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingNtp]**](SettingNtp.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from unifi_client.models.setting_ntp_response import SettingNtpResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingNtpResponse from a JSON string
setting_ntp_response_instance = SettingNtpResponse.from_json(json)
# print the JSON string representation of the object
print SettingNtpResponse.to_json()

# convert the object into a dict
setting_ntp_response_dict = setting_ntp_response_instance.to_dict()
# create an instance of SettingNtpResponse from a dict
setting_ntp_response_form_dict = setting_ntp_response.from_dict(setting_ntp_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


