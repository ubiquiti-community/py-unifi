# openapi_client.SettingUsgApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_usg**](SettingUsgApi.md#get_setting_usg) | **GET** /get/setting/usg | 
[**update_setting_usg**](SettingUsgApi.md#update_setting_usg) | **PUT** /set/setting/usg | 


# **get_setting_usg**
> SettingUsgResponse get_setting_usg()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_usg_response import SettingUsgResponse
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
    api_instance = openapi_client.SettingUsgApi(api_client)

    try:
        api_response = api_instance.get_setting_usg()
        print("The response of SettingUsgApi->get_setting_usg:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingUsgApi->get_setting_usg: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingUsgResponse**](SettingUsgResponse.md)

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

# **update_setting_usg**
> SettingUsgResponse update_setting_usg(setting_usg=setting_usg)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_usg import SettingUsg
from openapi_client.models.setting_usg_response import SettingUsgResponse
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
    api_instance = openapi_client.SettingUsgApi(api_client)
    setting_usg = openapi_client.SettingUsg() # SettingUsg |  (optional)

    try:
        api_response = api_instance.update_setting_usg(setting_usg=setting_usg)
        print("The response of SettingUsgApi->update_setting_usg:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingUsgApi->update_setting_usg: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_usg** | [**SettingUsg**](SettingUsg.md)|  | [optional] 

### Return type

[**SettingUsgResponse**](SettingUsgResponse.md)

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

