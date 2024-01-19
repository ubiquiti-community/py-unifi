# SettingDoh


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**server_names** | **List[str]** |  | [optional] 
**site_id** | **str** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.setting_doh import SettingDoh

# TODO update the JSON string below
json = "{}"
# create an instance of SettingDoh from a JSON string
setting_doh_instance = SettingDoh.from_json(json)
# print the JSON string representation of the object
print SettingDoh.to_json()

# convert the object into a dict
setting_doh_dict = setting_doh_instance.to_dict()
# create an instance of SettingDoh from a dict
setting_doh_form_dict = setting_doh.from_dict(setting_doh_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


