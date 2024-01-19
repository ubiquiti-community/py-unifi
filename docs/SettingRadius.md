# SettingRadius


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**accounting_enabled** | **bool** |  | [optional] 
**acct_port** | **int** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**auth_port** | **int** |  | [optional] 
**configure_whole_network** | **bool** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**interim_update_interval** | **int** |  | [optional] 
**key** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**tunneled_reply** | **bool** |  | [optional] 
**x_secret** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.setting_radius import SettingRadius

# TODO update the JSON string below
json = "{}"
# create an instance of SettingRadius from a JSON string
setting_radius_instance = SettingRadius.from_json(json)
# print the JSON string representation of the object
print SettingRadius.to_json()

# convert the object into a dict
setting_radius_dict = setting_radius_instance.to_dict()
# create an instance of SettingRadius from a dict
setting_radius_form_dict = setting_radius.from_dict(setting_radius_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


