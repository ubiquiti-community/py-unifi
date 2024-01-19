# SettingIpsAlerts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**gid** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**signature** | **str** |  | [optional] 
**tracking** | [**List[SettingIpsTracking]**](SettingIpsTracking.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.setting_ips_alerts import SettingIpsAlerts

# TODO update the JSON string below
json = "{}"
# create an instance of SettingIpsAlerts from a JSON string
setting_ips_alerts_instance = SettingIpsAlerts.from_json(json)
# print the JSON string representation of the object
print SettingIpsAlerts.to_json()

# convert the object into a dict
setting_ips_alerts_dict = setting_ips_alerts_instance.to_dict()
# create an instance of SettingIpsAlerts from a dict
setting_ips_alerts_form_dict = setting_ips_alerts.from_dict(setting_ips_alerts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


