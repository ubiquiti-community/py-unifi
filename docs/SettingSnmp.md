# SettingSnmp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**community** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**enabled_v3** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**x_password** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.setting_snmp import SettingSnmp

# TODO update the JSON string below
json = "{}"
# create an instance of SettingSnmp from a JSON string
setting_snmp_instance = SettingSnmp.from_json(json)
# print the JSON string representation of the object
print SettingSnmp.to_json()

# convert the object into a dict
setting_snmp_dict = setting_snmp_instance.to_dict()
# create an instance of SettingSnmp from a dict
setting_snmp_form_dict = setting_snmp.from_dict(setting_snmp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


