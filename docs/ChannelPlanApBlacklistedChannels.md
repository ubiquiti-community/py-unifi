# ChannelPlanApBlacklistedChannels


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **int** |  | [optional] 
**mac** | **str** |  | [optional] 
**timestamp** | **int** |  | [optional] 

## Example

```python
from unifi_client.models.channel_plan_ap_blacklisted_channels import ChannelPlanApBlacklistedChannels

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelPlanApBlacklistedChannels from a JSON string
channel_plan_ap_blacklisted_channels_instance = ChannelPlanApBlacklistedChannels.from_json(json)
# print the JSON string representation of the object
print ChannelPlanApBlacklistedChannels.to_json()

# convert the object into a dict
channel_plan_ap_blacklisted_channels_dict = channel_plan_ap_blacklisted_channels_instance.to_dict()
# create an instance of ChannelPlanApBlacklistedChannels from a dict
channel_plan_ap_blacklisted_channels_form_dict = channel_plan_ap_blacklisted_channels.from_dict(channel_plan_ap_blacklisted_channels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


