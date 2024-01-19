# openapi_client.SettingRadiusApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_radius**](SettingRadiusApi.md#get_setting_radius) | **GET** /get/setting/radius | 
[**update_setting_radius**](SettingRadiusApi.md#update_setting_radius) | **PUT** /set/setting/radius | 


# **get_setting_radius**
> SettingRadiusResponse get_setting_radius()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_radius_response import SettingRadiusResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://unifi.ui.com/proxy/network/api/s/default
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://unifi.ui.com/proxy/network/api/s/default"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SettingRadiusApi(api_client)

    try:
        api_response = api_instance.get_setting_radius()
        print("The response of SettingRadiusApi->get_setting_radius:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingRadiusApi->get_setting_radius: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingRadiusResponse**](SettingRadiusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_setting_radius**
> SettingRadiusResponse update_setting_radius(setting_radius=setting_radius)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_radius import SettingRadius
from openapi_client.models.setting_radius_response import SettingRadiusResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://unifi.ui.com/proxy/network/api/s/default
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://unifi.ui.com/proxy/network/api/s/default"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SettingRadiusApi(api_client)
    setting_radius = openapi_client.SettingRadius() # SettingRadius |  (optional)

    try:
        api_response = api_instance.update_setting_radius(setting_radius=setting_radius)
        print("The response of SettingRadiusApi->update_setting_radius:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingRadiusApi->update_setting_radius: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_radius** | [**SettingRadius**](SettingRadius.md)|  | [optional] 

### Return type

[**SettingRadiusResponse**](SettingRadiusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

