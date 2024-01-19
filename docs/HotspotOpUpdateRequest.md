# HotspotOpUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**x_password** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.hotspot_op_update_request import HotspotOpUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HotspotOpUpdateRequest from a JSON string
hotspot_op_update_request_instance = HotspotOpUpdateRequest.from_json(json)
# print the JSON string representation of the object
print HotspotOpUpdateRequest.to_json()

# convert the object into a dict
hotspot_op_update_request_dict = hotspot_op_update_request_instance.to_dict()
# create an instance of HotspotOpUpdateRequest from a dict
hotspot_op_update_request_form_dict = hotspot_op_update_request.from_dict(hotspot_op_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


