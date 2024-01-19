# WLANScheduleWithDuration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_minutes** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**start_days_of_week** | **List[str]** |  | [optional] 
**start_hour** | **int** |  | [optional] 
**start_minute** | **int** |  | [optional] 

## Example

```python
from unifi_client.models.wlan_schedule_with_duration import WLANScheduleWithDuration

# TODO update the JSON string below
json = "{}"
# create an instance of WLANScheduleWithDuration from a JSON string
wlan_schedule_with_duration_instance = WLANScheduleWithDuration.from_json(json)
# print the JSON string representation of the object
print WLANScheduleWithDuration.to_json()

# convert the object into a dict
wlan_schedule_with_duration_dict = wlan_schedule_with_duration_instance.to_dict()
# create an instance of WLANScheduleWithDuration from a dict
wlan_schedule_with_duration_form_dict = wlan_schedule_with_duration.from_dict(wlan_schedule_with_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


