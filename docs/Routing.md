# Routing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**gateway_device** | **str** |  | [optional] 
**gateway_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**static_route_distance** | **int** |  | [optional] 
**static_route_interface** | **str** |  | [optional] 
**static_route_network** | **str** |  | [optional] 
**static_route_nexthop** | **str** |  | [optional] 
**static_route_type** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.routing import Routing

# TODO update the JSON string below
json = "{}"
# create an instance of Routing from a JSON string
routing_instance = Routing.from_json(json)
# print the JSON string representation of the object
print Routing.to_json()

# convert the object into a dict
routing_dict = routing_instance.to_dict()
# create an instance of Routing from a dict
routing_form_dict = routing.from_dict(routing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


