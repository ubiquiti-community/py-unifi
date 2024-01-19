# WLANResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WLAN]**](WLAN.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.wlan_response import WLANResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WLANResponse from a JSON string
wlan_response_instance = WLANResponse.from_json(json)
# print the JSON string representation of the object
print WLANResponse.to_json()

# convert the object into a dict
wlan_response_dict = wlan_response_instance.to_dict()
# create an instance of WLANResponse from a dict
wlan_response_form_dict = wlan_response.from_dict(wlan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


