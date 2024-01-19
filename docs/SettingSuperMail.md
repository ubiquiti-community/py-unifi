# SettingSuperMail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.setting_super_mail import SettingSuperMail

# TODO update the JSON string below
json = "{}"
# create an instance of SettingSuperMail from a JSON string
setting_super_mail_instance = SettingSuperMail.from_json(json)
# print the JSON string representation of the object
print SettingSuperMail.to_json()

# convert the object into a dict
setting_super_mail_dict = setting_super_mail_instance.to_dict()
# create an instance of SettingSuperMail from a dict
setting_super_mail_form_dict = setting_super_mail.from_dict(setting_super_mail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


