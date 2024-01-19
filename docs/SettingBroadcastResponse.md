# SettingBroadcastResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingBroadcast]**](SettingBroadcast.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.setting_broadcast_response import SettingBroadcastResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingBroadcastResponse from a JSON string
setting_broadcast_response_instance = SettingBroadcastResponse.from_json(json)
# print the JSON string representation of the object
print SettingBroadcastResponse.to_json()

# convert the object into a dict
setting_broadcast_response_dict = setting_broadcast_response_instance.to_dict()
# create an instance of SettingBroadcastResponse from a dict
setting_broadcast_response_form_dict = setting_broadcast_response.from_dict(setting_broadcast_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


