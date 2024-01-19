# GetSettingAutoSpeedtestDefaultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetSettingAutoSpeedtestDefaultResponseDataInner]**](GetSettingAutoSpeedtestDefaultResponseDataInner.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_setting_auto_speedtest_default_response import GetSettingAutoSpeedtestDefaultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSettingAutoSpeedtestDefaultResponse from a JSON string
get_setting_auto_speedtest_default_response_instance = GetSettingAutoSpeedtestDefaultResponse.from_json(json)
# print the JSON string representation of the object
print GetSettingAutoSpeedtestDefaultResponse.to_json()

# convert the object into a dict
get_setting_auto_speedtest_default_response_dict = get_setting_auto_speedtest_default_response_instance.to_dict()
# create an instance of GetSettingAutoSpeedtestDefaultResponse from a dict
get_setting_auto_speedtest_default_response_form_dict = get_setting_auto_speedtest_default_response.from_dict(get_setting_auto_speedtest_default_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


