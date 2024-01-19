# openapi_client.MapApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_map**](MapApi.md#create_map) | **POST** /rest/map | 
[**delete_map**](MapApi.md#delete_map) | **DELETE** /rest/map/{id} | 
[**get_map**](MapApi.md#get_map) | **GET** /rest/map/{id} | 
[**list_map**](MapApi.md#list_map) | **GET** /rest/map | 
[**update_map**](MapApi.md#update_map) | **PUT** /rest/map/{id} | 


# **create_map**
> MapResponse create_map(map=map)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.map import Map
from openapi_client.models.map_response import MapResponse
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
    api_instance = openapi_client.MapApi(api_client)
    map = openapi_client.Map() # Map |  (optional)

    try:
        api_response = api_instance.create_map(map=map)
        print("The response of MapApi->create_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapApi->create_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map** | [**Map**](Map.md)|  | [optional] 

### Return type

[**MapResponse**](MapResponse.md)

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

# **delete_map**
> MapResponse delete_map(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.map_response import MapResponse
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
    api_instance = openapi_client.MapApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.delete_map(id)
        print("The response of MapApi->delete_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapApi->delete_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**MapResponse**](MapResponse.md)

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

# **get_map**
> MapResponse get_map(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.map_response import MapResponse
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
    api_instance = openapi_client.MapApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_map(id)
        print("The response of MapApi->get_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapApi->get_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**MapResponse**](MapResponse.md)

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

# **list_map**
> MapResponse list_map()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.map_response import MapResponse
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
    api_instance = openapi_client.MapApi(api_client)

    try:
        api_response = api_instance.list_map()
        print("The response of MapApi->list_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapApi->list_map: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MapResponse**](MapResponse.md)

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

# **update_map**
> MapResponse update_map(id, map_update_request=map_update_request)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.map_response import MapResponse
from openapi_client.models.map_update_request import MapUpdateRequest
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
    api_instance = openapi_client.MapApi(api_client)
    id = 'id_example' # str | 
    map_update_request = openapi_client.MapUpdateRequest() # MapUpdateRequest |  (optional)

    try:
        api_response = api_instance.update_map(id, map_update_request=map_update_request)
        print("The response of MapApi->update_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapApi->update_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **map_update_request** | [**MapUpdateRequest**](MapUpdateRequest.md)|  | [optional] 

### Return type

[**MapResponse**](MapResponse.md)

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

