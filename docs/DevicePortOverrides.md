# DevicePortOverrides


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregate_num_ports** | **int** |  | [optional] 
**autoneg** | **bool** |  | [optional] 
**dot1x_ctrl** | **str** |  | [optional] 
**dot1x_idle_timeout** | **int** |  | [optional] 
**egress_rate_limit_kbps** | **int** |  | [optional] 
**egress_rate_limit_kbps_enabled** | **bool** |  | [optional] 
**excluded_networkconf_ids** | **List[str]** |  | [optional] 
**forward** | **str** |  | [optional] 
**full_duplex** | **bool** |  | [optional] 
**isolation** | **bool** |  | [optional] 
**lldpmed_enabled** | **bool** |  | [optional] 
**lldpmed_notify_enabled** | **bool** |  | [optional] 
**mirror_port_idx** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**native_networkconf_id** | **str** |  | [optional] 
**op_mode** | **str** |  | [optional] 
**poe_mode** | **str** |  | [optional] 
**port_idx** | **int** |  | [optional] 
**port_keepalive_enabled** | **bool** |  | [optional] 
**port_security_enabled** | **bool** |  | [optional] 
**port_security_mac_address** | **List[str]** |  | [optional] 
**portconf_id** | **str** |  | [optional] 
**priority_queue1_level** | **int** |  | [optional] 
**priority_queue2_level** | **int** |  | [optional] 
**priority_queue3_level** | **int** |  | [optional] 
**priority_queue4_level** | **int** |  | [optional] 
**setting_preference** | **str** |  | [optional] 
**speed** | **int** |  | [optional] 
**stormctrl_bcast_enabled** | **bool** |  | [optional] 
**stormctrl_bcast_level** | **int** |  | [optional] 
**stormctrl_bcast_rate** | **int** |  | [optional] 
**stormctrl_mcast_enabled** | **bool** |  | [optional] 
**stormctrl_mcast_level** | **int** |  | [optional] 
**stormctrl_mcast_rate** | **int** |  | [optional] 
**stormctrl_type** | **str** |  | [optional] 
**stormctrl_ucast_enabled** | **bool** |  | [optional] 
**stormctrl_ucast_level** | **int** |  | [optional] 
**stormctrl_ucast_rate** | **int** |  | [optional] 
**stp_port_mode** | **bool** |  | [optional] 
**tagged_vlan_mgmt** | **str** |  | [optional] 
**voice_networkconf_id** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.device_port_overrides import DevicePortOverrides

# TODO update the JSON string below
json = "{}"
# create an instance of DevicePortOverrides from a JSON string
device_port_overrides_instance = DevicePortOverrides.from_json(json)
# print the JSON string representation of the object
print DevicePortOverrides.to_json()

# convert the object into a dict
device_port_overrides_dict = device_port_overrides_instance.to_dict()
# create an instance of DevicePortOverrides from a dict
device_port_overrides_form_dict = device_port_overrides.from_dict(device_port_overrides_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


