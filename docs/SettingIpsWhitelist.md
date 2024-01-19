# SettingIpsWhitelist


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.setting_ips_whitelist import SettingIpsWhitelist

# TODO update the JSON string below
json = "{}"
# create an instance of SettingIpsWhitelist from a JSON string
setting_ips_whitelist_instance = SettingIpsWhitelist.from_json(json)
# print the JSON string representation of the object
print SettingIpsWhitelist.to_json()

# convert the object into a dict
setting_ips_whitelist_dict = setting_ips_whitelist_instance.to_dict()
# create an instance of SettingIpsWhitelist from a dict
setting_ips_whitelist_form_dict = setting_ips_whitelist.from_dict(setting_ips_whitelist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


