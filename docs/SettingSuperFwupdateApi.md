# unifi_client.SettingSuperFwupdateApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_super_fwupdate**](SettingSuperFwupdateApi.md#get_setting_super_fwupdate) | **GET** /get/setting/super_fwupdate | 
[**update_setting_super_fwupdate**](SettingSuperFwupdateApi.md#update_setting_super_fwupdate) | **PUT** /set/setting/super_fwupdate | 


# **get_setting_super_fwupdate**
> SettingSuperFwupdateResponse get_setting_super_fwupdate()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_super_fwupdate_response import SettingSuperFwupdateResponse
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
    api_instance = unifi_client.SettingSuperFwupdateApi(api_client)

    try:
        api_response = await api_instance.get_setting_super_fwupdate()
        print("The response of SettingSuperFwupdateApi->get_setting_super_fwupdate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingSuperFwupdateApi->get_setting_super_fwupdate: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingSuperFwupdateResponse**](SettingSuperFwupdateResponse.md)

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

# **update_setting_super_fwupdate**
> SettingSuperFwupdateResponse update_setting_super_fwupdate(setting_super_fwupdate=setting_super_fwupdate)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_super_fwupdate import SettingSuperFwupdate
from unifi_client.models.setting_super_fwupdate_response import SettingSuperFwupdateResponse
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
    api_instance = unifi_client.SettingSuperFwupdateApi(api_client)
    setting_super_fwupdate = unifi_client.SettingSuperFwupdate() # SettingSuperFwupdate |  (optional)

    try:
        api_response = await api_instance.update_setting_super_fwupdate(setting_super_fwupdate=setting_super_fwupdate)
        print("The response of SettingSuperFwupdateApi->update_setting_super_fwupdate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingSuperFwupdateApi->update_setting_super_fwupdate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_super_fwupdate** | [**SettingSuperFwupdate**](SettingSuperFwupdate.md)|  | [optional] 

### Return type

[**SettingSuperFwupdateResponse**](SettingSuperFwupdateResponse.md)

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

