# SettingIpsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingIps]**](SettingIps.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.setting_ips_response import SettingIpsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingIpsResponse from a JSON string
setting_ips_response_instance = SettingIpsResponse.from_json(json)
# print the JSON string representation of the object
print SettingIpsResponse.to_json()

# convert the object into a dict
setting_ips_response_dict = setting_ips_response_instance.to_dict()
# create an instance of SettingIpsResponse from a dict
setting_ips_response_form_dict = setting_ips_response.from_dict(setting_ips_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


