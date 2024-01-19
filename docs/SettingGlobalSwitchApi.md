# openapi_client.SettingGlobalSwitchApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_global_switch**](SettingGlobalSwitchApi.md#get_setting_global_switch) | **GET** /get/setting/global_switch | 
[**update_setting_global_switch**](SettingGlobalSwitchApi.md#update_setting_global_switch) | **PUT** /set/setting/global_switch | 


# **get_setting_global_switch**
> SettingGlobalSwitchResponse get_setting_global_switch()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_global_switch_response import SettingGlobalSwitchResponse
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
    api_instance = openapi_client.SettingGlobalSwitchApi(api_client)

    try:
        api_response = api_instance.get_setting_global_switch()
        print("The response of SettingGlobalSwitchApi->get_setting_global_switch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingGlobalSwitchApi->get_setting_global_switch: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingGlobalSwitchResponse**](SettingGlobalSwitchResponse.md)

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

# **update_setting_global_switch**
> SettingGlobalSwitchResponse update_setting_global_switch(setting_global_switch=setting_global_switch)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_global_switch import SettingGlobalSwitch
from openapi_client.models.setting_global_switch_response import SettingGlobalSwitchResponse
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
    api_instance = openapi_client.SettingGlobalSwitchApi(api_client)
    setting_global_switch = openapi_client.SettingGlobalSwitch() # SettingGlobalSwitch |  (optional)

    try:
        api_response = api_instance.update_setting_global_switch(setting_global_switch=setting_global_switch)
        print("The response of SettingGlobalSwitchApi->update_setting_global_switch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingGlobalSwitchApi->update_setting_global_switch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_global_switch** | [**SettingGlobalSwitch**](SettingGlobalSwitch.md)|  | [optional] 

### Return type

[**SettingGlobalSwitchResponse**](SettingGlobalSwitchResponse.md)

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

