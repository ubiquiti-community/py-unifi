# SettingEtherLightingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingEtherLighting]**](SettingEtherLighting.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.setting_ether_lighting_response import SettingEtherLightingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingEtherLightingResponse from a JSON string
setting_ether_lighting_response_instance = SettingEtherLightingResponse.from_json(json)
# print the JSON string representation of the object
print SettingEtherLightingResponse.to_json()

# convert the object into a dict
setting_ether_lighting_response_dict = setting_ether_lighting_response_instance.to_dict()
# create an instance of SettingEtherLightingResponse from a dict
setting_ether_lighting_response_form_dict = setting_ether_lighting_response.from_dict(setting_ether_lighting_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


