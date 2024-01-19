# DynamicDNSUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**custom_service** | **str** |  | [optional] 
**host_name** | **str** |  | [optional] 
**interface** | **str** |  | [optional] 
**login** | **str** |  | [optional] 
**options** | **List[str]** |  | [optional] 
**server** | **str** |  | [optional] 
**service** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**x_password** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.dynamic_dns_update_request import DynamicDNSUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicDNSUpdateRequest from a JSON string
dynamic_dns_update_request_instance = DynamicDNSUpdateRequest.from_json(json)
# print the JSON string representation of the object
print DynamicDNSUpdateRequest.to_json()

# convert the object into a dict
dynamic_dns_update_request_dict = dynamic_dns_update_request_instance.to_dict()
# create an instance of DynamicDNSUpdateRequest from a dict
dynamic_dns_update_request_form_dict = dynamic_dns_update_request.from_dict(dynamic_dns_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


