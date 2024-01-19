# unifi_client.SettingBroadcastApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_broadcast**](SettingBroadcastApi.md#get_setting_broadcast) | **GET** /get/setting/broadcast | 
[**update_setting_broadcast**](SettingBroadcastApi.md#update_setting_broadcast) | **PUT** /set/setting/broadcast | 


# **get_setting_broadcast**
> SettingBroadcastResponse get_setting_broadcast()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_broadcast_response import SettingBroadcastResponse
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
    api_instance = unifi_client.SettingBroadcastApi(api_client)

    try:
        api_response = await api_instance.get_setting_broadcast()
        print("The response of SettingBroadcastApi->get_setting_broadcast:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingBroadcastApi->get_setting_broadcast: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingBroadcastResponse**](SettingBroadcastResponse.md)

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

# **update_setting_broadcast**
> SettingBroadcastResponse update_setting_broadcast(setting_broadcast=setting_broadcast)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_broadcast import SettingBroadcast
from unifi_client.models.setting_broadcast_response import SettingBroadcastResponse
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
    api_instance = unifi_client.SettingBroadcastApi(api_client)
    setting_broadcast = unifi_client.SettingBroadcast() # SettingBroadcast |  (optional)

    try:
        api_response = await api_instance.update_setting_broadcast(setting_broadcast=setting_broadcast)
        print("The response of SettingBroadcastApi->update_setting_broadcast:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingBroadcastApi->update_setting_broadcast: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_broadcast** | [**SettingBroadcast**](SettingBroadcast.md)|  | [optional] 

### Return type

[**SettingBroadcastResponse**](SettingBroadcastResponse.md)

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

