# unifi_client.SettingRsyslogdApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_rsyslogd**](SettingRsyslogdApi.md#get_setting_rsyslogd) | **GET** /get/setting/rsyslogd | 
[**update_setting_rsyslogd**](SettingRsyslogdApi.md#update_setting_rsyslogd) | **PUT** /set/setting/rsyslogd | 


# **get_setting_rsyslogd**
> SettingRsyslogdResponse get_setting_rsyslogd()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_rsyslogd_response import SettingRsyslogdResponse
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
    api_instance = unifi_client.SettingRsyslogdApi(api_client)

    try:
        api_response = await api_instance.get_setting_rsyslogd()
        print("The response of SettingRsyslogdApi->get_setting_rsyslogd:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingRsyslogdApi->get_setting_rsyslogd: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingRsyslogdResponse**](SettingRsyslogdResponse.md)

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

# **update_setting_rsyslogd**
> SettingRsyslogdResponse update_setting_rsyslogd(setting_rsyslogd=setting_rsyslogd)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_rsyslogd import SettingRsyslogd
from unifi_client.models.setting_rsyslogd_response import SettingRsyslogdResponse
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
    api_instance = unifi_client.SettingRsyslogdApi(api_client)
    setting_rsyslogd = unifi_client.SettingRsyslogd() # SettingRsyslogd |  (optional)

    try:
        api_response = await api_instance.update_setting_rsyslogd(setting_rsyslogd=setting_rsyslogd)
        print("The response of SettingRsyslogdApi->update_setting_rsyslogd:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingRsyslogdApi->update_setting_rsyslogd: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_rsyslogd** | [**SettingRsyslogd**](SettingRsyslogd.md)|  | [optional] 

### Return type

[**SettingRsyslogdResponse**](SettingRsyslogdResponse.md)

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

