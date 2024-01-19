# Hotspot2ConfResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Hotspot2Conf]**](Hotspot2Conf.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from unifi_client.models.hotspot2_conf_response import Hotspot2ConfResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Hotspot2ConfResponse from a JSON string
hotspot2_conf_response_instance = Hotspot2ConfResponse.from_json(json)
# print the JSON string representation of the object
print Hotspot2ConfResponse.to_json()

# convert the object into a dict
hotspot2_conf_response_dict = hotspot2_conf_response_instance.to_dict()
# create an instance of Hotspot2ConfResponse from a dict
hotspot2_conf_response_form_dict = hotspot2_conf_response.from_dict(hotspot2_conf_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


