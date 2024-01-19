# DpiGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**dpiapp_ids** | **List[str]** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.dpi_group import DpiGroup

# TODO update the JSON string below
json = "{}"
# create an instance of DpiGroup from a JSON string
dpi_group_instance = DpiGroup.from_json(json)
# print the JSON string representation of the object
print DpiGroup.to_json()

# convert the object into a dict
dpi_group_dict = dpi_group_instance.to_dict()
# create an instance of DpiGroup from a dict
dpi_group_form_dict = dpi_group.from_dict(dpi_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


