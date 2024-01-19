# WLANGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WLANGroup]**](WLANGroup.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from unifi_client.models.wlan_group_response import WLANGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WLANGroupResponse from a JSON string
wlan_group_response_instance = WLANGroupResponse.from_json(json)
# print the JSON string representation of the object
print WLANGroupResponse.to_json()

# convert the object into a dict
wlan_group_response_dict = wlan_group_response_instance.to_dict()
# create an instance of WLANGroupResponse from a dict
wlan_group_response_form_dict = wlan_group_response.from_dict(wlan_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


