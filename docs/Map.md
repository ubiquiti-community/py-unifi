# Map


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**lat** | **str** |  | [optional] 
**lng** | **str** |  | [optional] 
**map_type_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**offset_left** | **float** |  | [optional] 
**offset_top** | **float** |  | [optional] 
**opacity** | **float** |  | [optional] 
**selected** | **bool** |  | [optional] 
**site_id** | **str** |  | [optional] 
**tilt** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 
**upp** | **float** |  | [optional] 
**zoom** | **int** |  | [optional] 

## Example

```python
from unifi_client.models.map import Map

# TODO update the JSON string below
json = "{}"
# create an instance of Map from a JSON string
map_instance = Map.from_json(json)
# print the JSON string representation of the object
print Map.to_json()

# convert the object into a dict
map_dict = map_instance.to_dict()
# create an instance of Map from a dict
map_form_dict = map.from_dict(map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


