# SettingUsg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**arp_cache_base_reachable** | **int** |  | [optional] 
**arp_cache_timeout** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**broadcast_ping** | **bool** |  | [optional] 
**dhcp_relay_agents_packets** | **str** |  | [optional] 
**dhcp_relay_hop_count** | **int** |  | [optional] 
**dhcp_relay_max_size** | **int** |  | [optional] 
**dhcp_relay_port** | **int** |  | [optional] 
**dhcp_relay_server_1** | **str** |  | [optional] 
**dhcp_relay_server_2** | **str** |  | [optional] 
**dhcp_relay_server_3** | **str** |  | [optional] 
**dhcp_relay_server_4** | **str** |  | [optional] 
**dhcp_relay_server_5** | **str** |  | [optional] 
**dhcpd_hostfile_update** | **bool** |  | [optional] 
**dhcpd_use_dnsmasq** | **bool** |  | [optional] 
**dnsmasq_all_servers** | **bool** |  | [optional] 
**echo_server** | **str** |  | [optional] 
**firewall_guest_default_log** | **bool** |  | [optional] 
**firewall_lan_default_log** | **bool** |  | [optional] 
**firewall_wan_default_log** | **bool** |  | [optional] 
**ftp_module** | **bool** |  | [optional] 
**geo_ip_filtering_block** | **str** |  | [optional] 
**geo_ip_filtering_countries** | **str** |  | [optional] 
**geo_ip_filtering_enabled** | **bool** |  | [optional] 
**geo_ip_filtering_traffic_direction** | **str** |  | [optional] 
**gre_module** | **bool** |  | [optional] 
**h323_module** | **bool** |  | [optional] 
**icmp_timeout** | **int** |  | [optional] 
**key** | **str** |  | [optional] 
**lldp_enable_all** | **bool** |  | [optional] 
**mdns_enabled** | **bool** |  | [optional] 
**mss_clamp** | **str** |  | [optional] 
**mss_clamp_mss** | **int** |  | [optional] 
**offload_accounting** | **bool** |  | [optional] 
**offload_l2_blocking** | **bool** |  | [optional] 
**offload_sch** | **bool** |  | [optional] 
**other_timeout** | **int** |  | [optional] 
**pptp_module** | **bool** |  | [optional] 
**receive_redirects** | **bool** |  | [optional] 
**send_redirects** | **bool** |  | [optional] 
**sip_module** | **bool** |  | [optional] 
**site_id** | **str** |  | [optional] 
**syn_cookies** | **bool** |  | [optional] 
**tcp_close_timeout** | **int** |  | [optional] 
**tcp_close_wait_timeout** | **int** |  | [optional] 
**tcp_established_timeout** | **int** |  | [optional] 
**tcp_fin_wait_timeout** | **int** |  | [optional] 
**tcp_last_ack_timeout** | **int** |  | [optional] 
**tcp_syn_recv_timeout** | **int** |  | [optional] 
**tcp_syn_sent_timeout** | **int** |  | [optional] 
**tcp_time_wait_timeout** | **int** |  | [optional] 
**tftp_module** | **bool** |  | [optional] 
**timeout_setting_preference** | **str** |  | [optional] 
**udp_other_timeout** | **int** |  | [optional] 
**udp_stream_timeout** | **int** |  | [optional] 
**upnp_enabled** | **bool** |  | [optional] 
**upnp_nat_pmp_enabled** | **bool** |  | [optional] 
**upnp_secure_mode** | **bool** |  | [optional] 
**upnp_wan_interface** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.setting_usg import SettingUsg

# TODO update the JSON string below
json = "{}"
# create an instance of SettingUsg from a JSON string
setting_usg_instance = SettingUsg.from_json(json)
# print the JSON string representation of the object
print SettingUsg.to_json()

# convert the object into a dict
setting_usg_dict = setting_usg_instance.to_dict()
# create an instance of SettingUsg from a dict
setting_usg_form_dict = setting_usg.from_dict(setting_usg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


