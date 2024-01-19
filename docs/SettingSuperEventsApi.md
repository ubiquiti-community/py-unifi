# openapi_client.SettingSuperEventsApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_super_events**](SettingSuperEventsApi.md#get_setting_super_events) | **GET** /get/setting/super_events | 
[**update_setting_super_events**](SettingSuperEventsApi.md#update_setting_super_events) | **PUT** /set/setting/super_events | 


# **get_setting_super_events**
> SettingSuperEventsResponse get_setting_super_events()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_super_events_response import SettingSuperEventsResponse
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
    api_instance = openapi_client.SettingSuperEventsApi(api_client)

    try:
        api_response = api_instance.get_setting_super_events()
        print("The response of SettingSuperEventsApi->get_setting_super_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingSuperEventsApi->get_setting_super_events: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingSuperEventsResponse**](SettingSuperEventsResponse.md)

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

# **update_setting_super_events**
> SettingSuperEventsResponse update_setting_super_events(setting_super_events=setting_super_events)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_super_events import SettingSuperEvents
from openapi_client.models.setting_super_events_response import SettingSuperEventsResponse
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
    api_instance = openapi_client.SettingSuperEventsApi(api_client)
    setting_super_events = openapi_client.SettingSuperEvents() # SettingSuperEvents |  (optional)

    try:
        api_response = api_instance.update_setting_super_events(setting_super_events=setting_super_events)
        print("The response of SettingSuperEventsApi->update_setting_super_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingSuperEventsApi->update_setting_super_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_super_events** | [**SettingSuperEvents**](SettingSuperEvents.md)|  | [optional] 

### Return type

[**SettingSuperEventsResponse**](SettingSuperEventsResponse.md)

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

