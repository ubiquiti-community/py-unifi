# SettingAutoSpeedtest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**cron_expr** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.setting_auto_speedtest import SettingAutoSpeedtest

# TODO update the JSON string below
json = "{}"
# create an instance of SettingAutoSpeedtest from a JSON string
setting_auto_speedtest_instance = SettingAutoSpeedtest.from_json(json)
# print the JSON string representation of the object
print SettingAutoSpeedtest.to_json()

# convert the object into a dict
setting_auto_speedtest_dict = setting_auto_speedtest_instance.to_dict()
# create an instance of SettingAutoSpeedtest from a dict
setting_auto_speedtest_form_dict = setting_auto_speedtest.from_dict(setting_auto_speedtest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


