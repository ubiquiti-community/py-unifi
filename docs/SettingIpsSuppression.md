# SettingIpsSuppression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | [**List[SettingIpsAlerts]**](SettingIpsAlerts.md) |  | [optional] 
**whitelist** | [**List[SettingIpsWhitelist]**](SettingIpsWhitelist.md) |  | [optional] 

## Example

```python
from openapi_client.models.setting_ips_suppression import SettingIpsSuppression

# TODO update the JSON string below
json = "{}"
# create an instance of SettingIpsSuppression from a JSON string
setting_ips_suppression_instance = SettingIpsSuppression.from_json(json)
# print the JSON string representation of the object
print SettingIpsSuppression.to_json()

# convert the object into a dict
setting_ips_suppression_dict = setting_ips_suppression_instance.to_dict()
# create an instance of SettingIpsSuppression from a dict
setting_ips_suppression_form_dict = setting_ips_suppression.from_dict(setting_ips_suppression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


