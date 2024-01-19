# SettingConnectivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**enable_isolated_wlan** | **bool** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**uplink_host** | **str** |  | [optional] 
**uplink_type** | **str** |  | [optional] 
**x_mesh_essid** | **str** |  | [optional] 
**x_mesh_psk** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.setting_connectivity import SettingConnectivity

# TODO update the JSON string below
json = "{}"
# create an instance of SettingConnectivity from a JSON string
setting_connectivity_instance = SettingConnectivity.from_json(json)
# print the JSON string representation of the object
print SettingConnectivity.to_json()

# convert the object into a dict
setting_connectivity_dict = setting_connectivity_instance.to_dict()
# create an instance of SettingConnectivity from a dict
setting_connectivity_form_dict = setting_connectivity.from_dict(setting_connectivity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


