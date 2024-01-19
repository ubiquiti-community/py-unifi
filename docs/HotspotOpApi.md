# openapi_client.HotspotOpApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_hotspot_op**](HotspotOpApi.md#create_hotspot_op) | **POST** /rest/hotspotop | 
[**delete_hotspot_op**](HotspotOpApi.md#delete_hotspot_op) | **DELETE** /rest/hotspotop/{id} | 
[**get_hotspot_op**](HotspotOpApi.md#get_hotspot_op) | **GET** /rest/hotspotop/{id} | 
[**list_hotspot_op**](HotspotOpApi.md#list_hotspot_op) | **GET** /rest/hotspotop | 
[**update_hotspot_op**](HotspotOpApi.md#update_hotspot_op) | **PUT** /rest/hotspotop/{id} | 


# **create_hotspot_op**
> HotspotOpResponse create_hotspot_op(hotspot_op=hotspot_op)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.hotspot_op import HotspotOp
from openapi_client.models.hotspot_op_response import HotspotOpResponse
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
    api_instance = openapi_client.HotspotOpApi(api_client)
    hotspot_op = openapi_client.HotspotOp() # HotspotOp |  (optional)

    try:
        api_response = api_instance.create_hotspot_op(hotspot_op=hotspot_op)
        print("The response of HotspotOpApi->create_hotspot_op:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HotspotOpApi->create_hotspot_op: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hotspot_op** | [**HotspotOp**](HotspotOp.md)|  | [optional] 

### Return type

[**HotspotOpResponse**](HotspotOpResponse.md)

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

# **delete_hotspot_op**
> HotspotOpResponse delete_hotspot_op(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.hotspot_op_response import HotspotOpResponse
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
    api_instance = openapi_client.HotspotOpApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.delete_hotspot_op(id)
        print("The response of HotspotOpApi->delete_hotspot_op:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HotspotOpApi->delete_hotspot_op: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**HotspotOpResponse**](HotspotOpResponse.md)

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

# **get_hotspot_op**
> HotspotOpResponse get_hotspot_op(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.hotspot_op_response import HotspotOpResponse
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
    api_instance = openapi_client.HotspotOpApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_hotspot_op(id)
        print("The response of HotspotOpApi->get_hotspot_op:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HotspotOpApi->get_hotspot_op: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**HotspotOpResponse**](HotspotOpResponse.md)

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

# **list_hotspot_op**
> HotspotOpResponse list_hotspot_op()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.hotspot_op_response import HotspotOpResponse
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
    api_instance = openapi_client.HotspotOpApi(api_client)

    try:
        api_response = api_instance.list_hotspot_op()
        print("The response of HotspotOpApi->list_hotspot_op:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HotspotOpApi->list_hotspot_op: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HotspotOpResponse**](HotspotOpResponse.md)

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

# **update_hotspot_op**
> HotspotOpResponse update_hotspot_op(id, hotspot_op_update_request=hotspot_op_update_request)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.hotspot_op_response import HotspotOpResponse
from openapi_client.models.hotspot_op_update_request import HotspotOpUpdateRequest
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
    api_instance = openapi_client.HotspotOpApi(api_client)
    id = 'id_example' # str | 
    hotspot_op_update_request = openapi_client.HotspotOpUpdateRequest() # HotspotOpUpdateRequest |  (optional)

    try:
        api_response = api_instance.update_hotspot_op(id, hotspot_op_update_request=hotspot_op_update_request)
        print("The response of HotspotOpApi->update_hotspot_op:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HotspotOpApi->update_hotspot_op: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **hotspot_op_update_request** | [**HotspotOpUpdateRequest**](HotspotOpUpdateRequest.md)|  | [optional] 

### Return type

[**HotspotOpResponse**](HotspotOpResponse.md)

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

