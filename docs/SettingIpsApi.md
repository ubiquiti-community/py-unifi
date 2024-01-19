# openapi_client.SettingIpsApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_ips**](SettingIpsApi.md#get_setting_ips) | **GET** /get/setting/ips | 
[**update_setting_ips**](SettingIpsApi.md#update_setting_ips) | **PUT** /set/setting/ips | 


# **get_setting_ips**
> SettingIpsResponse get_setting_ips()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_ips_response import SettingIpsResponse
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
    api_instance = openapi_client.SettingIpsApi(api_client)

    try:
        api_response = api_instance.get_setting_ips()
        print("The response of SettingIpsApi->get_setting_ips:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingIpsApi->get_setting_ips: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingIpsResponse**](SettingIpsResponse.md)

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

# **update_setting_ips**
> SettingIpsResponse update_setting_ips(setting_ips=setting_ips)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_ips import SettingIps
from openapi_client.models.setting_ips_response import SettingIpsResponse
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
    api_instance = openapi_client.SettingIpsApi(api_client)
    setting_ips = openapi_client.SettingIps() # SettingIps |  (optional)

    try:
        api_response = api_instance.update_setting_ips(setting_ips=setting_ips)
        print("The response of SettingIpsApi->update_setting_ips:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingIpsApi->update_setting_ips: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_ips** | [**SettingIps**](SettingIps.md)|  | [optional] 

### Return type

[**SettingIpsResponse**](SettingIpsResponse.md)

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

