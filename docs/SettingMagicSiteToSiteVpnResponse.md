# SettingMagicSiteToSiteVpnResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingMagicSiteToSiteVpn]**](SettingMagicSiteToSiteVpn.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from unifi_client.models.setting_magic_site_to_site_vpn_response import SettingMagicSiteToSiteVpnResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingMagicSiteToSiteVpnResponse from a JSON string
setting_magic_site_to_site_vpn_response_instance = SettingMagicSiteToSiteVpnResponse.from_json(json)
# print the JSON string representation of the object
print SettingMagicSiteToSiteVpnResponse.to_json()

# convert the object into a dict
setting_magic_site_to_site_vpn_response_dict = setting_magic_site_to_site_vpn_response_instance.to_dict()
# create an instance of SettingMagicSiteToSiteVpnResponse from a dict
setting_magic_site_to_site_vpn_response_form_dict = setting_magic_site_to_site_vpn_response.from_dict(setting_magic_site_to_site_vpn_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


