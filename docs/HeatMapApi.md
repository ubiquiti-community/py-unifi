# unifi_client.HeatMapApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_heat_map**](HeatMapApi.md#create_heat_map) | **POST** /rest/heatmap | 
[**delete_heat_map**](HeatMapApi.md#delete_heat_map) | **DELETE** /rest/heatmap/{id} | 
[**get_heat_map**](HeatMapApi.md#get_heat_map) | **GET** /rest/heatmap/{id} | 
[**list_heat_map**](HeatMapApi.md#list_heat_map) | **GET** /rest/heatmap | 
[**update_heat_map**](HeatMapApi.md#update_heat_map) | **PUT** /rest/heatmap/{id} | 


# **create_heat_map**
> HeatMapResponse create_heat_map(heat_map=heat_map)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.heat_map import HeatMap
from unifi_client.models.heat_map_response import HeatMapResponse
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
    api_instance = unifi_client.HeatMapApi(api_client)
    heat_map = unifi_client.HeatMap() # HeatMap |  (optional)

    try:
        api_response = await api_instance.create_heat_map(heat_map=heat_map)
        print("The response of HeatMapApi->create_heat_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeatMapApi->create_heat_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **heat_map** | [**HeatMap**](HeatMap.md)|  | [optional] 

### Return type

[**HeatMapResponse**](HeatMapResponse.md)

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

# **delete_heat_map**
> HeatMapResponse delete_heat_map(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.heat_map_response import HeatMapResponse
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
    api_instance = unifi_client.HeatMapApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.delete_heat_map(id)
        print("The response of HeatMapApi->delete_heat_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeatMapApi->delete_heat_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**HeatMapResponse**](HeatMapResponse.md)

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

# **get_heat_map**
> HeatMapResponse get_heat_map(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.heat_map_response import HeatMapResponse
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
    api_instance = unifi_client.HeatMapApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.get_heat_map(id)
        print("The response of HeatMapApi->get_heat_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeatMapApi->get_heat_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**HeatMapResponse**](HeatMapResponse.md)

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

# **list_heat_map**
> HeatMapResponse list_heat_map()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.heat_map_response import HeatMapResponse
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
    api_instance = unifi_client.HeatMapApi(api_client)

    try:
        api_response = await api_instance.list_heat_map()
        print("The response of HeatMapApi->list_heat_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeatMapApi->list_heat_map: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HeatMapResponse**](HeatMapResponse.md)

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

# **update_heat_map**
> HeatMapResponse update_heat_map(id, heat_map_update_request=heat_map_update_request)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.heat_map_response import HeatMapResponse
from unifi_client.models.heat_map_update_request import HeatMapUpdateRequest
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
    api_instance = unifi_client.HeatMapApi(api_client)
    id = 'id_example' # str | 
    heat_map_update_request = unifi_client.HeatMapUpdateRequest() # HeatMapUpdateRequest |  (optional)

    try:
        api_response = await api_instance.update_heat_map(id, heat_map_update_request=heat_map_update_request)
        print("The response of HeatMapApi->update_heat_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeatMapApi->update_heat_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **heat_map_update_request** | [**HeatMapUpdateRequest**](HeatMapUpdateRequest.md)|  | [optional] 

### Return type

[**HeatMapResponse**](HeatMapResponse.md)

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

