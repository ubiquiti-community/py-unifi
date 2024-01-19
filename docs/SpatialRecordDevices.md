# SpatialRecordDevices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mac** | **str** |  | [optional] 
**position** | [**SpatialRecordPosition**](SpatialRecordPosition.md) |  | [optional] 

## Example

```python
from unifi_client.models.spatial_record_devices import SpatialRecordDevices

# TODO update the JSON string below
json = "{}"
# create an instance of SpatialRecordDevices from a JSON string
spatial_record_devices_instance = SpatialRecordDevices.from_json(json)
# print the JSON string representation of the object
print SpatialRecordDevices.to_json()

# convert the object into a dict
spatial_record_devices_dict = spatial_record_devices_instance.to_dict()
# create an instance of SpatialRecordDevices from a dict
spatial_record_devices_form_dict = spatial_record_devices.from_dict(spatial_record_devices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


