# Device


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**adopted** | **bool** |  | [optional] 
**atf_enabled** | **bool** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**bandsteering_mode** | **str** |  | [optional] 
**baresip_auth_user** | **str** |  | [optional] 
**baresip_enabled** | **bool** |  | [optional] 
**baresip_extension** | **str** |  | [optional] 
**config_network** | [**DeviceConfigNetwork**](DeviceConfigNetwork.md) |  | [optional] 
**connected_battery_overrides** | [**List[DeviceConnectedBatteryOverrides]**](DeviceConnectedBatteryOverrides.md) |  | [optional] 
**disabled** | **bool** |  | [optional] 
**dot1x_fallback_networkconf_id** | **str** |  | [optional] 
**dot1x_portctrl_enabled** | **bool** |  | [optional] 
**dpi_enabled** | **bool** |  | [optional] 
**ether_lighting** | [**DeviceEtherLighting**](DeviceEtherLighting.md) |  | [optional] 
**ethernet_overrides** | [**List[DeviceEthernetOverrides]**](DeviceEthernetOverrides.md) |  | [optional] 
**flowctrl_enabled** | **bool** |  | [optional] 
**gateway_vrrp_mode** | **str** |  | [optional] 
**gateway_vrrp_priority** | **int** |  | [optional] 
**height_in_meters** | **float** |  | [optional] 
**hostname** | **str** |  | [optional] 
**jumboframe_enabled** | **bool** |  | [optional] 
**lcm_brightness** | **int** |  | [optional] 
**lcm_brightness_override** | **bool** |  | [optional] 
**lcm_idle_timeout** | **int** |  | [optional] 
**lcm_idle_timeout_override** | **bool** |  | [optional] 
**lcm_night_mode_begins** | **str** |  | [optional] 
**lcm_night_mode_ends** | **str** |  | [optional] 
**lcm_settings_restricted_access** | **bool** |  | [optional] 
**lcm_tracker_enabled** | **bool** |  | [optional] 
**lcm_tracker_seed** | **str** |  | [optional] 
**led_override** | **str** |  | [optional] 
**led_override_color** | **str** |  | [optional] 
**led_override_color_brightness** | **int** |  | [optional] 
**locked** | **bool** |  | [optional] 
**lowpfmode_override** | **bool** |  | [optional] 
**lte_apn** | **str** |  | [optional] 
**lte_auth_type** | **str** |  | [optional] 
**lte_data_limit_enabled** | **bool** |  | [optional] 
**lte_data_warning_enabled** | **bool** |  | [optional] 
**lte_ext_ant** | **bool** |  | [optional] 
**lte_hard_limit** | **int** |  | [optional] 
**lte_password** | **str** |  | [optional] 
**lte_poe** | **bool** |  | [optional] 
**lte_roaming_allowed** | **bool** |  | [optional] 
**lte_sim_pin** | **int** |  | [optional] 
**lte_soft_limit** | **int** |  | [optional] 
**lte_username** | **str** |  | [optional] 
**mac** | **str** |  | [optional] 
**map_id** | **str** |  | [optional] 
**mesh_sta_vap_enabled** | **bool** |  | [optional] 
**mgmt_network_id** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**outdoor_mode_override** | **str** |  | [optional] 
**outlet_enabled** | **bool** |  | [optional] 
**outlet_overrides** | [**List[DeviceOutletOverrides]**](DeviceOutletOverrides.md) |  | [optional] 
**outlet_power_cycle_enabled** | **bool** |  | [optional] 
**port_overrides** | [**List[DevicePortOverrides]**](DevicePortOverrides.md) |  | [optional] 
**power_source_ctrl** | **str** |  | [optional] 
**power_source_ctrl_budget** | **int** |  | [optional] 
**power_source_ctrl_enabled** | **bool** |  | [optional] 
**radio_table** | [**List[DeviceRadioTable]**](DeviceRadioTable.md) |  | [optional] 
**radiusprofile_id** | **str** |  | [optional] 
**resetbtn_enabled** | **str** |  | [optional] 
**rps_override** | [**DeviceRpsOverride**](DeviceRpsOverride.md) |  | [optional] 
**site_id** | **str** |  | [optional] 
**snmp_contact** | **str** |  | [optional] 
**snmp_location** | **str** |  | [optional] 
**state** | **int** |  | [optional] 
**stp_priority** | **str** |  | [optional] 
**stp_version** | **str** |  | [optional] 
**switch_vlan_enabled** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**ubb_pair_name** | **str** |  | [optional] 
**volume** | **int** |  | [optional] 
**x** | **float** |  | [optional] 
**x_baresip_password** | **str** |  | [optional] 
**y** | **float** |  | [optional] 

## Example

```python
from unifi_client.models.device import Device

# TODO update the JSON string below
json = "{}"
# create an instance of Device from a JSON string
device_instance = Device.from_json(json)
# print the JSON string representation of the object
print Device.to_json()

# convert the object into a dict
device_dict = device_instance.to_dict()
# create an instance of Device from a dict
device_form_dict = device.from_dict(device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


