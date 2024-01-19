# SettingTeleportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingTeleport]**](SettingTeleport.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.setting_teleport_response import SettingTeleportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingTeleportResponse from a JSON string
setting_teleport_response_instance = SettingTeleportResponse.from_json(json)
# print the JSON string representation of the object
print SettingTeleportResponse.to_json()

# convert the object into a dict
setting_teleport_response_dict = setting_teleport_response_instance.to_dict()
# create an instance of SettingTeleportResponse from a dict
setting_teleport_response_form_dict = setting_teleport_response.from_dict(setting_teleport_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


