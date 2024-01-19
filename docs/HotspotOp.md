# HotspotOp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**x_password** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.hotspot_op import HotspotOp

# TODO update the JSON string below
json = "{}"
# create an instance of HotspotOp from a JSON string
hotspot_op_instance = HotspotOp.from_json(json)
# print the JSON string representation of the object
print HotspotOp.to_json()

# convert the object into a dict
hotspot_op_dict = hotspot_op_instance.to_dict()
# create an instance of HotspotOp from a dict
hotspot_op_form_dict = hotspot_op.from_dict(hotspot_op_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


