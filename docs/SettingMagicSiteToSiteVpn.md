# SettingMagicSiteToSiteVpn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.setting_magic_site_to_site_vpn import SettingMagicSiteToSiteVpn

# TODO update the JSON string below
json = "{}"
# create an instance of SettingMagicSiteToSiteVpn from a JSON string
setting_magic_site_to_site_vpn_instance = SettingMagicSiteToSiteVpn.from_json(json)
# print the JSON string representation of the object
print SettingMagicSiteToSiteVpn.to_json()

# convert the object into a dict
setting_magic_site_to_site_vpn_dict = setting_magic_site_to_site_vpn_instance.to_dict()
# create an instance of SettingMagicSiteToSiteVpn from a dict
setting_magic_site_to_site_vpn_form_dict = setting_magic_site_to_site_vpn.from_dict(setting_magic_site_to_site_vpn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


