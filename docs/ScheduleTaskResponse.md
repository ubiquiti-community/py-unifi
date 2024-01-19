# ScheduleTaskResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ScheduleTask]**](ScheduleTask.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_task_response import ScheduleTaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleTaskResponse from a JSON string
schedule_task_response_instance = ScheduleTaskResponse.from_json(json)
# print the JSON string representation of the object
print ScheduleTaskResponse.to_json()

# convert the object into a dict
schedule_task_response_dict = schedule_task_response_instance.to_dict()
# create an instance of ScheduleTaskResponse from a dict
schedule_task_response_form_dict = schedule_task_response.from_dict(schedule_task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


