# SettingMgmtResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingMgmt]**](SettingMgmt.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.setting_mgmt_response import SettingMgmtResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingMgmtResponse from a JSON string
setting_mgmt_response_instance = SettingMgmtResponse.from_json(json)
# print the JSON string representation of the object
print SettingMgmtResponse.to_json()

# convert the object into a dict
setting_mgmt_response_dict = setting_mgmt_response_instance.to_dict()
# create an instance of SettingMgmtResponse from a dict
setting_mgmt_response_form_dict = setting_mgmt_response.from_dict(setting_mgmt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


