# SettingElementAdoptResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingElementAdopt]**](SettingElementAdopt.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from unifi_client.models.setting_element_adopt_response import SettingElementAdoptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingElementAdoptResponse from a JSON string
setting_element_adopt_response_instance = SettingElementAdoptResponse.from_json(json)
# print the JSON string representation of the object
print SettingElementAdoptResponse.to_json()

# convert the object into a dict
setting_element_adopt_response_dict = setting_element_adopt_response_instance.to_dict()
# create an instance of SettingElementAdoptResponse from a dict
setting_element_adopt_response_form_dict = setting_element_adopt_response.from_dict(setting_element_adopt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


