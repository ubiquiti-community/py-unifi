# SettingRadioAiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingRadioAi]**](SettingRadioAi.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.setting_radio_ai_response import SettingRadioAiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingRadioAiResponse from a JSON string
setting_radio_ai_response_instance = SettingRadioAiResponse.from_json(json)
# print the JSON string representation of the object
print SettingRadioAiResponse.to_json()

# convert the object into a dict
setting_radio_ai_response_dict = setting_radio_ai_response_instance.to_dict()
# create an instance of SettingRadioAiResponse from a dict
setting_radio_ai_response_form_dict = setting_radio_ai_response.from_dict(setting_radio_ai_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


