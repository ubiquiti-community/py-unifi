# openapi_client.SettingDpiApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_dpi**](SettingDpiApi.md#get_setting_dpi) | **GET** /get/setting/dpi | 
[**update_setting_dpi**](SettingDpiApi.md#update_setting_dpi) | **PUT** /set/setting/dpi | 


# **get_setting_dpi**
> SettingDpiResponse get_setting_dpi()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_dpi_response import SettingDpiResponse
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
    api_instance = openapi_client.SettingDpiApi(api_client)

    try:
        api_response = api_instance.get_setting_dpi()
        print("The response of SettingDpiApi->get_setting_dpi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingDpiApi->get_setting_dpi: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingDpiResponse**](SettingDpiResponse.md)

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

# **update_setting_dpi**
> SettingDpiResponse update_setting_dpi(setting_dpi=setting_dpi)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_dpi import SettingDpi
from openapi_client.models.setting_dpi_response import SettingDpiResponse
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
    api_instance = openapi_client.SettingDpiApi(api_client)
    setting_dpi = openapi_client.SettingDpi() # SettingDpi |  (optional)

    try:
        api_response = api_instance.update_setting_dpi(setting_dpi=setting_dpi)
        print("The response of SettingDpiApi->update_setting_dpi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingDpiApi->update_setting_dpi: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_dpi** | [**SettingDpi**](SettingDpi.md)|  | [optional] 

### Return type

[**SettingDpiResponse**](SettingDpiResponse.md)

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

