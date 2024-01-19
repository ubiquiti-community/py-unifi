# openapi_client.SettingPortaApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_porta**](SettingPortaApi.md#get_setting_porta) | **GET** /get/setting/porta | 
[**update_setting_porta**](SettingPortaApi.md#update_setting_porta) | **PUT** /set/setting/porta | 


# **get_setting_porta**
> SettingPortaResponse get_setting_porta()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_porta_response import SettingPortaResponse
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
    api_instance = openapi_client.SettingPortaApi(api_client)

    try:
        api_response = api_instance.get_setting_porta()
        print("The response of SettingPortaApi->get_setting_porta:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingPortaApi->get_setting_porta: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingPortaResponse**](SettingPortaResponse.md)

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

# **update_setting_porta**
> SettingPortaResponse update_setting_porta(setting_porta=setting_porta)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_porta import SettingPorta
from openapi_client.models.setting_porta_response import SettingPortaResponse
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
    api_instance = openapi_client.SettingPortaApi(api_client)
    setting_porta = openapi_client.SettingPorta() # SettingPorta |  (optional)

    try:
        api_response = api_instance.update_setting_porta(setting_porta=setting_porta)
        print("The response of SettingPortaApi->update_setting_porta:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingPortaApi->update_setting_porta: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_porta** | [**SettingPorta**](SettingPorta.md)|  | [optional] 

### Return type

[**SettingPortaResponse**](SettingPortaResponse.md)

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

