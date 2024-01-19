# DHCPOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**signed** | **bool** |  | [optional] 
**site_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**width** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.dhcp_option import DHCPOption

# TODO update the JSON string below
json = "{}"
# create an instance of DHCPOption from a JSON string
dhcp_option_instance = DHCPOption.from_json(json)
# print the JSON string representation of the object
print DHCPOption.to_json()

# convert the object into a dict
dhcp_option_dict = dhcp_option_instance.to_dict()
# create an instance of DHCPOption from a dict
dhcp_option_form_dict = dhcp_option.from_dict(dhcp_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


