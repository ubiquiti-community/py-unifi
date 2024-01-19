# SettingUswResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingUsw]**](SettingUsw.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.setting_usw_response import SettingUswResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingUswResponse from a JSON string
setting_usw_response_instance = SettingUswResponse.from_json(json)
# print the JSON string representation of the object
print SettingUswResponse.to_json()

# convert the object into a dict
setting_usw_response_dict = setting_usw_response_instance.to_dict()
# create an instance of SettingUswResponse from a dict
setting_usw_response_form_dict = setting_usw_response.from_dict(setting_usw_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


