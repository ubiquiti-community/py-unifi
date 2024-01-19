# ScheduleTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**action** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**cron_expr** | **str** |  | [optional] 
**execute_only_once** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**upgrade_targets** | [**List[ScheduleTaskUpgradeTargets]**](ScheduleTaskUpgradeTargets.md) |  | [optional] 

## Example

```python
from unifi_client.models.schedule_task import ScheduleTask

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleTask from a JSON string
schedule_task_instance = ScheduleTask.from_json(json)
# print the JSON string representation of the object
print ScheduleTask.to_json()

# convert the object into a dict
schedule_task_dict = schedule_task_instance.to_dict()
# create an instance of ScheduleTask from a dict
schedule_task_form_dict = schedule_task.from_dict(schedule_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


