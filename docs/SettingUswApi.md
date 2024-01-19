# openapi_client.SettingUswApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_usw**](SettingUswApi.md#get_setting_usw) | **GET** /get/setting/usw | 
[**update_setting_usw**](SettingUswApi.md#update_setting_usw) | **PUT** /set/setting/usw | 


# **get_setting_usw**
> SettingUswResponse get_setting_usw()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_usw_response import SettingUswResponse
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
    api_instance = openapi_client.SettingUswApi(api_client)

    try:
        api_response = api_instance.get_setting_usw()
        print("The response of SettingUswApi->get_setting_usw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingUswApi->get_setting_usw: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingUswResponse**](SettingUswResponse.md)

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

# **update_setting_usw**
> SettingUswResponse update_setting_usw(setting_usw=setting_usw)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_usw import SettingUsw
from openapi_client.models.setting_usw_response import SettingUswResponse
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
    api_instance = openapi_client.SettingUswApi(api_client)
    setting_usw = openapi_client.SettingUsw() # SettingUsw |  (optional)

    try:
        api_response = api_instance.update_setting_usw(setting_usw=setting_usw)
        print("The response of SettingUswApi->update_setting_usw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingUswApi->update_setting_usw: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_usw** | [**SettingUsw**](SettingUsw.md)|  | [optional] 

### Return type

[**SettingUswResponse**](SettingUswResponse.md)

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

