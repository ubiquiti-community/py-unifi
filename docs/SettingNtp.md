# SettingNtp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**ntp_server_1** | **str** |  | [optional] 
**ntp_server_2** | **str** |  | [optional] 
**ntp_server_3** | **str** |  | [optional] 
**ntp_server_4** | **str** |  | [optional] 
**setting_preference** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.setting_ntp import SettingNtp

# TODO update the JSON string below
json = "{}"
# create an instance of SettingNtp from a JSON string
setting_ntp_instance = SettingNtp.from_json(json)
# print the JSON string representation of the object
print SettingNtp.to_json()

# convert the object into a dict
setting_ntp_dict = setting_ntp_instance.to_dict()
# create an instance of SettingNtp from a dict
setting_ntp_form_dict = setting_ntp.from_dict(setting_ntp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


