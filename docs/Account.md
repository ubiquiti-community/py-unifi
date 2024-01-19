# Account


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**ip** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**networkconf_id** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**tunnel_config_type** | **str** |  | [optional] 
**tunnel_medium_type** | **int** |  | [optional] 
**tunnel_type** | **int** |  | [optional] 
**vlan** | **int** |  | [optional] 
**x_password** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print Account.to_json()

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_form_dict = account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


