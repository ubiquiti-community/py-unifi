# HotspotPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**charged_as** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**custom_payment_fields_enabled** | **bool** |  | [optional] 
**hours** | **int** |  | [optional] 
**index** | **int** |  | [optional] 
**limit_down** | **int** |  | [optional] 
**limit_overwrite** | **bool** |  | [optional] 
**limit_quota** | **int** |  | [optional] 
**limit_up** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**payment_fields_address_enabled** | **bool** |  | [optional] 
**payment_fields_address_required** | **bool** |  | [optional] 
**payment_fields_city_enabled** | **bool** |  | [optional] 
**payment_fields_city_required** | **bool** |  | [optional] 
**payment_fields_country_enabled** | **bool** |  | [optional] 
**payment_fields_country_required** | **bool** |  | [optional] 
**payment_fields_email_enabled** | **bool** |  | [optional] 
**payment_fields_email_required** | **bool** |  | [optional] 
**payment_fields_first_name_enabled** | **bool** |  | [optional] 
**payment_fields_first_name_required** | **bool** |  | [optional] 
**payment_fields_last_name_enabled** | **bool** |  | [optional] 
**payment_fields_last_name_required** | **bool** |  | [optional] 
**payment_fields_state_enabled** | **bool** |  | [optional] 
**payment_fields_state_required** | **bool** |  | [optional] 
**payment_fields_zip_enabled** | **bool** |  | [optional] 
**payment_fields_zip_required** | **bool** |  | [optional] 
**site_id** | **str** |  | [optional] 
**trial_duration_minutes** | **int** |  | [optional] 
**trial_reset** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.hotspot_package import HotspotPackage

# TODO update the JSON string below
json = "{}"
# create an instance of HotspotPackage from a JSON string
hotspot_package_instance = HotspotPackage.from_json(json)
# print the JSON string representation of the object
print HotspotPackage.to_json()

# convert the object into a dict
hotspot_package_dict = hotspot_package_instance.to_dict()
# create an instance of HotspotPackage from a dict
hotspot_package_form_dict = hotspot_package.from_dict(hotspot_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


