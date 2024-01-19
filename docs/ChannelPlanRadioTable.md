# ChannelPlanRadioTable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_channel** | **str** |  | [optional] 
**channel** | **str** |  | [optional] 
**device_mac** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**tx_power** | **str** |  | [optional] 
**tx_power_mode** | **str** |  | [optional] 
**width** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.channel_plan_radio_table import ChannelPlanRadioTable

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelPlanRadioTable from a JSON string
channel_plan_radio_table_instance = ChannelPlanRadioTable.from_json(json)
# print the JSON string representation of the object
print ChannelPlanRadioTable.to_json()

# convert the object into a dict
channel_plan_radio_table_dict = channel_plan_radio_table_instance.to_dict()
# create an instance of ChannelPlanRadioTable from a dict
channel_plan_radio_table_form_dict = channel_plan_radio_table.from_dict(channel_plan_radio_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


