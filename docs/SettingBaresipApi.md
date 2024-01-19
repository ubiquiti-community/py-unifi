# unifi_client.SettingBaresipApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_baresip**](SettingBaresipApi.md#get_setting_baresip) | **GET** /get/setting/baresip | 
[**update_setting_baresip**](SettingBaresipApi.md#update_setting_baresip) | **PUT** /set/setting/baresip | 


# **get_setting_baresip**
> SettingBaresipResponse get_setting_baresip()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_baresip_response import SettingBaresipResponse
from unifi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://unifi.ui.com/proxy/network/api/s/default
# See configuration.py for a list of all supported configuration parameters.
configuration = unifi_client.Configuration(
    host = "https://unifi.ui.com/proxy/network/api/s/default"
)


# Enter a context with an instance of the API client
async with unifi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = unifi_client.SettingBaresipApi(api_client)

    try:
        api_response = await api_instance.get_setting_baresip()
        print("The response of SettingBaresipApi->get_setting_baresip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingBaresipApi->get_setting_baresip: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingBaresipResponse**](SettingBaresipResponse.md)

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

# **update_setting_baresip**
> SettingBaresipResponse update_setting_baresip(setting_baresip=setting_baresip)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_baresip import SettingBaresip
from unifi_client.models.setting_baresip_response import SettingBaresipResponse
from unifi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://unifi.ui.com/proxy/network/api/s/default
# See configuration.py for a list of all supported configuration parameters.
configuration = unifi_client.Configuration(
    host = "https://unifi.ui.com/proxy/network/api/s/default"
)


# Enter a context with an instance of the API client
async with unifi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = unifi_client.SettingBaresipApi(api_client)
    setting_baresip = unifi_client.SettingBaresip() # SettingBaresip |  (optional)

    try:
        api_response = await api_instance.update_setting_baresip(setting_baresip=setting_baresip)
        print("The response of SettingBaresipApi->update_setting_baresip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingBaresipApi->update_setting_baresip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_baresip** | [**SettingBaresip**](SettingBaresip.md)|  | [optional] 

### Return type

[**SettingBaresipResponse**](SettingBaresipResponse.md)

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

