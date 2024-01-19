# Hotspot2ConfDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.hotspot2_conf_description import Hotspot2ConfDescription

# TODO update the JSON string below
json = "{}"
# create an instance of Hotspot2ConfDescription from a JSON string
hotspot2_conf_description_instance = Hotspot2ConfDescription.from_json(json)
# print the JSON string representation of the object
print Hotspot2ConfDescription.to_json()

# convert the object into a dict
hotspot2_conf_description_dict = hotspot2_conf_description_instance.to_dict()
# create an instance of Hotspot2ConfDescription from a dict
hotspot2_conf_description_form_dict = hotspot2_conf_description.from_dict(hotspot2_conf_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


