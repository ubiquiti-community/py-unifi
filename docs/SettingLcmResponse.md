# SettingLcmResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingLcm]**](SettingLcm.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from unifi_client.models.setting_lcm_response import SettingLcmResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingLcmResponse from a JSON string
setting_lcm_response_instance = SettingLcmResponse.from_json(json)
# print the JSON string representation of the object
print SettingLcmResponse.to_json()

# convert the object into a dict
setting_lcm_response_dict = setting_lcm_response_instance.to_dict()
# create an instance of SettingLcmResponse from a dict
setting_lcm_response_form_dict = setting_lcm_response.from_dict(setting_lcm_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


