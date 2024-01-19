# HeatMap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**map_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.heat_map import HeatMap

# TODO update the JSON string below
json = "{}"
# create an instance of HeatMap from a JSON string
heat_map_instance = HeatMap.from_json(json)
# print the JSON string representation of the object
print HeatMap.to_json()

# convert the object into a dict
heat_map_dict = heat_map_instance.to_dict()
# create an instance of HeatMap from a dict
heat_map_form_dict = heat_map.from_dict(heat_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


