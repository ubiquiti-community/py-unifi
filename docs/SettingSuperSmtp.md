# SettingSuperSmtp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**host** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**sender** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**use_auth** | **bool** |  | [optional] 
**use_sender** | **bool** |  | [optional] 
**use_ssl** | **bool** |  | [optional] 
**username** | **str** |  | [optional] 
**x_password** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.setting_super_smtp import SettingSuperSmtp

# TODO update the JSON string below
json = "{}"
# create an instance of SettingSuperSmtp from a JSON string
setting_super_smtp_instance = SettingSuperSmtp.from_json(json)
# print the JSON string representation of the object
print SettingSuperSmtp.to_json()

# convert the object into a dict
setting_super_smtp_dict = setting_super_smtp_instance.to_dict()
# create an instance of SettingSuperSmtp from a dict
setting_super_smtp_form_dict = setting_super_smtp.from_dict(setting_super_smtp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


