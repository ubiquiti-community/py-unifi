# unifi_client.SettingNetworkOptimizationApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_network_optimization**](SettingNetworkOptimizationApi.md#get_setting_network_optimization) | **GET** /get/setting/network_optimization | 
[**update_setting_network_optimization**](SettingNetworkOptimizationApi.md#update_setting_network_optimization) | **PUT** /set/setting/network_optimization | 


# **get_setting_network_optimization**
> SettingNetworkOptimizationResponse get_setting_network_optimization()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_network_optimization_response import SettingNetworkOptimizationResponse
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
    api_instance = unifi_client.SettingNetworkOptimizationApi(api_client)

    try:
        api_response = await api_instance.get_setting_network_optimization()
        print("The response of SettingNetworkOptimizationApi->get_setting_network_optimization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingNetworkOptimizationApi->get_setting_network_optimization: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingNetworkOptimizationResponse**](SettingNetworkOptimizationResponse.md)

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

# **update_setting_network_optimization**
> SettingNetworkOptimizationResponse update_setting_network_optimization(setting_network_optimization=setting_network_optimization)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_network_optimization import SettingNetworkOptimization
from unifi_client.models.setting_network_optimization_response import SettingNetworkOptimizationResponse
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
    api_instance = unifi_client.SettingNetworkOptimizationApi(api_client)
    setting_network_optimization = unifi_client.SettingNetworkOptimization() # SettingNetworkOptimization |  (optional)

    try:
        api_response = await api_instance.update_setting_network_optimization(setting_network_optimization=setting_network_optimization)
        print("The response of SettingNetworkOptimizationApi->update_setting_network_optimization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingNetworkOptimizationApi->update_setting_network_optimization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_network_optimization** | [**SettingNetworkOptimization**](SettingNetworkOptimization.md)|  | [optional] 

### Return type

[**SettingNetworkOptimizationResponse**](SettingNetworkOptimizationResponse.md)

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

