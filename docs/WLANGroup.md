# WLANGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.wlan_group import WLANGroup

# TODO update the JSON string below
json = "{}"
# create an instance of WLANGroup from a JSON string
wlan_group_instance = WLANGroup.from_json(json)
# print the JSON string representation of the object
print WLANGroup.to_json()

# convert the object into a dict
wlan_group_dict = wlan_group_instance.to_dict()
# create an instance of WLANGroup from a dict
wlan_group_form_dict = wlan_group.from_dict(wlan_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


