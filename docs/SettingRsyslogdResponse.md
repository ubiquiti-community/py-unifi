# SettingRsyslogdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingRsyslogd]**](SettingRsyslogd.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from unifi_client.models.setting_rsyslogd_response import SettingRsyslogdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingRsyslogdResponse from a JSON string
setting_rsyslogd_response_instance = SettingRsyslogdResponse.from_json(json)
# print the JSON string representation of the object
print SettingRsyslogdResponse.to_json()

# convert the object into a dict
setting_rsyslogd_response_dict = setting_rsyslogd_response_instance.to_dict()
# create an instance of SettingRsyslogdResponse from a dict
setting_rsyslogd_response_form_dict = setting_rsyslogd_response.from_dict(setting_rsyslogd_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


