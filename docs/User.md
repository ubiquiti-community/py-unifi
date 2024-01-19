# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**blocked** | **bool** |  | [optional] 
**dev_id_override** | **int** |  | [optional] 
**fixed_ap_enabled** | **bool** |  | [optional] 
**fixed_ap_mac** | **str** |  | [optional] 
**fixed_ip** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**last_seen** | **int** |  | [optional] 
**local_dns_record** | **str** |  | [optional] 
**local_dns_record_enabled** | **bool** |  | [optional] 
**mac** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**network_id** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**use_fixedip** | **bool** |  | [optional] 
**usergroup_id** | **str** |  | [optional] 
**virtual_network_override_enabled** | **bool** |  | [optional] 
**virtual_network_override_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print User.to_json()

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


