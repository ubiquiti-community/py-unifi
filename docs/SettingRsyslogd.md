# SettingRsyslogd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**debug** | **bool** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**ip** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**netconsole_enabled** | **bool** |  | [optional] 
**netconsole_host** | **str** |  | [optional] 
**netconsole_port** | **int** |  | [optional] 
**port** | **int** |  | [optional] 
**site_id** | **str** |  | [optional] 
**this_controller** | **bool** |  | [optional] 
**this_controller_encrypted_only** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.setting_rsyslogd import SettingRsyslogd

# TODO update the JSON string below
json = "{}"
# create an instance of SettingRsyslogd from a JSON string
setting_rsyslogd_instance = SettingRsyslogd.from_json(json)
# print the JSON string representation of the object
print SettingRsyslogd.to_json()

# convert the object into a dict
setting_rsyslogd_dict = setting_rsyslogd_instance.to_dict()
# create an instance of SettingRsyslogd from a dict
setting_rsyslogd_form_dict = setting_rsyslogd.from_dict(setting_rsyslogd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


