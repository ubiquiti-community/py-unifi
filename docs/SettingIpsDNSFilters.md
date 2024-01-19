# SettingIpsDNSFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_sites** | **List[str]** |  | [optional] 
**blocked_sites** | **List[str]** |  | [optional] 
**blocked_tld** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**filter** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**network_id** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.setting_ips_dns_filters import SettingIpsDNSFilters

# TODO update the JSON string below
json = "{}"
# create an instance of SettingIpsDNSFilters from a JSON string
setting_ips_dns_filters_instance = SettingIpsDNSFilters.from_json(json)
# print the JSON string representation of the object
print SettingIpsDNSFilters.to_json()

# convert the object into a dict
setting_ips_dns_filters_dict = setting_ips_dns_filters_instance.to_dict()
# create an instance of SettingIpsDNSFilters from a dict
setting_ips_dns_filters_form_dict = setting_ips_dns_filters.from_dict(setting_ips_dns_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


