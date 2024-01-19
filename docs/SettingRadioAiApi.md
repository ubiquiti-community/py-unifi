# unifi_client.SettingRadioAiApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_radio_ai**](SettingRadioAiApi.md#get_setting_radio_ai) | **GET** /get/setting/radio_ai | 
[**update_setting_radio_ai**](SettingRadioAiApi.md#update_setting_radio_ai) | **PUT** /set/setting/radio_ai | 


# **get_setting_radio_ai**
> SettingRadioAiResponse get_setting_radio_ai()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_radio_ai_response import SettingRadioAiResponse
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
    api_instance = unifi_client.SettingRadioAiApi(api_client)

    try:
        api_response = await api_instance.get_setting_radio_ai()
        print("The response of SettingRadioAiApi->get_setting_radio_ai:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingRadioAiApi->get_setting_radio_ai: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingRadioAiResponse**](SettingRadioAiResponse.md)

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

# **update_setting_radio_ai**
> SettingRadioAiResponse update_setting_radio_ai(setting_radio_ai=setting_radio_ai)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_radio_ai import SettingRadioAi
from unifi_client.models.setting_radio_ai_response import SettingRadioAiResponse
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
    api_instance = unifi_client.SettingRadioAiApi(api_client)
    setting_radio_ai = unifi_client.SettingRadioAi() # SettingRadioAi |  (optional)

    try:
        api_response = await api_instance.update_setting_radio_ai(setting_radio_ai=setting_radio_ai)
        print("The response of SettingRadioAiApi->update_setting_radio_ai:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingRadioAiApi->update_setting_radio_ai: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_radio_ai** | [**SettingRadioAi**](SettingRadioAi.md)|  | [optional] 

### Return type

[**SettingRadioAiResponse**](SettingRadioAiResponse.md)

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

