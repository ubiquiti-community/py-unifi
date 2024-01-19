# openapi_client.NetworkApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_network**](NetworkApi.md#create_network) | **POST** /rest/networkconf | 
[**delete_network**](NetworkApi.md#delete_network) | **DELETE** /rest/networkconf/{id} | 
[**get_network**](NetworkApi.md#get_network) | **GET** /rest/networkconf/{id} | 
[**list_network**](NetworkApi.md#list_network) | **GET** /rest/networkconf | 
[**update_network**](NetworkApi.md#update_network) | **PUT** /rest/networkconf/{id} | 


# **create_network**
> NetworkResponse create_network(network=network)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.network import Network
from openapi_client.models.network_response import NetworkResponse
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
    api_instance = openapi_client.NetworkApi(api_client)
    network = openapi_client.Network() # Network |  (optional)

    try:
        api_response = api_instance.create_network(network=network)
        print("The response of NetworkApi->create_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkApi->create_network: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network** | [**Network**](Network.md)|  | [optional] 

### Return type

[**NetworkResponse**](NetworkResponse.md)

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

# **delete_network**
> NetworkResponse delete_network(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.network_response import NetworkResponse
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
    api_instance = openapi_client.NetworkApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.delete_network(id)
        print("The response of NetworkApi->delete_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkApi->delete_network: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**NetworkResponse**](NetworkResponse.md)

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

# **get_network**
> NetworkResponse get_network(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.network_response import NetworkResponse
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
    api_instance = openapi_client.NetworkApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_network(id)
        print("The response of NetworkApi->get_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkApi->get_network: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**NetworkResponse**](NetworkResponse.md)

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

# **list_network**
> NetworkResponse list_network()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.network_response import NetworkResponse
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
    api_instance = openapi_client.NetworkApi(api_client)

    try:
        api_response = api_instance.list_network()
        print("The response of NetworkApi->list_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkApi->list_network: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NetworkResponse**](NetworkResponse.md)

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

# **update_network**
> NetworkResponse update_network(id, network_update_request=network_update_request)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.network_response import NetworkResponse
from openapi_client.models.network_update_request import NetworkUpdateRequest
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
    api_instance = openapi_client.NetworkApi(api_client)
    id = 'id_example' # str | 
    network_update_request = openapi_client.NetworkUpdateRequest() # NetworkUpdateRequest |  (optional)

    try:
        api_response = api_instance.update_network(id, network_update_request=network_update_request)
        print("The response of NetworkApi->update_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkApi->update_network: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **network_update_request** | [**NetworkUpdateRequest**](NetworkUpdateRequest.md)|  | [optional] 

### Return type

[**NetworkResponse**](NetworkResponse.md)

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

