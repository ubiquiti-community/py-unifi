# openapi_client.SettingMgmtApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_mgmt**](SettingMgmtApi.md#get_setting_mgmt) | **GET** /get/setting/mgmt | 
[**update_setting_mgmt**](SettingMgmtApi.md#update_setting_mgmt) | **PUT** /set/setting/mgmt | 


# **get_setting_mgmt**
> SettingMgmtResponse get_setting_mgmt()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_mgmt_response import SettingMgmtResponse
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
    api_instance = openapi_client.SettingMgmtApi(api_client)

    try:
        api_response = api_instance.get_setting_mgmt()
        print("The response of SettingMgmtApi->get_setting_mgmt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingMgmtApi->get_setting_mgmt: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingMgmtResponse**](SettingMgmtResponse.md)

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

# **update_setting_mgmt**
> SettingMgmtResponse update_setting_mgmt(setting_mgmt=setting_mgmt)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_mgmt import SettingMgmt
from openapi_client.models.setting_mgmt_response import SettingMgmtResponse
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
    api_instance = openapi_client.SettingMgmtApi(api_client)
    setting_mgmt = openapi_client.SettingMgmt() # SettingMgmt |  (optional)

    try:
        api_response = api_instance.update_setting_mgmt(setting_mgmt=setting_mgmt)
        print("The response of SettingMgmtApi->update_setting_mgmt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingMgmtApi->update_setting_mgmt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_mgmt** | [**SettingMgmt**](SettingMgmt.md)|  | [optional] 

### Return type

[**SettingMgmtResponse**](SettingMgmtResponse.md)

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

