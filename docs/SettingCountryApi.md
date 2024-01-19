# openapi_client.SettingCountryApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_country**](SettingCountryApi.md#get_setting_country) | **GET** /get/setting/country | 
[**update_setting_country**](SettingCountryApi.md#update_setting_country) | **PUT** /set/setting/country | 


# **get_setting_country**
> SettingCountryResponse get_setting_country()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_country_response import SettingCountryResponse
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
    api_instance = openapi_client.SettingCountryApi(api_client)

    try:
        api_response = api_instance.get_setting_country()
        print("The response of SettingCountryApi->get_setting_country:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingCountryApi->get_setting_country: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingCountryResponse**](SettingCountryResponse.md)

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

# **update_setting_country**
> SettingCountryResponse update_setting_country(setting_country=setting_country)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_country import SettingCountry
from openapi_client.models.setting_country_response import SettingCountryResponse
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
    api_instance = openapi_client.SettingCountryApi(api_client)
    setting_country = openapi_client.SettingCountry() # SettingCountry |  (optional)

    try:
        api_response = api_instance.update_setting_country(setting_country=setting_country)
        print("The response of SettingCountryApi->update_setting_country:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingCountryApi->update_setting_country: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_country** | [**SettingCountry**](SettingCountry.md)|  | [optional] 

### Return type

[**SettingCountryResponse**](SettingCountryResponse.md)

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

