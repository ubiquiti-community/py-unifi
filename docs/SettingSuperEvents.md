# SettingSuperEvents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**ignored** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.setting_super_events import SettingSuperEvents

# TODO update the JSON string below
json = "{}"
# create an instance of SettingSuperEvents from a JSON string
setting_super_events_instance = SettingSuperEvents.from_json(json)
# print the JSON string representation of the object
print SettingSuperEvents.to_json()

# convert the object into a dict
setting_super_events_dict = setting_super_events_instance.to_dict()
# create an instance of SettingSuperEvents from a dict
setting_super_events_form_dict = setting_super_events.from_dict(setting_super_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


