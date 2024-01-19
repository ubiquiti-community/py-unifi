# SettingSuperFwupdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingSuperFwupdate]**](SettingSuperFwupdate.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.setting_super_fwupdate_response import SettingSuperFwupdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingSuperFwupdateResponse from a JSON string
setting_super_fwupdate_response_instance = SettingSuperFwupdateResponse.from_json(json)
# print the JSON string representation of the object
print SettingSuperFwupdateResponse.to_json()

# convert the object into a dict
setting_super_fwupdate_response_dict = setting_super_fwupdate_response_instance.to_dict()
# create an instance of SettingSuperFwupdateResponse from a dict
setting_super_fwupdate_response_form_dict = setting_super_fwupdate_response.from_dict(setting_super_fwupdate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


