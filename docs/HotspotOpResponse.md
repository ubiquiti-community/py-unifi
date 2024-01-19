# HotspotOpResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[HotspotOp]**](HotspotOp.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.hotspot_op_response import HotspotOpResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HotspotOpResponse from a JSON string
hotspot_op_response_instance = HotspotOpResponse.from_json(json)
# print the JSON string representation of the object
print HotspotOpResponse.to_json()

# convert the object into a dict
hotspot_op_response_dict = hotspot_op_response_instance.to_dict()
# create an instance of HotspotOpResponse from a dict
hotspot_op_response_form_dict = hotspot_op_response.from_dict(hotspot_op_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


