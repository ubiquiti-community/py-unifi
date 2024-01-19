# SettingLcm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**brightness** | **int** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**idle_timeout** | **int** |  | [optional] 
**key** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**sync** | **bool** |  | [optional] 
**touch_event** | **bool** |  | [optional] 

## Example

```python
from unifi_client.models.setting_lcm import SettingLcm

# TODO update the JSON string below
json = "{}"
# create an instance of SettingLcm from a JSON string
setting_lcm_instance = SettingLcm.from_json(json)
# print the JSON string representation of the object
print SettingLcm.to_json()

# convert the object into a dict
setting_lcm_dict = setting_lcm_instance.to_dict()
# create an instance of SettingLcm from a dict
setting_lcm_form_dict = setting_lcm.from_dict(setting_lcm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


