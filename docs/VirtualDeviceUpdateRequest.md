# VirtualDeviceUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**height_in_meters** | **float** |  | [optional] 
**locked** | **bool** |  | [optional] 
**map_id** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**x** | **str** |  | [optional] 
**y** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.virtual_device_update_request import VirtualDeviceUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDeviceUpdateRequest from a JSON string
virtual_device_update_request_instance = VirtualDeviceUpdateRequest.from_json(json)
# print the JSON string representation of the object
print VirtualDeviceUpdateRequest.to_json()

# convert the object into a dict
virtual_device_update_request_dict = virtual_device_update_request_instance.to_dict()
# create an instance of VirtualDeviceUpdateRequest from a dict
virtual_device_update_request_form_dict = virtual_device_update_request.from_dict(virtual_device_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


