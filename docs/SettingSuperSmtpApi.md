# openapi_client.SettingSuperSmtpApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_super_smtp**](SettingSuperSmtpApi.md#get_setting_super_smtp) | **GET** /get/setting/super_smtp | 
[**update_setting_super_smtp**](SettingSuperSmtpApi.md#update_setting_super_smtp) | **PUT** /set/setting/super_smtp | 


# **get_setting_super_smtp**
> SettingSuperSmtpResponse get_setting_super_smtp()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_super_smtp_response import SettingSuperSmtpResponse
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
    api_instance = openapi_client.SettingSuperSmtpApi(api_client)

    try:
        api_response = api_instance.get_setting_super_smtp()
        print("The response of SettingSuperSmtpApi->get_setting_super_smtp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingSuperSmtpApi->get_setting_super_smtp: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingSuperSmtpResponse**](SettingSuperSmtpResponse.md)

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

# **update_setting_super_smtp**
> SettingSuperSmtpResponse update_setting_super_smtp(setting_super_smtp=setting_super_smtp)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_super_smtp import SettingSuperSmtp
from openapi_client.models.setting_super_smtp_response import SettingSuperSmtpResponse
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
    api_instance = openapi_client.SettingSuperSmtpApi(api_client)
    setting_super_smtp = openapi_client.SettingSuperSmtp() # SettingSuperSmtp |  (optional)

    try:
        api_response = api_instance.update_setting_super_smtp(setting_super_smtp=setting_super_smtp)
        print("The response of SettingSuperSmtpApi->update_setting_super_smtp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingSuperSmtpApi->update_setting_super_smtp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_super_smtp** | [**SettingSuperSmtp**](SettingSuperSmtp.md)|  | [optional] 

### Return type

[**SettingSuperSmtpResponse**](SettingSuperSmtpResponse.md)

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

