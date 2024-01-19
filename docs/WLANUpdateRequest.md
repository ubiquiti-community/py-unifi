# WLANUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**ap_group_ids** | **List[str]** |  | [optional] 
**ap_group_mode** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**auth_cache** | **bool** |  | [optional] 
**b_supported** | **bool** |  | [optional] 
**bc_filter_enabled** | **bool** |  | [optional] 
**bc_filter_list** | **List[str]** |  | [optional] 
**bss_transition** | **bool** |  | [optional] 
**country_beacon** | **bool** |  | [optional] 
**dpi_enabled** | **bool** |  | [optional] 
**dpigroup_id** | **str** |  | [optional] 
**dtim_6e** | **int** |  | [optional] 
**dtim_mode** | **str** |  | [optional] 
**dtim_na** | **int** |  | [optional] 
**dtim_ng** | **int** |  | [optional] 
**element_adopt** | **bool** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**fast_roaming_enabled** | **bool** |  | [optional] 
**group_rekey** | **int** |  | [optional] 
**hide_ssid** | **bool** |  | [optional] 
**hotspot2conf_enabled** | **bool** |  | [optional] 
**hotspot2conf_id** | **str** |  | [optional] 
**iapp_enabled** | **bool** |  | [optional] 
**is_guest** | **bool** |  | [optional] 
**l2_isolation** | **bool** |  | [optional] 
**log_level** | **str** |  | [optional] 
**mac_filter_enabled** | **bool** |  | [optional] 
**mac_filter_list** | **List[str]** |  | [optional] 
**mac_filter_policy** | **str** |  | [optional] 
**mcastenhance_enabled** | **bool** |  | [optional] 
**minrate_na_advertising_rates** | **bool** |  | [optional] 
**minrate_na_data_rate_kbps** | **int** |  | [optional] 
**minrate_na_enabled** | **bool** |  | [optional] 
**minrate_ng_advertising_rates** | **bool** |  | [optional] 
**minrate_ng_data_rate_kbps** | **int** |  | [optional] 
**minrate_ng_enabled** | **bool** |  | [optional] 
**minrate_setting_preference** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**name_combine_enabled** | **bool** |  | [optional] 
**name_combine_suffix** | **str** |  | [optional] 
**networkconf_id** | **str** |  | [optional] 
**no2ghz_oui** | **bool** |  | [optional] 
**optimize_iot_wifi_connectivity** | **bool** |  | [optional] 
**p2p** | **bool** |  | [optional] 
**p2p_cross_connect** | **bool** |  | [optional] 
**pmf_cipher** | **str** |  | [optional] 
**pmf_mode** | **str** |  | [optional] 
**priority** | **str** |  | [optional] 
**private_preshared_keys** | [**List[WLANPrivatePresharedKeys]**](WLANPrivatePresharedKeys.md) |  | [optional] 
**private_preshared_keys_enabled** | **bool** |  | [optional] 
**proxy_arp** | **bool** |  | [optional] 
**radius_das_enabled** | **bool** |  | [optional] 
**radius_mac_auth_enabled** | **bool** |  | [optional] 
**radius_macacl_empty_password** | **bool** |  | [optional] 
**radius_macacl_format** | **str** |  | [optional] 
**radiusprofile_id** | **str** |  | [optional] 
**roam_cluster_id** | **int** |  | [optional] 
**rrm_enabled** | **bool** |  | [optional] 
**sae_anti_clogging** | **int** |  | [optional] 
**sae_groups** | **List[int]** |  | [optional] 
**sae_psk** | [**List[WLANSaePsk]**](WLANSaePsk.md) |  | [optional] 
**sae_psk_vlan_required** | **bool** |  | [optional] 
**sae_sync** | **int** |  | [optional] 
**schedule** | **List[str]** |  | [optional] 
**schedule_enabled** | **bool** |  | [optional] 
**schedule_reversed** | **bool** |  | [optional] 
**schedule_with_duration** | [**List[WLANScheduleWithDuration]**](WLANScheduleWithDuration.md) |  | [optional] 
**security** | **str** |  | [optional] 
**setting_preference** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**tdls_prohibit** | **bool** |  | [optional] 
**uapsd_enabled** | **bool** |  | [optional] 
**uid_workspace_url** | **str** |  | [optional] 
**usergroup_id** | **str** |  | [optional] 
**vlan** | **int** |  | [optional] 
**vlan_enabled** | **bool** |  | [optional] 
**wep_idx** | **int** |  | [optional] 
**wlan_band** | **str** |  | [optional] 
**wlan_bands** | **List[str]** |  | [optional] 
**wlangroup_id** | **str** |  | [optional] 
**wpa_enc** | **str** |  | [optional] 
**wpa_mode** | **str** |  | [optional] 
**wpa_psk_radius** | **str** |  | [optional] 
**wpa3_enhanced_192** | **bool** |  | [optional] 
**wpa3_fast_roaming** | **bool** |  | [optional] 
**wpa3_support** | **bool** |  | [optional] 
**wpa3_transition** | **bool** |  | [optional] 
**x_iapp_key** | **str** |  | [optional] 
**x_passphrase** | **str** |  | [optional] 
**x_wep** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.wlan_update_request import WLANUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WLANUpdateRequest from a JSON string
wlan_update_request_instance = WLANUpdateRequest.from_json(json)
# print the JSON string representation of the object
print WLANUpdateRequest.to_json()

# convert the object into a dict
wlan_update_request_dict = wlan_update_request_instance.to_dict()
# create an instance of WLANUpdateRequest from a dict
wlan_update_request_form_dict = wlan_update_request.from_dict(wlan_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


