# unifi_client.PortForwardApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_port_forward**](PortForwardApi.md#create_port_forward) | **POST** /rest/portforward | 
[**delete_port_forward**](PortForwardApi.md#delete_port_forward) | **DELETE** /rest/portforward/{id} | 
[**get_port_forward**](PortForwardApi.md#get_port_forward) | **GET** /rest/portforward/{id} | 
[**list_port_forward**](PortForwardApi.md#list_port_forward) | **GET** /rest/portforward | 
[**update_port_forward**](PortForwardApi.md#update_port_forward) | **PUT** /rest/portforward/{id} | 


# **create_port_forward**
> PortForwardResponse create_port_forward(port_forward=port_forward)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.port_forward import PortForward
from unifi_client.models.port_forward_response import PortForwardResponse
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
    api_instance = unifi_client.PortForwardApi(api_client)
    port_forward = unifi_client.PortForward() # PortForward |  (optional)

    try:
        api_response = await api_instance.create_port_forward(port_forward=port_forward)
        print("The response of PortForwardApi->create_port_forward:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortForwardApi->create_port_forward: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port_forward** | [**PortForward**](PortForward.md)|  | [optional] 

### Return type

[**PortForwardResponse**](PortForwardResponse.md)

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

# **delete_port_forward**
> PortForwardResponse delete_port_forward(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.port_forward_response import PortForwardResponse
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
    api_instance = unifi_client.PortForwardApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.delete_port_forward(id)
        print("The response of PortForwardApi->delete_port_forward:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortForwardApi->delete_port_forward: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PortForwardResponse**](PortForwardResponse.md)

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

# **get_port_forward**
> PortForwardResponse get_port_forward(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.port_forward_response import PortForwardResponse
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
    api_instance = unifi_client.PortForwardApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.get_port_forward(id)
        print("The response of PortForwardApi->get_port_forward:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortForwardApi->get_port_forward: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PortForwardResponse**](PortForwardResponse.md)

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

# **list_port_forward**
> PortForwardResponse list_port_forward()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.port_forward_response import PortForwardResponse
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
    api_instance = unifi_client.PortForwardApi(api_client)

    try:
        api_response = await api_instance.list_port_forward()
        print("The response of PortForwardApi->list_port_forward:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortForwardApi->list_port_forward: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PortForwardResponse**](PortForwardResponse.md)

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

# **update_port_forward**
> PortForwardResponse update_port_forward(id, port_forward_update_request=port_forward_update_request)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.port_forward_response import PortForwardResponse
from unifi_client.models.port_forward_update_request import PortForwardUpdateRequest
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
    api_instance = unifi_client.PortForwardApi(api_client)
    id = 'id_example' # str | 
    port_forward_update_request = unifi_client.PortForwardUpdateRequest() # PortForwardUpdateRequest |  (optional)

    try:
        api_response = await api_instance.update_port_forward(id, port_forward_update_request=port_forward_update_request)
        print("The response of PortForwardApi->update_port_forward:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortForwardApi->update_port_forward: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **port_forward_update_request** | [**PortForwardUpdateRequest**](PortForwardUpdateRequest.md)|  | [optional] 

### Return type

[**PortForwardResponse**](PortForwardResponse.md)

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

