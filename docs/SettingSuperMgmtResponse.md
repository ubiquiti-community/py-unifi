# SettingSuperMgmtResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingSuperMgmt]**](SettingSuperMgmt.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.setting_super_mgmt_response import SettingSuperMgmtResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingSuperMgmtResponse from a JSON string
setting_super_mgmt_response_instance = SettingSuperMgmtResponse.from_json(json)
# print the JSON string representation of the object
print SettingSuperMgmtResponse.to_json()

# convert the object into a dict
setting_super_mgmt_response_dict = setting_super_mgmt_response_instance.to_dict()
# create an instance of SettingSuperMgmtResponse from a dict
setting_super_mgmt_response_form_dict = setting_super_mgmt_response.from_dict(setting_super_mgmt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


