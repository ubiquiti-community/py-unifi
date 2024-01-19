# ChannelPlanResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ChannelPlan]**](ChannelPlan.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from unifi_client.models.channel_plan_response import ChannelPlanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelPlanResponse from a JSON string
channel_plan_response_instance = ChannelPlanResponse.from_json(json)
# print the JSON string representation of the object
print ChannelPlanResponse.to_json()

# convert the object into a dict
channel_plan_response_dict = channel_plan_response_instance.to_dict()
# create an instance of ChannelPlanResponse from a dict
channel_plan_response_form_dict = channel_plan_response.from_dict(channel_plan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


