# SettingSuperCloudaccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**device_auth** | **str** |  | [optional] 
**device_id** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**ubic_uuid** | **str** |  | [optional] 
**x_certificate_arn** | **str** |  | [optional] 
**x_certificate_pem** | **str** |  | [optional] 
**x_private_key** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.setting_super_cloudaccess import SettingSuperCloudaccess

# TODO update the JSON string below
json = "{}"
# create an instance of SettingSuperCloudaccess from a JSON string
setting_super_cloudaccess_instance = SettingSuperCloudaccess.from_json(json)
# print the JSON string representation of the object
print SettingSuperCloudaccess.to_json()

# convert the object into a dict
setting_super_cloudaccess_dict = setting_super_cloudaccess_instance.to_dict()
# create an instance of SettingSuperCloudaccess from a dict
setting_super_cloudaccess_form_dict = setting_super_cloudaccess.from_dict(setting_super_cloudaccess_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


