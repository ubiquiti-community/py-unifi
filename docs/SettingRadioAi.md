# SettingRadioAi


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**auto_adjust_channels_to_country** | **bool** |  | [optional] 
**channels_na** | **List[int]** |  | [optional] 
**channels_ng** | **List[int]** |  | [optional] 
**cron_expr** | **str** |  | [optional] 
**default** | **bool** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**exclude_devices** | **List[str]** |  | [optional] 
**ht_modes_na** | **List[int]** |  | [optional] 
**ht_modes_ng** | **List[int]** |  | [optional] 
**key** | **str** |  | [optional] 
**optimize** | **List[str]** |  | [optional] 
**radios** | **List[str]** |  | [optional] 
**setting_preference** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**use_xy** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.setting_radio_ai import SettingRadioAi

# TODO update the JSON string below
json = "{}"
# create an instance of SettingRadioAi from a JSON string
setting_radio_ai_instance = SettingRadioAi.from_json(json)
# print the JSON string representation of the object
print SettingRadioAi.to_json()

# convert the object into a dict
setting_radio_ai_dict = setting_radio_ai_instance.to_dict()
# create an instance of SettingRadioAi from a dict
setting_radio_ai_form_dict = setting_radio_ai.from_dict(setting_radio_ai_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


