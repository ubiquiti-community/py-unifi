# SettingSuperSmtpResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingSuperSmtp]**](SettingSuperSmtp.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from unifi_client.models.setting_super_smtp_response import SettingSuperSmtpResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingSuperSmtpResponse from a JSON string
setting_super_smtp_response_instance = SettingSuperSmtpResponse.from_json(json)
# print the JSON string representation of the object
print SettingSuperSmtpResponse.to_json()

# convert the object into a dict
setting_super_smtp_response_dict = setting_super_smtp_response_instance.to_dict()
# create an instance of SettingSuperSmtpResponse from a dict
setting_super_smtp_response_form_dict = setting_super_smtp_response.from_dict(setting_super_smtp_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


