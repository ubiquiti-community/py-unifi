# SettingIps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**ad_blocking_configurations** | [**List[SettingIpsAdBlockingConfigurations]**](SettingIpsAdBlockingConfigurations.md) |  | [optional] 
**ad_blocking_enabled** | **bool** |  | [optional] 
**advanced_filtering_preference** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**dns_filtering** | **bool** |  | [optional] 
**dns_filters** | [**List[SettingIpsDNSFilters]**](SettingIpsDNSFilters.md) |  | [optional] 
**enabled_categories** | **List[str]** |  | [optional] 
**enabled_networks** | **List[str]** |  | [optional] 
**honeypot** | [**List[SettingIpsHoneypot]**](SettingIpsHoneypot.md) |  | [optional] 
**honeypot_enabled** | **bool** |  | [optional] 
**ips_mode** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**restrict_ip_addresses** | **bool** |  | [optional] 
**restrict_tor** | **bool** |  | [optional] 
**restrict_torrents** | **bool** |  | [optional] 
**site_id** | **str** |  | [optional] 
**suppression** | [**SettingIpsSuppression**](SettingIpsSuppression.md) |  | [optional] 

## Example

```python
from openapi_client.models.setting_ips import SettingIps

# TODO update the JSON string below
json = "{}"
# create an instance of SettingIps from a JSON string
setting_ips_instance = SettingIps.from_json(json)
# print the JSON string representation of the object
print SettingIps.to_json()

# convert the object into a dict
setting_ips_dict = setting_ips_instance.to_dict()
# create an instance of SettingIps from a dict
setting_ips_form_dict = setting_ips.from_dict(setting_ips_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


