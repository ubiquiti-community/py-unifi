# openapi_client.SettingSuperCloudaccessApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_super_cloudaccess**](SettingSuperCloudaccessApi.md#get_setting_super_cloudaccess) | **GET** /get/setting/super_cloudaccess | 
[**update_setting_super_cloudaccess**](SettingSuperCloudaccessApi.md#update_setting_super_cloudaccess) | **PUT** /set/setting/super_cloudaccess | 


# **get_setting_super_cloudaccess**
> SettingSuperCloudaccessResponse get_setting_super_cloudaccess()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_super_cloudaccess_response import SettingSuperCloudaccessResponse
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
    api_instance = openapi_client.SettingSuperCloudaccessApi(api_client)

    try:
        api_response = api_instance.get_setting_super_cloudaccess()
        print("The response of SettingSuperCloudaccessApi->get_setting_super_cloudaccess:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingSuperCloudaccessApi->get_setting_super_cloudaccess: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingSuperCloudaccessResponse**](SettingSuperCloudaccessResponse.md)

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

# **update_setting_super_cloudaccess**
> SettingSuperCloudaccessResponse update_setting_super_cloudaccess(setting_super_cloudaccess=setting_super_cloudaccess)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_super_cloudaccess import SettingSuperCloudaccess
from openapi_client.models.setting_super_cloudaccess_response import SettingSuperCloudaccessResponse
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
    api_instance = openapi_client.SettingSuperCloudaccessApi(api_client)
    setting_super_cloudaccess = openapi_client.SettingSuperCloudaccess() # SettingSuperCloudaccess |  (optional)

    try:
        api_response = api_instance.update_setting_super_cloudaccess(setting_super_cloudaccess=setting_super_cloudaccess)
        print("The response of SettingSuperCloudaccessApi->update_setting_super_cloudaccess:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingSuperCloudaccessApi->update_setting_super_cloudaccess: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_super_cloudaccess** | [**SettingSuperCloudaccess**](SettingSuperCloudaccess.md)|  | [optional] 

### Return type

[**SettingSuperCloudaccessResponse**](SettingSuperCloudaccessResponse.md)

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

