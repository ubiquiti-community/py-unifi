# openapi_client.SettingSuperIdentityApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_super_identity**](SettingSuperIdentityApi.md#get_setting_super_identity) | **GET** /get/setting/super_identity | 
[**update_setting_super_identity**](SettingSuperIdentityApi.md#update_setting_super_identity) | **PUT** /set/setting/super_identity | 


# **get_setting_super_identity**
> SettingSuperIdentityResponse get_setting_super_identity()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_super_identity_response import SettingSuperIdentityResponse
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
    api_instance = openapi_client.SettingSuperIdentityApi(api_client)

    try:
        api_response = api_instance.get_setting_super_identity()
        print("The response of SettingSuperIdentityApi->get_setting_super_identity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingSuperIdentityApi->get_setting_super_identity: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingSuperIdentityResponse**](SettingSuperIdentityResponse.md)

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

# **update_setting_super_identity**
> SettingSuperIdentityResponse update_setting_super_identity(setting_super_identity=setting_super_identity)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_super_identity import SettingSuperIdentity
from openapi_client.models.setting_super_identity_response import SettingSuperIdentityResponse
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
    api_instance = openapi_client.SettingSuperIdentityApi(api_client)
    setting_super_identity = openapi_client.SettingSuperIdentity() # SettingSuperIdentity |  (optional)

    try:
        api_response = api_instance.update_setting_super_identity(setting_super_identity=setting_super_identity)
        print("The response of SettingSuperIdentityApi->update_setting_super_identity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingSuperIdentityApi->update_setting_super_identity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_super_identity** | [**SettingSuperIdentity**](SettingSuperIdentity.md)|  | [optional] 

### Return type

[**SettingSuperIdentityResponse**](SettingSuperIdentityResponse.md)

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

