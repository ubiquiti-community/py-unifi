# SettingBaresipResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingBaresip]**](SettingBaresip.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.setting_baresip_response import SettingBaresipResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingBaresipResponse from a JSON string
setting_baresip_response_instance = SettingBaresipResponse.from_json(json)
# print the JSON string representation of the object
print SettingBaresipResponse.to_json()

# convert the object into a dict
setting_baresip_response_dict = setting_baresip_response_instance.to_dict()
# create an instance of SettingBaresipResponse from a dict
setting_baresip_response_form_dict = setting_baresip_response.from_dict(setting_baresip_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


