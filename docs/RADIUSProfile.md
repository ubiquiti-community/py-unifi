# RADIUSProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**accounting_enabled** | **bool** |  | [optional] 
**acct_servers** | [**List[RADIUSProfileAcctServers]**](RADIUSProfileAcctServers.md) |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**auth_servers** | [**List[RADIUSProfileAuthServers]**](RADIUSProfileAuthServers.md) |  | [optional] 
**interim_update_enabled** | **bool** |  | [optional] 
**interim_update_interval** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**use_usg_acct_server** | **bool** |  | [optional] 
**use_usg_auth_server** | **bool** |  | [optional] 
**vlan_enabled** | **bool** |  | [optional] 
**vlan_wlan_mode** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.radius_profile import RADIUSProfile

# TODO update the JSON string below
json = "{}"
# create an instance of RADIUSProfile from a JSON string
radius_profile_instance = RADIUSProfile.from_json(json)
# print the JSON string representation of the object
print RADIUSProfile.to_json()

# convert the object into a dict
radius_profile_dict = radius_profile_instance.to_dict()
# create an instance of RADIUSProfile from a dict
radius_profile_form_dict = radius_profile.from_dict(radius_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


