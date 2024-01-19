# unifi_client.BroadcastGroupApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_broadcast_group**](BroadcastGroupApi.md#create_broadcast_group) | **POST** /rest/broadcastgroup | 
[**delete_broadcast_group**](BroadcastGroupApi.md#delete_broadcast_group) | **DELETE** /rest/broadcastgroup/{id} | 
[**get_broadcast_group**](BroadcastGroupApi.md#get_broadcast_group) | **GET** /rest/broadcastgroup/{id} | 
[**list_broadcast_group**](BroadcastGroupApi.md#list_broadcast_group) | **GET** /rest/broadcastgroup | 
[**update_broadcast_group**](BroadcastGroupApi.md#update_broadcast_group) | **PUT** /rest/broadcastgroup/{id} | 


# **create_broadcast_group**
> BroadcastGroupResponse create_broadcast_group(broadcast_group=broadcast_group)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.broadcast_group import BroadcastGroup
from unifi_client.models.broadcast_group_response import BroadcastGroupResponse
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
    api_instance = unifi_client.BroadcastGroupApi(api_client)
    broadcast_group = unifi_client.BroadcastGroup() # BroadcastGroup |  (optional)

    try:
        api_response = await api_instance.create_broadcast_group(broadcast_group=broadcast_group)
        print("The response of BroadcastGroupApi->create_broadcast_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BroadcastGroupApi->create_broadcast_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broadcast_group** | [**BroadcastGroup**](BroadcastGroup.md)|  | [optional] 

### Return type

[**BroadcastGroupResponse**](BroadcastGroupResponse.md)

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

# **delete_broadcast_group**
> BroadcastGroupResponse delete_broadcast_group(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.broadcast_group_response import BroadcastGroupResponse
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
    api_instance = unifi_client.BroadcastGroupApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.delete_broadcast_group(id)
        print("The response of BroadcastGroupApi->delete_broadcast_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BroadcastGroupApi->delete_broadcast_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BroadcastGroupResponse**](BroadcastGroupResponse.md)

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

# **get_broadcast_group**
> BroadcastGroupResponse get_broadcast_group(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.broadcast_group_response import BroadcastGroupResponse
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
    api_instance = unifi_client.BroadcastGroupApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.get_broadcast_group(id)
        print("The response of BroadcastGroupApi->get_broadcast_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BroadcastGroupApi->get_broadcast_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BroadcastGroupResponse**](BroadcastGroupResponse.md)

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

# **list_broadcast_group**
> BroadcastGroupResponse list_broadcast_group()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.broadcast_group_response import BroadcastGroupResponse
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
    api_instance = unifi_client.BroadcastGroupApi(api_client)

    try:
        api_response = await api_instance.list_broadcast_group()
        print("The response of BroadcastGroupApi->list_broadcast_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BroadcastGroupApi->list_broadcast_group: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BroadcastGroupResponse**](BroadcastGroupResponse.md)

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

# **update_broadcast_group**
> BroadcastGroupResponse update_broadcast_group(id, broadcast_group_update_request=broadcast_group_update_request)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.broadcast_group_response import BroadcastGroupResponse
from unifi_client.models.broadcast_group_update_request import BroadcastGroupUpdateRequest
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
    api_instance = unifi_client.BroadcastGroupApi(api_client)
    id = 'id_example' # str | 
    broadcast_group_update_request = unifi_client.BroadcastGroupUpdateRequest() # BroadcastGroupUpdateRequest |  (optional)

    try:
        api_response = await api_instance.update_broadcast_group(id, broadcast_group_update_request=broadcast_group_update_request)
        print("The response of BroadcastGroupApi->update_broadcast_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BroadcastGroupApi->update_broadcast_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **broadcast_group_update_request** | [**BroadcastGroupUpdateRequest**](BroadcastGroupUpdateRequest.md)|  | [optional] 

### Return type

[**BroadcastGroupResponse**](BroadcastGroupResponse.md)

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

