# openapi_client.SettingAutoSpeedtestApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_auto_speedtest**](SettingAutoSpeedtestApi.md#get_setting_auto_speedtest) | **GET** /get/setting/auto_speedtest | 
[**update_setting_auto_speedtest**](SettingAutoSpeedtestApi.md#update_setting_auto_speedtest) | **PUT** /set/setting/auto_speedtest | 


# **get_setting_auto_speedtest**
> SettingAutoSpeedtestResponse get_setting_auto_speedtest()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_auto_speedtest_response import SettingAutoSpeedtestResponse
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
    api_instance = openapi_client.SettingAutoSpeedtestApi(api_client)

    try:
        api_response = api_instance.get_setting_auto_speedtest()
        print("The response of SettingAutoSpeedtestApi->get_setting_auto_speedtest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingAutoSpeedtestApi->get_setting_auto_speedtest: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingAutoSpeedtestResponse**](SettingAutoSpeedtestResponse.md)

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

# **update_setting_auto_speedtest**
> SettingAutoSpeedtestResponse update_setting_auto_speedtest(setting_auto_speedtest=setting_auto_speedtest)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_auto_speedtest import SettingAutoSpeedtest
from openapi_client.models.setting_auto_speedtest_response import SettingAutoSpeedtestResponse
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
    api_instance = openapi_client.SettingAutoSpeedtestApi(api_client)
    setting_auto_speedtest = openapi_client.SettingAutoSpeedtest() # SettingAutoSpeedtest |  (optional)

    try:
        api_response = api_instance.update_setting_auto_speedtest(setting_auto_speedtest=setting_auto_speedtest)
        print("The response of SettingAutoSpeedtestApi->update_setting_auto_speedtest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingAutoSpeedtestApi->update_setting_auto_speedtest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_auto_speedtest** | [**SettingAutoSpeedtest**](SettingAutoSpeedtest.md)|  | [optional] 

### Return type

[**SettingAutoSpeedtestResponse**](SettingAutoSpeedtestResponse.md)

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

