# unifi_client.SettingSuperSdnApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_super_sdn**](SettingSuperSdnApi.md#get_setting_super_sdn) | **GET** /get/setting/super_sdn | 
[**update_setting_super_sdn**](SettingSuperSdnApi.md#update_setting_super_sdn) | **PUT** /set/setting/super_sdn | 


# **get_setting_super_sdn**
> SettingSuperSdnResponse get_setting_super_sdn()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_super_sdn_response import SettingSuperSdnResponse
from unifi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://unifi.ui.com/proxy/network/api/s/default
# See configuration.py for a list of all supported configuration parameters.
configuration = unifi_client.Configuration(
    host = "https://unifi.ui.com/proxy/network/api/s/default"
)


# Enter a context with an instance of the API client
async with unifi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = unifi_client.SettingSuperSdnApi(api_client)

    try:
        api_response = await api_instance.get_setting_super_sdn()
        print("The response of SettingSuperSdnApi->get_setting_super_sdn:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingSuperSdnApi->get_setting_super_sdn: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingSuperSdnResponse**](SettingSuperSdnResponse.md)

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

# **update_setting_super_sdn**
> SettingSuperSdnResponse update_setting_super_sdn(setting_super_sdn=setting_super_sdn)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_super_sdn import SettingSuperSdn
from unifi_client.models.setting_super_sdn_response import SettingSuperSdnResponse
from unifi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://unifi.ui.com/proxy/network/api/s/default
# See configuration.py for a list of all supported configuration parameters.
configuration = unifi_client.Configuration(
    host = "https://unifi.ui.com/proxy/network/api/s/default"
)


# Enter a context with an instance of the API client
async with unifi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = unifi_client.SettingSuperSdnApi(api_client)
    setting_super_sdn = unifi_client.SettingSuperSdn() # SettingSuperSdn |  (optional)

    try:
        api_response = await api_instance.update_setting_super_sdn(setting_super_sdn=setting_super_sdn)
        print("The response of SettingSuperSdnApi->update_setting_super_sdn:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingSuperSdnApi->update_setting_super_sdn: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_super_sdn** | [**SettingSuperSdn**](SettingSuperSdn.md)|  | [optional] 

### Return type

[**SettingSuperSdnResponse**](SettingSuperSdnResponse.md)

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

