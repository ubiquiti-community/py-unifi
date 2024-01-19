# SettingAutoSpeedtestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingAutoSpeedtest]**](SettingAutoSpeedtest.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.setting_auto_speedtest_response import SettingAutoSpeedtestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingAutoSpeedtestResponse from a JSON string
setting_auto_speedtest_response_instance = SettingAutoSpeedtestResponse.from_json(json)
# print the JSON string representation of the object
print SettingAutoSpeedtestResponse.to_json()

# convert the object into a dict
setting_auto_speedtest_response_dict = setting_auto_speedtest_response_instance.to_dict()
# create an instance of SettingAutoSpeedtestResponse from a dict
setting_auto_speedtest_response_form_dict = setting_auto_speedtest_response.from_dict(setting_auto_speedtest_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


