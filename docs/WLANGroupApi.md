# unifi_client.WLANGroupApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_wlan_group**](WLANGroupApi.md#create_wlan_group) | **POST** /rest/wlangroup | 
[**delete_wlan_group**](WLANGroupApi.md#delete_wlan_group) | **DELETE** /rest/wlangroup/{id} | 
[**get_wlan_group**](WLANGroupApi.md#get_wlan_group) | **GET** /rest/wlangroup/{id} | 
[**list_wlan_group**](WLANGroupApi.md#list_wlan_group) | **GET** /rest/wlangroup | 
[**update_wlan_group**](WLANGroupApi.md#update_wlan_group) | **PUT** /rest/wlangroup/{id} | 


# **create_wlan_group**
> WLANGroupResponse create_wlan_group(wlan_group=wlan_group)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.wlan_group import WLANGroup
from unifi_client.models.wlan_group_response import WLANGroupResponse
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
    api_instance = unifi_client.WLANGroupApi(api_client)
    wlan_group = unifi_client.WLANGroup() # WLANGroup |  (optional)

    try:
        api_response = await api_instance.create_wlan_group(wlan_group=wlan_group)
        print("The response of WLANGroupApi->create_wlan_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WLANGroupApi->create_wlan_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wlan_group** | [**WLANGroup**](WLANGroup.md)|  | [optional] 

### Return type

[**WLANGroupResponse**](WLANGroupResponse.md)

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

# **delete_wlan_group**
> WLANGroupResponse delete_wlan_group(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.wlan_group_response import WLANGroupResponse
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
    api_instance = unifi_client.WLANGroupApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.delete_wlan_group(id)
        print("The response of WLANGroupApi->delete_wlan_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WLANGroupApi->delete_wlan_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WLANGroupResponse**](WLANGroupResponse.md)

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

# **get_wlan_group**
> WLANGroupResponse get_wlan_group(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.wlan_group_response import WLANGroupResponse
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
    api_instance = unifi_client.WLANGroupApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.get_wlan_group(id)
        print("The response of WLANGroupApi->get_wlan_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WLANGroupApi->get_wlan_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WLANGroupResponse**](WLANGroupResponse.md)

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

# **list_wlan_group**
> WLANGroupResponse list_wlan_group()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.wlan_group_response import WLANGroupResponse
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
    api_instance = unifi_client.WLANGroupApi(api_client)

    try:
        api_response = await api_instance.list_wlan_group()
        print("The response of WLANGroupApi->list_wlan_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WLANGroupApi->list_wlan_group: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WLANGroupResponse**](WLANGroupResponse.md)

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

# **update_wlan_group**
> WLANGroupResponse update_wlan_group(id, wlan_group_update_request=wlan_group_update_request)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.wlan_group_response import WLANGroupResponse
from unifi_client.models.wlan_group_update_request import WLANGroupUpdateRequest
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
    api_instance = unifi_client.WLANGroupApi(api_client)
    id = 'id_example' # str | 
    wlan_group_update_request = unifi_client.WLANGroupUpdateRequest() # WLANGroupUpdateRequest |  (optional)

    try:
        api_response = await api_instance.update_wlan_group(id, wlan_group_update_request=wlan_group_update_request)
        print("The response of WLANGroupApi->update_wlan_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WLANGroupApi->update_wlan_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **wlan_group_update_request** | [**WLANGroupUpdateRequest**](WLANGroupUpdateRequest.md)|  | [optional] 

### Return type

[**WLANGroupResponse**](WLANGroupResponse.md)

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

