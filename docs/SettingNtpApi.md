# openapi_client.SettingNtpApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_ntp**](SettingNtpApi.md#get_setting_ntp) | **GET** /get/setting/ntp | 
[**update_setting_ntp**](SettingNtpApi.md#update_setting_ntp) | **PUT** /set/setting/ntp | 


# **get_setting_ntp**
> SettingNtpResponse get_setting_ntp()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_ntp_response import SettingNtpResponse
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
    api_instance = openapi_client.SettingNtpApi(api_client)

    try:
        api_response = api_instance.get_setting_ntp()
        print("The response of SettingNtpApi->get_setting_ntp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingNtpApi->get_setting_ntp: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingNtpResponse**](SettingNtpResponse.md)

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

# **update_setting_ntp**
> SettingNtpResponse update_setting_ntp(setting_ntp=setting_ntp)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_ntp import SettingNtp
from openapi_client.models.setting_ntp_response import SettingNtpResponse
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
    api_instance = openapi_client.SettingNtpApi(api_client)
    setting_ntp = openapi_client.SettingNtp() # SettingNtp |  (optional)

    try:
        api_response = api_instance.update_setting_ntp(setting_ntp=setting_ntp)
        print("The response of SettingNtpApi->update_setting_ntp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingNtpApi->update_setting_ntp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_ntp** | [**SettingNtp**](SettingNtp.md)|  | [optional] 

### Return type

[**SettingNtpResponse**](SettingNtpResponse.md)

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

