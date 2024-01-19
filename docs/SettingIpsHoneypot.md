# SettingIpsHoneypot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** |  | [optional] 
**network_id** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.setting_ips_honeypot import SettingIpsHoneypot

# TODO update the JSON string below
json = "{}"
# create an instance of SettingIpsHoneypot from a JSON string
setting_ips_honeypot_instance = SettingIpsHoneypot.from_json(json)
# print the JSON string representation of the object
print SettingIpsHoneypot.to_json()

# convert the object into a dict
setting_ips_honeypot_dict = setting_ips_honeypot_instance.to_dict()
# create an instance of SettingIpsHoneypot from a dict
setting_ips_honeypot_form_dict = setting_ips_honeypot.from_dict(setting_ips_honeypot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


