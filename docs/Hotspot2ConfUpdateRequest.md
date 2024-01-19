# Hotspot2ConfUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**anqp_domain_id** | **int** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**capab** | [**List[Hotspot2ConfCapab]**](Hotspot2ConfCapab.md) |  | [optional] 
**cellular_network_list** | [**List[Hotspot2ConfCellularNetworkList]**](Hotspot2ConfCellularNetworkList.md) |  | [optional] 
**deauth_req_timeout** | **int** |  | [optional] 
**disable_dgaf** | **bool** |  | [optional] 
**domain_name_list** | **List[str]** |  | [optional] 
**friendly_name** | [**List[Hotspot2ConfFriendlyName]**](Hotspot2ConfFriendlyName.md) |  | [optional] 
**gas_advanced** | **bool** |  | [optional] 
**gas_comeback_delay** | **int** |  | [optional] 
**gas_frag_limit** | **int** |  | [optional] 
**hessid** | **str** |  | [optional] 
**hessid_used** | **bool** |  | [optional] 
**icons** | [**List[Hotspot2ConfIcons]**](Hotspot2ConfIcons.md) |  | [optional] 
**ipaddr_type_avail_v4** | **int** |  | [optional] 
**ipaddr_type_avail_v6** | **int** |  | [optional] 
**metrics_downlink_load** | **int** |  | [optional] 
**metrics_downlink_load_set** | **bool** |  | [optional] 
**metrics_downlink_speed** | **int** |  | [optional] 
**metrics_downlink_speed_set** | **bool** |  | [optional] 
**metrics_info_at_capacity** | **bool** |  | [optional] 
**metrics_info_link_status** | **str** |  | [optional] 
**metrics_info_symmetric** | **bool** |  | [optional] 
**metrics_measurement** | **int** |  | [optional] 
**metrics_measurement_set** | **bool** |  | [optional] 
**metrics_status** | **bool** |  | [optional] 
**metrics_uplink_load** | **int** |  | [optional] 
**metrics_uplink_load_set** | **bool** |  | [optional] 
**metrics_uplink_speed** | **int** |  | [optional] 
**metrics_uplink_speed_set** | **bool** |  | [optional] 
**nai_realm_list** | [**List[Hotspot2ConfNaiRealmList]**](Hotspot2ConfNaiRealmList.md) |  | [optional] 
**name** | **str** |  | [optional] 
**network_access_asra** | **bool** |  | [optional] 
**network_access_esr** | **bool** |  | [optional] 
**network_access_internet** | **bool** |  | [optional] 
**network_access_uesa** | **bool** |  | [optional] 
**network_auth_type** | **int** |  | [optional] 
**network_auth_url** | **str** |  | [optional] 
**network_type** | **int** |  | [optional] 
**osu** | [**List[Hotspot2ConfOsu]**](Hotspot2ConfOsu.md) |  | [optional] 
**osu_ssid** | **str** |  | [optional] 
**qos_map_dcsp** | [**List[Hotspot2ConfQOSMapDcsp]**](Hotspot2ConfQOSMapDcsp.md) |  | [optional] 
**qos_map_exceptions** | [**List[Hotspot2ConfQOSMapExceptions]**](Hotspot2ConfQOSMapExceptions.md) |  | [optional] 
**qos_map_status** | **bool** |  | [optional] 
**roaming_consortium_list** | [**List[Hotspot2ConfRoamingConsortiumList]**](Hotspot2ConfRoamingConsortiumList.md) |  | [optional] 
**save_timestamp** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**t_c_filename** | **str** |  | [optional] 
**t_c_timestamp** | **int** |  | [optional] 
**venue_group** | **int** |  | [optional] 
**venue_name** | [**List[Hotspot2ConfVenueName]**](Hotspot2ConfVenueName.md) |  | [optional] 
**venue_type** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.hotspot2_conf_update_request import Hotspot2ConfUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of Hotspot2ConfUpdateRequest from a JSON string
hotspot2_conf_update_request_instance = Hotspot2ConfUpdateRequest.from_json(json)
# print the JSON string representation of the object
print Hotspot2ConfUpdateRequest.to_json()

# convert the object into a dict
hotspot2_conf_update_request_dict = hotspot2_conf_update_request_instance.to_dict()
# create an instance of Hotspot2ConfUpdateRequest from a dict
hotspot2_conf_update_request_form_dict = hotspot2_conf_update_request.from_dict(hotspot2_conf_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


