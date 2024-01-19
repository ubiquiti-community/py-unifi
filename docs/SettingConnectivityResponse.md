# SettingConnectivityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingConnectivity]**](SettingConnectivity.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from unifi_client.models.setting_connectivity_response import SettingConnectivityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingConnectivityResponse from a JSON string
setting_connectivity_response_instance = SettingConnectivityResponse.from_json(json)
# print the JSON string representation of the object
print SettingConnectivityResponse.to_json()

# convert the object into a dict
setting_connectivity_response_dict = setting_connectivity_response_instance.to_dict()
# create an instance of SettingConnectivityResponse from a dict
setting_connectivity_response_form_dict = setting_connectivity_response.from_dict(setting_connectivity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


