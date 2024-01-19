# openapi_client.HeatMapPointApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_heat_map_point**](HeatMapPointApi.md#create_heat_map_point) | **POST** /rest/heatmappoint | 
[**delete_heat_map_point**](HeatMapPointApi.md#delete_heat_map_point) | **DELETE** /rest/heatmappoint/{id} | 
[**get_heat_map_point**](HeatMapPointApi.md#get_heat_map_point) | **GET** /rest/heatmappoint/{id} | 
[**list_heat_map_point**](HeatMapPointApi.md#list_heat_map_point) | **GET** /rest/heatmappoint | 
[**update_heat_map_point**](HeatMapPointApi.md#update_heat_map_point) | **PUT** /rest/heatmappoint/{id} | 


# **create_heat_map_point**
> HeatMapPointResponse create_heat_map_point(heat_map_point=heat_map_point)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.heat_map_point import HeatMapPoint
from openapi_client.models.heat_map_point_response import HeatMapPointResponse
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
    api_instance = openapi_client.HeatMapPointApi(api_client)
    heat_map_point = openapi_client.HeatMapPoint() # HeatMapPoint |  (optional)

    try:
        api_response = api_instance.create_heat_map_point(heat_map_point=heat_map_point)
        print("The response of HeatMapPointApi->create_heat_map_point:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeatMapPointApi->create_heat_map_point: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **heat_map_point** | [**HeatMapPoint**](HeatMapPoint.md)|  | [optional] 

### Return type

[**HeatMapPointResponse**](HeatMapPointResponse.md)

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

# **delete_heat_map_point**
> HeatMapPointResponse delete_heat_map_point(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.heat_map_point_response import HeatMapPointResponse
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
    api_instance = openapi_client.HeatMapPointApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.delete_heat_map_point(id)
        print("The response of HeatMapPointApi->delete_heat_map_point:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeatMapPointApi->delete_heat_map_point: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**HeatMapPointResponse**](HeatMapPointResponse.md)

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

# **get_heat_map_point**
> HeatMapPointResponse get_heat_map_point(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.heat_map_point_response import HeatMapPointResponse
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
    api_instance = openapi_client.HeatMapPointApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_heat_map_point(id)
        print("The response of HeatMapPointApi->get_heat_map_point:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeatMapPointApi->get_heat_map_point: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**HeatMapPointResponse**](HeatMapPointResponse.md)

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

# **list_heat_map_point**
> HeatMapPointResponse list_heat_map_point()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.heat_map_point_response import HeatMapPointResponse
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
    api_instance = openapi_client.HeatMapPointApi(api_client)

    try:
        api_response = api_instance.list_heat_map_point()
        print("The response of HeatMapPointApi->list_heat_map_point:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeatMapPointApi->list_heat_map_point: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HeatMapPointResponse**](HeatMapPointResponse.md)

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

# **update_heat_map_point**
> HeatMapPointResponse update_heat_map_point(id, heat_map_point_update_request=heat_map_point_update_request)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.heat_map_point_response import HeatMapPointResponse
from openapi_client.models.heat_map_point_update_request import HeatMapPointUpdateRequest
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
    api_instance = openapi_client.HeatMapPointApi(api_client)
    id = 'id_example' # str | 
    heat_map_point_update_request = openapi_client.HeatMapPointUpdateRequest() # HeatMapPointUpdateRequest |  (optional)

    try:
        api_response = api_instance.update_heat_map_point(id, heat_map_point_update_request=heat_map_point_update_request)
        print("The response of HeatMapPointApi->update_heat_map_point:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeatMapPointApi->update_heat_map_point: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **heat_map_point_update_request** | [**HeatMapPointUpdateRequest**](HeatMapPointUpdateRequest.md)|  | [optional] 

### Return type

[**HeatMapPointResponse**](HeatMapPointResponse.md)

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

