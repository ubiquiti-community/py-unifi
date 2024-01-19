# Hotspot2ConfOsu


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**List[Hotspot2ConfDescription]**](Hotspot2ConfDescription.md) |  | [optional] 
**friendly_name** | [**List[Hotspot2ConfFriendlyName]**](Hotspot2ConfFriendlyName.md) |  | [optional] 
**icon** | [**List[Hotspot2ConfIcon]**](Hotspot2ConfIcon.md) |  | [optional] 
**method_oma_dm** | **bool** |  | [optional] 
**method_soap_xml_spp** | **bool** |  | [optional] 
**nai** | **str** |  | [optional] 
**nai2** | **str** |  | [optional] 
**operating_class** | **str** |  | [optional] 
**server_uri** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.hotspot2_conf_osu import Hotspot2ConfOsu

# TODO update the JSON string below
json = "{}"
# create an instance of Hotspot2ConfOsu from a JSON string
hotspot2_conf_osu_instance = Hotspot2ConfOsu.from_json(json)
# print the JSON string representation of the object
print Hotspot2ConfOsu.to_json()

# convert the object into a dict
hotspot2_conf_osu_dict = hotspot2_conf_osu_instance.to_dict()
# create an instance of Hotspot2ConfOsu from a dict
hotspot2_conf_osu_form_dict = hotspot2_conf_osu.from_dict(hotspot2_conf_osu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


