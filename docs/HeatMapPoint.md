# HeatMapPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**download_speed** | **float** |  | [optional] 
**heatmap_id** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**upload_speed** | **float** |  | [optional] 
**x** | **float** |  | [optional] 
**y** | **float** |  | [optional] 

## Example

```python
from unifi_client.models.heat_map_point import HeatMapPoint

# TODO update the JSON string below
json = "{}"
# create an instance of HeatMapPoint from a JSON string
heat_map_point_instance = HeatMapPoint.from_json(json)
# print the JSON string representation of the object
print HeatMapPoint.to_json()

# convert the object into a dict
heat_map_point_dict = heat_map_point_instance.to_dict()
# create an instance of HeatMapPoint from a dict
heat_map_point_form_dict = heat_map_point.from_dict(heat_map_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


