# PortProfileUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
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
**name** | **str** |  | [optional] 
**native_networkconf_id** | **str** |  | [optional] 
**op_mode** | **str** |  | [optional] 
**poe_mode** | **str** |  | [optional] 
**port_keepalive_enabled** | **bool** |  | [optional] 
**port_security_enabled** | **bool** |  | [optional] 
**port_security_mac_address** | **List[str]** |  | [optional] 
**priority_queue1_level** | **int** |  | [optional] 
**priority_queue2_level** | **int** |  | [optional] 
**priority_queue3_level** | **int** |  | [optional] 
**priority_queue4_level** | **int** |  | [optional] 
**setting_preference** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
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
from openapi_client.models.port_profile_update_request import PortProfileUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PortProfileUpdateRequest from a JSON string
port_profile_update_request_instance = PortProfileUpdateRequest.from_json(json)
# print the JSON string representation of the object
print PortProfileUpdateRequest.to_json()

# convert the object into a dict
port_profile_update_request_dict = port_profile_update_request_instance.to_dict()
# create an instance of PortProfileUpdateRequest from a dict
port_profile_update_request_form_dict = port_profile_update_request.from_dict(port_profile_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


