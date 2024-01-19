# unifi_client.SettingGuestAccessApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_guest_access**](SettingGuestAccessApi.md#get_setting_guest_access) | **GET** /get/setting/guest_access | 
[**update_setting_guest_access**](SettingGuestAccessApi.md#update_setting_guest_access) | **PUT** /set/setting/guest_access | 


# **get_setting_guest_access**
> SettingGuestAccessResponse get_setting_guest_access()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_guest_access_response import SettingGuestAccessResponse
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
    api_instance = unifi_client.SettingGuestAccessApi(api_client)

    try:
        api_response = await api_instance.get_setting_guest_access()
        print("The response of SettingGuestAccessApi->get_setting_guest_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingGuestAccessApi->get_setting_guest_access: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingGuestAccessResponse**](SettingGuestAccessResponse.md)

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

# **update_setting_guest_access**
> SettingGuestAccessResponse update_setting_guest_access(setting_guest_access=setting_guest_access)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_guest_access import SettingGuestAccess
from unifi_client.models.setting_guest_access_response import SettingGuestAccessResponse
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
    api_instance = unifi_client.SettingGuestAccessApi(api_client)
    setting_guest_access = unifi_client.SettingGuestAccess() # SettingGuestAccess |  (optional)

    try:
        api_response = await api_instance.update_setting_guest_access(setting_guest_access=setting_guest_access)
        print("The response of SettingGuestAccessApi->update_setting_guest_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingGuestAccessApi->update_setting_guest_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_guest_access** | [**SettingGuestAccess**](SettingGuestAccess.md)|  | [optional] 

### Return type

[**SettingGuestAccessResponse**](SettingGuestAccessResponse.md)

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

