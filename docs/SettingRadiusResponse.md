# SettingRadiusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingRadius]**](SettingRadius.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.setting_radius_response import SettingRadiusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingRadiusResponse from a JSON string
setting_radius_response_instance = SettingRadiusResponse.from_json(json)
# print the JSON string representation of the object
print SettingRadiusResponse.to_json()

# convert the object into a dict
setting_radius_response_dict = setting_radius_response_instance.to_dict()
# create an instance of SettingRadiusResponse from a dict
setting_radius_response_form_dict = setting_radius_response.from_dict(setting_radius_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


