# PortForwardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PortForward]**](PortForward.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.port_forward_response import PortForwardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PortForwardResponse from a JSON string
port_forward_response_instance = PortForwardResponse.from_json(json)
# print the JSON string representation of the object
print PortForwardResponse.to_json()

# convert the object into a dict
port_forward_response_dict = port_forward_response_instance.to_dict()
# create an instance of PortForwardResponse from a dict
port_forward_response_form_dict = port_forward_response.from_dict(port_forward_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


