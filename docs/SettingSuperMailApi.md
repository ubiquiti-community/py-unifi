# unifi_client.SettingSuperMailApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_super_mail**](SettingSuperMailApi.md#get_setting_super_mail) | **GET** /get/setting/super_mail | 
[**update_setting_super_mail**](SettingSuperMailApi.md#update_setting_super_mail) | **PUT** /set/setting/super_mail | 


# **get_setting_super_mail**
> SettingSuperMailResponse get_setting_super_mail()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_super_mail_response import SettingSuperMailResponse
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
    api_instance = unifi_client.SettingSuperMailApi(api_client)

    try:
        api_response = await api_instance.get_setting_super_mail()
        print("The response of SettingSuperMailApi->get_setting_super_mail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingSuperMailApi->get_setting_super_mail: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingSuperMailResponse**](SettingSuperMailResponse.md)

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

# **update_setting_super_mail**
> SettingSuperMailResponse update_setting_super_mail(setting_super_mail=setting_super_mail)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_super_mail import SettingSuperMail
from unifi_client.models.setting_super_mail_response import SettingSuperMailResponse
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
    api_instance = unifi_client.SettingSuperMailApi(api_client)
    setting_super_mail = unifi_client.SettingSuperMail() # SettingSuperMail |  (optional)

    try:
        api_response = await api_instance.update_setting_super_mail(setting_super_mail=setting_super_mail)
        print("The response of SettingSuperMailApi->update_setting_super_mail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingSuperMailApi->update_setting_super_mail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_super_mail** | [**SettingSuperMail**](SettingSuperMail.md)|  | [optional] 

### Return type

[**SettingSuperMailResponse**](SettingSuperMailResponse.md)

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

