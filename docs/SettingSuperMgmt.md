# SettingSuperMgmt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**analytics_disapproved_for** | **str** |  | [optional] 
**attr_hidden** | **bool** |  | [optional] 
**attr_hidden_id** | **str** |  | [optional] 
**attr_no_delete** | **bool** |  | [optional] 
**attr_no_edit** | **bool** |  | [optional] 
**auto_upgrade** | **bool** |  | [optional] 
**autobackup_cron_expr** | **str** |  | [optional] 
**autobackup_days** | **int** |  | [optional] 
**autobackup_enabled** | **bool** |  | [optional] 
**autobackup_gcs_bucket** | **str** |  | [optional] 
**autobackup_gcs_certificate_path** | **str** |  | [optional] 
**autobackup_local_path** | **str** |  | [optional] 
**autobackup_max_files** | **int** |  | [optional] 
**autobackup_post_actions** | **List[str]** |  | [optional] 
**autobackup_s3_access_key** | **str** |  | [optional] 
**autobackup_s3_access_secret** | **str** |  | [optional] 
**autobackup_s3_bucket** | **str** |  | [optional] 
**autobackup_timezone** | **str** |  | [optional] 
**backup_to_cloud_enabled** | **bool** |  | [optional] 
**contact_info_city** | **str** |  | [optional] 
**contact_info_company_name** | **str** |  | [optional] 
**contact_info_country** | **str** |  | [optional] 
**contact_info_full_name** | **str** |  | [optional] 
**contact_info_phone_number** | **str** |  | [optional] 
**contact_info_shipping_address_1** | **str** |  | [optional] 
**contact_info_shipping_address_2** | **str** |  | [optional] 
**contact_info_state** | **str** |  | [optional] 
**contact_info_zip** | **str** |  | [optional] 
**data_retention_setting_preference** | **str** |  | [optional] 
**data_retention_time_in_hours_for_5minutes_scale** | **int** |  | [optional] 
**data_retention_time_in_hours_for_daily_scale** | **int** |  | [optional] 
**data_retention_time_in_hours_for_hourly_scale** | **int** |  | [optional] 
**data_retention_time_in_hours_for_monthly_scale** | **int** |  | [optional] 
**data_retention_time_in_hours_for_others** | **int** |  | [optional] 
**default_site_device_auth_password_alert** | **str** |  | [optional] 
**discoverable** | **bool** |  | [optional] 
**enable_analytics** | **bool** |  | [optional] 
**google_maps_api_key** | **str** |  | [optional] 
**image_maps_use_google_engine** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**led_enabled** | **bool** |  | [optional] 
**live_chat** | **str** |  | [optional] 
**live_updates** | **str** |  | [optional] 
**minimum_usable_hd_space** | **int** |  | [optional] 
**minimum_usable_sd_space** | **int** |  | [optional] 
**multiple_sites_enabled** | **bool** |  | [optional] 
**override_inform_host** | **bool** |  | [optional] 
**override_inform_host_location** | **str** |  | [optional] 
**site_id** | **str** |  | [optional] 
**store_enabled** | **str** |  | [optional] 
**time_series_per_client_stats_enabled** | **bool** |  | [optional] 
**x_ssh_password** | **str** |  | [optional] 
**x_ssh_username** | **str** |  | [optional] 

## Example

```python
from unifi_client.models.setting_super_mgmt import SettingSuperMgmt

# TODO update the JSON string below
json = "{}"
# create an instance of SettingSuperMgmt from a JSON string
setting_super_mgmt_instance = SettingSuperMgmt.from_json(json)
# print the JSON string representation of the object
print SettingSuperMgmt.to_json()

# convert the object into a dict
setting_super_mgmt_dict = setting_super_mgmt_instance.to_dict()
# create an instance of SettingSuperMgmt from a dict
setting_super_mgmt_form_dict = setting_super_mgmt.from_dict(setting_super_mgmt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


