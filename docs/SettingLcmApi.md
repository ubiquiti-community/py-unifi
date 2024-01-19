# openapi_client.SettingLcmApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_lcm**](SettingLcmApi.md#get_setting_lcm) | **GET** /get/setting/lcm | 
[**update_setting_lcm**](SettingLcmApi.md#update_setting_lcm) | **PUT** /set/setting/lcm | 


# **get_setting_lcm**
> SettingLcmResponse get_setting_lcm()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_lcm_response import SettingLcmResponse
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
    api_instance = openapi_client.SettingLcmApi(api_client)

    try:
        api_response = api_instance.get_setting_lcm()
        print("The response of SettingLcmApi->get_setting_lcm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingLcmApi->get_setting_lcm: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingLcmResponse**](SettingLcmResponse.md)

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

# **update_setting_lcm**
> SettingLcmResponse update_setting_lcm(setting_lcm=setting_lcm)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_lcm import SettingLcm
from openapi_client.models.setting_lcm_response import SettingLcmResponse
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
    api_instance = openapi_client.SettingLcmApi(api_client)
    setting_lcm = openapi_client.SettingLcm() # SettingLcm |  (optional)

    try:
        api_response = api_instance.update_setting_lcm(setting_lcm=setting_lcm)
        print("The response of SettingLcmApi->update_setting_lcm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingLcmApi->update_setting_lcm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_lcm** | [**SettingLcm**](SettingLcm.md)|  | [optional] 

### Return type

[**SettingLcmResponse**](SettingLcmResponse.md)

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

