# openapi_client.SettingGlobalApApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_global_ap**](SettingGlobalApApi.md#get_setting_global_ap) | **GET** /get/setting/global_ap | 
[**update_setting_global_ap**](SettingGlobalApApi.md#update_setting_global_ap) | **PUT** /set/setting/global_ap | 


# **get_setting_global_ap**
> SettingGlobalApResponse get_setting_global_ap()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_global_ap_response import SettingGlobalApResponse
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
    api_instance = openapi_client.SettingGlobalApApi(api_client)

    try:
        api_response = api_instance.get_setting_global_ap()
        print("The response of SettingGlobalApApi->get_setting_global_ap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingGlobalApApi->get_setting_global_ap: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingGlobalApResponse**](SettingGlobalApResponse.md)

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

# **update_setting_global_ap**
> SettingGlobalApResponse update_setting_global_ap(setting_global_ap=setting_global_ap)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_global_ap import SettingGlobalAp
from openapi_client.models.setting_global_ap_response import SettingGlobalApResponse
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
    api_instance = openapi_client.SettingGlobalApApi(api_client)
    setting_global_ap = openapi_client.SettingGlobalAp() # SettingGlobalAp |  (optional)

    try:
        api_response = api_instance.update_setting_global_ap(setting_global_ap=setting_global_ap)
        print("The response of SettingGlobalApApi->update_setting_global_ap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingGlobalApApi->update_setting_global_ap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_global_ap** | [**SettingGlobalAp**](SettingGlobalAp.md)|  | [optional] 

### Return type

[**SettingGlobalApResponse**](SettingGlobalApResponse.md)

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

