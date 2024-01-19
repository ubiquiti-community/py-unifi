# openapi_client.SettingDohApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_doh**](SettingDohApi.md#get_setting_doh) | **GET** /get/setting/doh | 
[**update_setting_doh**](SettingDohApi.md#update_setting_doh) | **PUT** /set/setting/doh | 


# **get_setting_doh**
> SettingDohResponse get_setting_doh()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_doh_response import SettingDohResponse
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
    api_instance = openapi_client.SettingDohApi(api_client)

    try:
        api_response = api_instance.get_setting_doh()
        print("The response of SettingDohApi->get_setting_doh:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingDohApi->get_setting_doh: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingDohResponse**](SettingDohResponse.md)

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

# **update_setting_doh**
> SettingDohResponse update_setting_doh(setting_doh=setting_doh)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_doh import SettingDoh
from openapi_client.models.setting_doh_response import SettingDohResponse
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
    api_instance = openapi_client.SettingDohApi(api_client)
    setting_doh = openapi_client.SettingDoh() # SettingDoh |  (optional)

    try:
        api_response = api_instance.update_setting_doh(setting_doh=setting_doh)
        print("The response of SettingDohApi->update_setting_doh:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingDohApi->update_setting_doh: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_doh** | [**SettingDoh**](SettingDoh.md)|  | [optional] 

### Return type

[**SettingDohResponse**](SettingDohResponse.md)

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

