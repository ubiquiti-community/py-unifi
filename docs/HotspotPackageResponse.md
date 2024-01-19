# HotspotPackageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[HotspotPackage]**](HotspotPackage.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openapi_client.models.hotspot_package_response import HotspotPackageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HotspotPackageResponse from a JSON string
hotspot_package_response_instance = HotspotPackageResponse.from_json(json)
# print the JSON string representation of the object
print HotspotPackageResponse.to_json()

# convert the object into a dict
hotspot_package_response_dict = hotspot_package_response_instance.to_dict()
# create an instance of HotspotPackageResponse from a dict
hotspot_package_response_form_dict = hotspot_package_response.from_dict(hotspot_package_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


