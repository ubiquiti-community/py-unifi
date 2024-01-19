# SettingSnmpResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SettingSnmp]**](SettingSnmp.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.setting_snmp_response import SettingSnmpResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingSnmpResponse from a JSON string
setting_snmp_response_instance = SettingSnmpResponse.from_json(json)
# print the JSON string representation of the object
print SettingSnmpResponse.to_json()

# convert the object into a dict
setting_snmp_response_dict = setting_snmp_response_instance.to_dict()
# create an instance of SettingSnmpResponse from a dict
setting_snmp_response_form_dict = setting_snmp_response.from_dict(setting_snmp_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


