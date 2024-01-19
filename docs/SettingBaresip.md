# SettingBaresip


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**outbound_proxy** | **str** |  | [optional] 
**package_url** | **str** |  | [optional] 
**server** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.setting_baresip import SettingBaresip

# TODO update the JSON string below
json = "{}"
# create an instance of SettingBaresip from a JSON string
setting_baresip_instance = SettingBaresip.from_json(json)
# print the JSON string representation of the object
print SettingBaresip.to_json()

# convert the object into a dict
setting_baresip_dict = setting_baresip_instance.to_dict()
# create an instance of SettingBaresip from a dict
setting_baresip_form_dict = setting_baresip.from_dict(setting_baresip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


