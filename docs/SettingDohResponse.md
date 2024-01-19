# SettingDohResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingDoh]**](SettingDoh.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.setting_doh_response import SettingDohResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingDohResponse from a JSON string
setting_doh_response_instance = SettingDohResponse.from_json(json)
# print the JSON string representation of the object
print SettingDohResponse.to_json()

# convert the object into a dict
setting_doh_response_dict = setting_doh_response_instance.to_dict()
# create an instance of SettingDohResponse from a dict
setting_doh_response_form_dict = setting_doh_response.from_dict(setting_doh_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


