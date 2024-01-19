# SettingIpsTracking


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.setting_ips_tracking import SettingIpsTracking

# TODO update the JSON string below
json = "{}"
# create an instance of SettingIpsTracking from a JSON string
setting_ips_tracking_instance = SettingIpsTracking.from_json(json)
# print the JSON string representation of the object
print SettingIpsTracking.to_json()

# convert the object into a dict
setting_ips_tracking_dict = setting_ips_tracking_instance.to_dict()
# create an instance of SettingIpsTracking from a dict
setting_ips_tracking_form_dict = setting_ips_tracking.from_dict(setting_ips_tracking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


