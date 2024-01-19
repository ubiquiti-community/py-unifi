# PortForward


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**destination_ip** | **str** |  | [optional] 
**dst_port** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**fwd** | **str** |  | [optional] 
**fwd_port** | **str** |  | [optional] 
**log** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**pfwd_interface** | **str** |  | [optional] 
**proto** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**src** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.port_forward import PortForward

# TODO update the JSON string below
json = "{}"
# create an instance of PortForward from a JSON string
port_forward_instance = PortForward.from_json(json)
# print the JSON string representation of the object
print PortForward.to_json()

# convert the object into a dict
port_forward_dict = port_forward_instance.to_dict()
# create an instance of PortForward from a dict
port_forward_form_dict = port_forward.from_dict(port_forward_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


