# WLANPrivatePresharedKeys


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**networkconf_id** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.wlan_private_preshared_keys import WLANPrivatePresharedKeys

# TODO update the JSON string below
json = "{}"
# create an instance of WLANPrivatePresharedKeys from a JSON string
wlan_private_preshared_keys_instance = WLANPrivatePresharedKeys.from_json(json)
# print the JSON string representation of the object
print WLANPrivatePresharedKeys.to_json()

# convert the object into a dict
wlan_private_preshared_keys_dict = wlan_private_preshared_keys_instance.to_dict()
# create an instance of WLANPrivatePresharedKeys from a dict
wlan_private_preshared_keys_form_dict = wlan_private_preshared_keys.from_dict(wlan_private_preshared_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


