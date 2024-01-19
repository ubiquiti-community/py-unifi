# HeatMapResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[HeatMap]**](HeatMap.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from unifi_client.models.heat_map_response import HeatMapResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HeatMapResponse from a JSON string
heat_map_response_instance = HeatMapResponse.from_json(json)
# print the JSON string representation of the object
print HeatMapResponse.to_json()

# convert the object into a dict
heat_map_response_dict = heat_map_response_instance.to_dict()
# create an instance of HeatMapResponse from a dict
heat_map_response_form_dict = heat_map_response.from_dict(heat_map_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


