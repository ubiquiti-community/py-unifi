# ChannelPlanUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**ap_blacklisted_channels** | [**List[ChannelPlanApBlacklistedChannels]**](ChannelPlanApBlacklistedChannels.md) |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**conf_source** | **str** |  | [optional] 
**coupling** | [**List[ChannelPlanCoupling]**](ChannelPlanCoupling.md) |  | [optional] 
**var_date** | **str** |  | [optional] 
**fitness** | **float** |  | [optional] 
**note** | **str** |  | [optional] 
**radio** | **str** |  | [optional] 
**radio_table** | [**List[ChannelPlanRadioTable]**](ChannelPlanRadioTable.md) |  | [optional] 
**satisfaction** | **float** |  | [optional] 
**satisfaction_table** | [**List[ChannelPlanSatisfactionTable]**](ChannelPlanSatisfactionTable.md) |  | [optional] 
**site_blacklisted_channels** | [**List[ChannelPlanSiteBlacklistedChannels]**](ChannelPlanSiteBlacklistedChannels.md) |  | [optional] 
**site_id** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.channel_plan_update_request import ChannelPlanUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelPlanUpdateRequest from a JSON string
channel_plan_update_request_instance = ChannelPlanUpdateRequest.from_json(json)
# print the JSON string representation of the object
print ChannelPlanUpdateRequest.to_json()

# convert the object into a dict
channel_plan_update_request_dict = channel_plan_update_request_instance.to_dict()
# create an instance of ChannelPlanUpdateRequest from a dict
channel_plan_update_request_form_dict = channel_plan_update_request.from_dict(channel_plan_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


