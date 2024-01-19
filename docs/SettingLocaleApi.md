# unifi_client.SettingLocaleApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_locale**](SettingLocaleApi.md#get_setting_locale) | **GET** /get/setting/locale | 
[**update_setting_locale**](SettingLocaleApi.md#update_setting_locale) | **PUT** /set/setting/locale | 


# **get_setting_locale**
> SettingLocaleResponse get_setting_locale()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_locale_response import SettingLocaleResponse
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
    api_instance = unifi_client.SettingLocaleApi(api_client)

    try:
        api_response = await api_instance.get_setting_locale()
        print("The response of SettingLocaleApi->get_setting_locale:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingLocaleApi->get_setting_locale: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingLocaleResponse**](SettingLocaleResponse.md)

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

# **update_setting_locale**
> SettingLocaleResponse update_setting_locale(setting_locale=setting_locale)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_locale import SettingLocale
from unifi_client.models.setting_locale_response import SettingLocaleResponse
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
    api_instance = unifi_client.SettingLocaleApi(api_client)
    setting_locale = unifi_client.SettingLocale() # SettingLocale |  (optional)

    try:
        api_response = await api_instance.update_setting_locale(setting_locale=setting_locale)
        print("The response of SettingLocaleApi->update_setting_locale:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingLocaleApi->update_setting_locale: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_locale** | [**SettingLocale**](SettingLocale.md)|  | [optional] 

### Return type

[**SettingLocaleResponse**](SettingLocaleResponse.md)

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

