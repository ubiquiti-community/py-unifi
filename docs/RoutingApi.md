# unifi_client.RoutingApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_routing**](RoutingApi.md#create_routing) | **POST** /rest/routing | 
[**delete_routing**](RoutingApi.md#delete_routing) | **DELETE** /rest/routing/{id} | 
[**get_routing**](RoutingApi.md#get_routing) | **GET** /rest/routing/{id} | 
[**list_routing**](RoutingApi.md#list_routing) | **GET** /rest/routing | 
[**update_routing**](RoutingApi.md#update_routing) | **PUT** /rest/routing/{id} | 


# **create_routing**
> RoutingResponse create_routing(routing=routing)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.routing import Routing
from unifi_client.models.routing_response import RoutingResponse
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
    api_instance = unifi_client.RoutingApi(api_client)
    routing = unifi_client.Routing() # Routing |  (optional)

    try:
        api_response = await api_instance.create_routing(routing=routing)
        print("The response of RoutingApi->create_routing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingApi->create_routing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **routing** | [**Routing**](Routing.md)|  | [optional] 

### Return type

[**RoutingResponse**](RoutingResponse.md)

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

# **delete_routing**
> RoutingResponse delete_routing(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.routing_response import RoutingResponse
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
    api_instance = unifi_client.RoutingApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.delete_routing(id)
        print("The response of RoutingApi->delete_routing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingApi->delete_routing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**RoutingResponse**](RoutingResponse.md)

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

# **get_routing**
> RoutingResponse get_routing(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.routing_response import RoutingResponse
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
    api_instance = unifi_client.RoutingApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.get_routing(id)
        print("The response of RoutingApi->get_routing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingApi->get_routing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**RoutingResponse**](RoutingResponse.md)

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

# **list_routing**
> RoutingResponse list_routing()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.routing_response import RoutingResponse
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
    api_instance = unifi_client.RoutingApi(api_client)

    try:
        api_response = await api_instance.list_routing()
        print("The response of RoutingApi->list_routing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingApi->list_routing: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RoutingResponse**](RoutingResponse.md)

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

# **update_routing**
> RoutingResponse update_routing(id, routing_update_request=routing_update_request)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.routing_response import RoutingResponse
from unifi_client.models.routing_update_request import RoutingUpdateRequest
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
    api_instance = unifi_client.RoutingApi(api_client)
    id = 'id_example' # str | 
    routing_update_request = unifi_client.RoutingUpdateRequest() # RoutingUpdateRequest |  (optional)

    try:
        api_response = await api_instance.update_routing(id, routing_update_request=routing_update_request)
        print("The response of RoutingApi->update_routing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingApi->update_routing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **routing_update_request** | [**RoutingUpdateRequest**](RoutingUpdateRequest.md)|  | [optional] 

### Return type

[**RoutingResponse**](RoutingResponse.md)

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

