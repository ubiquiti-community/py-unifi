# openapi_client.SettingConnectivityApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_connectivity**](SettingConnectivityApi.md#get_setting_connectivity) | **GET** /get/setting/connectivity | 
[**update_setting_connectivity**](SettingConnectivityApi.md#update_setting_connectivity) | **PUT** /set/setting/connectivity | 


# **get_setting_connectivity**
> SettingConnectivityResponse get_setting_connectivity()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_connectivity_response import SettingConnectivityResponse
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
    api_instance = openapi_client.SettingConnectivityApi(api_client)

    try:
        api_response = api_instance.get_setting_connectivity()
        print("The response of SettingConnectivityApi->get_setting_connectivity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingConnectivityApi->get_setting_connectivity: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingConnectivityResponse**](SettingConnectivityResponse.md)

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

# **update_setting_connectivity**
> SettingConnectivityResponse update_setting_connectivity(setting_connectivity=setting_connectivity)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_connectivity import SettingConnectivity
from openapi_client.models.setting_connectivity_response import SettingConnectivityResponse
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
    api_instance = openapi_client.SettingConnectivityApi(api_client)
    setting_connectivity = openapi_client.SettingConnectivity() # SettingConnectivity |  (optional)

    try:
        api_response = api_instance.update_setting_connectivity(setting_connectivity=setting_connectivity)
        print("The response of SettingConnectivityApi->update_setting_connectivity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingConnectivityApi->update_setting_connectivity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_connectivity** | [**SettingConnectivity**](SettingConnectivity.md)|  | [optional] 

### Return type

[**SettingConnectivityResponse**](SettingConnectivityResponse.md)

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

