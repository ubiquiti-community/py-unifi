# WLANSaePsk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**mac** | **str** |  | [optional] 
**psk** | **str** |  | [optional] 
**vlan** | **int** |  | [optional] 

## Example

```python
from unifi_client.models.wlan_sae_psk import WLANSaePsk

# TODO update the JSON string below
json = "{}"
# create an instance of WLANSaePsk from a JSON string
wlan_sae_psk_instance = WLANSaePsk.from_json(json)
# print the JSON string representation of the object
print WLANSaePsk.to_json()

# convert the object into a dict
wlan_sae_psk_dict = wlan_sae_psk_instance.to_dict()
# create an instance of WLANSaePsk from a dict
wlan_sae_psk_form_dict = wlan_sae_psk.from_dict(wlan_sae_psk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


