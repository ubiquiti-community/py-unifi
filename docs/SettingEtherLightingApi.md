# unifi_client.SettingEtherLightingApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_ether_lighting**](SettingEtherLightingApi.md#get_setting_ether_lighting) | **GET** /get/setting/ether_lighting | 
[**update_setting_ether_lighting**](SettingEtherLightingApi.md#update_setting_ether_lighting) | **PUT** /set/setting/ether_lighting | 


# **get_setting_ether_lighting**
> SettingEtherLightingResponse get_setting_ether_lighting()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_ether_lighting_response import SettingEtherLightingResponse
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
    api_instance = unifi_client.SettingEtherLightingApi(api_client)

    try:
        api_response = await api_instance.get_setting_ether_lighting()
        print("The response of SettingEtherLightingApi->get_setting_ether_lighting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingEtherLightingApi->get_setting_ether_lighting: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingEtherLightingResponse**](SettingEtherLightingResponse.md)

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

# **update_setting_ether_lighting**
> SettingEtherLightingResponse update_setting_ether_lighting(setting_ether_lighting=setting_ether_lighting)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_ether_lighting import SettingEtherLighting
from unifi_client.models.setting_ether_lighting_response import SettingEtherLightingResponse
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
    api_instance = unifi_client.SettingEtherLightingApi(api_client)
    setting_ether_lighting = unifi_client.SettingEtherLighting() # SettingEtherLighting |  (optional)

    try:
        api_response = await api_instance.update_setting_ether_lighting(setting_ether_lighting=setting_ether_lighting)
        print("The response of SettingEtherLightingApi->update_setting_ether_lighting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingEtherLightingApi->update_setting_ether_lighting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_ether_lighting** | [**SettingEtherLighting**](SettingEtherLighting.md)|  | [optional] 

### Return type

[**SettingEtherLightingResponse**](SettingEtherLightingResponse.md)

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

