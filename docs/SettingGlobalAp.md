# SettingGlobalAp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**var_6e_channel_size** | **int** |  | [optional] 
**var_6e_tx_power** | **int** |  | [optional] 
**var_6e_tx_power_mode** | **str** |  | [optional] 
**ap_exclusions** | **List[str]** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**na_channel_size** | **int** |  | [optional] 
**na_tx_power** | **int** |  | [optional] 
**na_tx_power_mode** | **str** |  | [optional] 
**ng_channel_size** | **int** |  | [optional] 
**ng_tx_power** | **int** |  | [optional] 
**ng_tx_power_mode** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.setting_global_ap import SettingGlobalAp

# TODO update the JSON string below
json = "{}"
# create an instance of SettingGlobalAp from a JSON string
setting_global_ap_instance = SettingGlobalAp.from_json(json)
# print the JSON string representation of the object
print SettingGlobalAp.to_json()

# convert the object into a dict
setting_global_ap_dict = setting_global_ap_instance.to_dict()
# create an instance of SettingGlobalAp from a dict
setting_global_ap_form_dict = setting_global_ap.from_dict(setting_global_ap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


