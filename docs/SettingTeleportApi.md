# openapi_client.SettingTeleportApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_teleport**](SettingTeleportApi.md#get_setting_teleport) | **GET** /get/setting/teleport | 
[**update_setting_teleport**](SettingTeleportApi.md#update_setting_teleport) | **PUT** /set/setting/teleport | 


# **get_setting_teleport**
> SettingTeleportResponse get_setting_teleport()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_teleport_response import SettingTeleportResponse
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
    api_instance = openapi_client.SettingTeleportApi(api_client)

    try:
        api_response = api_instance.get_setting_teleport()
        print("The response of SettingTeleportApi->get_setting_teleport:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingTeleportApi->get_setting_teleport: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingTeleportResponse**](SettingTeleportResponse.md)

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

# **update_setting_teleport**
> SettingTeleportResponse update_setting_teleport(setting_teleport=setting_teleport)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_teleport import SettingTeleport
from openapi_client.models.setting_teleport_response import SettingTeleportResponse
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
    api_instance = openapi_client.SettingTeleportApi(api_client)
    setting_teleport = openapi_client.SettingTeleport() # SettingTeleport |  (optional)

    try:
        api_response = api_instance.update_setting_teleport(setting_teleport=setting_teleport)
        print("The response of SettingTeleportApi->update_setting_teleport:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingTeleportApi->update_setting_teleport: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_teleport** | [**SettingTeleport**](SettingTeleport.md)|  | [optional] 

### Return type

[**SettingTeleportResponse**](SettingTeleportResponse.md)

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

