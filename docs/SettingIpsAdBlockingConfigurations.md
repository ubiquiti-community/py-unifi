# SettingIpsAdBlockingConfigurations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_id** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.setting_ips_ad_blocking_configurations import SettingIpsAdBlockingConfigurations

# TODO update the JSON string below
json = "{}"
# create an instance of SettingIpsAdBlockingConfigurations from a JSON string
setting_ips_ad_blocking_configurations_instance = SettingIpsAdBlockingConfigurations.from_json(json)
# print the JSON string representation of the object
print SettingIpsAdBlockingConfigurations.to_json()

# convert the object into a dict
setting_ips_ad_blocking_configurations_dict = setting_ips_ad_blocking_configurations_instance.to_dict()
# create an instance of SettingIpsAdBlockingConfigurations from a dict
setting_ips_ad_blocking_configurations_form_dict = setting_ips_ad_blocking_configurations.from_dict(setting_ips_ad_blocking_configurations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


