# RoutingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Routing]**](Routing.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.routing_response import RoutingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingResponse from a JSON string
routing_response_instance = RoutingResponse.from_json(json)
# print the JSON string representation of the object
print RoutingResponse.to_json()

# convert the object into a dict
routing_response_dict = routing_response_instance.to_dict()
# create an instance of RoutingResponse from a dict
routing_response_form_dict = routing_response.from_dict(routing_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


