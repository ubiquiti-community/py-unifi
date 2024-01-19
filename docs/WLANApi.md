# unifi_client.WLANApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_wlan**](WLANApi.md#create_wlan) | **POST** /rest/wlanconf | 
[**delete_wlan**](WLANApi.md#delete_wlan) | **DELETE** /rest/wlanconf/{id} | 
[**get_wlan**](WLANApi.md#get_wlan) | **GET** /rest/wlanconf/{id} | 
[**list_wlan**](WLANApi.md#list_wlan) | **GET** /rest/wlanconf | 
[**update_wlan**](WLANApi.md#update_wlan) | **PUT** /rest/wlanconf/{id} | 


# **create_wlan**
> WLANResponse create_wlan(wlan=wlan)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.wlan import WLAN
from unifi_client.models.wlan_response import WLANResponse
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
    api_instance = unifi_client.WLANApi(api_client)
    wlan = unifi_client.WLAN() # WLAN |  (optional)

    try:
        api_response = await api_instance.create_wlan(wlan=wlan)
        print("The response of WLANApi->create_wlan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WLANApi->create_wlan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wlan** | [**WLAN**](WLAN.md)|  | [optional] 

### Return type

[**WLANResponse**](WLANResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wlan**
> WLANResponse delete_wlan(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.wlan_response import WLANResponse
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
    api_instance = unifi_client.WLANApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.delete_wlan(id)
        print("The response of WLANApi->delete_wlan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WLANApi->delete_wlan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WLANResponse**](WLANResponse.md)

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

# **get_wlan**
> WLANResponse get_wlan(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.wlan_response import WLANResponse
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
    api_instance = unifi_client.WLANApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.get_wlan(id)
        print("The response of WLANApi->get_wlan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WLANApi->get_wlan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WLANResponse**](WLANResponse.md)

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

# **list_wlan**
> WLANResponse list_wlan()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.wlan_response import WLANResponse
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
    api_instance = unifi_client.WLANApi(api_client)

    try:
        api_response = await api_instance.list_wlan()
        print("The response of WLANApi->list_wlan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WLANApi->list_wlan: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WLANResponse**](WLANResponse.md)

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

# **update_wlan**
> WLANResponse update_wlan(id, wlan_update_request=wlan_update_request)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.wlan_response import WLANResponse
from unifi_client.models.wlan_update_request import WLANUpdateRequest
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
    api_instance = unifi_client.WLANApi(api_client)
    id = 'id_example' # str | 
    wlan_update_request = unifi_client.WLANUpdateRequest() # WLANUpdateRequest |  (optional)

    try:
        api_response = await api_instance.update_wlan(id, wlan_update_request=wlan_update_request)
        print("The response of WLANApi->update_wlan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WLANApi->update_wlan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wlan_update_request** | [**WLANUpdateRequest**](WLANUpdateRequest.md)|  | [optional] 

### Return type

[**WLANResponse**](WLANResponse.md)

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

