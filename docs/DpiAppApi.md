# openapi_client.DpiAppApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dpi_app**](DpiAppApi.md#create_dpi_app) | **POST** /rest/dpiapp | 
[**delete_dpi_app**](DpiAppApi.md#delete_dpi_app) | **DELETE** /rest/dpiapp/{id} | 
[**get_dpi_app**](DpiAppApi.md#get_dpi_app) | **GET** /rest/dpiapp/{id} | 
[**list_dpi_app**](DpiAppApi.md#list_dpi_app) | **GET** /rest/dpiapp | 
[**update_dpi_app**](DpiAppApi.md#update_dpi_app) | **PUT** /rest/dpiapp/{id} | 


# **create_dpi_app**
> DpiAppResponse create_dpi_app(dpi_app=dpi_app)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dpi_app import DpiApp
from openapi_client.models.dpi_app_response import DpiAppResponse
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
    api_instance = openapi_client.DpiAppApi(api_client)
    dpi_app = openapi_client.DpiApp() # DpiApp |  (optional)

    try:
        api_response = api_instance.create_dpi_app(dpi_app=dpi_app)
        print("The response of DpiAppApi->create_dpi_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DpiAppApi->create_dpi_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dpi_app** | [**DpiApp**](DpiApp.md)|  | [optional] 

### Return type

[**DpiAppResponse**](DpiAppResponse.md)

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

# **delete_dpi_app**
> DpiAppResponse delete_dpi_app(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dpi_app_response import DpiAppResponse
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
    api_instance = openapi_client.DpiAppApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.delete_dpi_app(id)
        print("The response of DpiAppApi->delete_dpi_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DpiAppApi->delete_dpi_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DpiAppResponse**](DpiAppResponse.md)

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

# **get_dpi_app**
> DpiAppResponse get_dpi_app(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dpi_app_response import DpiAppResponse
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
    api_instance = openapi_client.DpiAppApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_dpi_app(id)
        print("The response of DpiAppApi->get_dpi_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DpiAppApi->get_dpi_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DpiAppResponse**](DpiAppResponse.md)

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

# **list_dpi_app**
> DpiAppResponse list_dpi_app()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dpi_app_response import DpiAppResponse
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
    api_instance = openapi_client.DpiAppApi(api_client)

    try:
        api_response = api_instance.list_dpi_app()
        print("The response of DpiAppApi->list_dpi_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DpiAppApi->list_dpi_app: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DpiAppResponse**](DpiAppResponse.md)

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

# **update_dpi_app**
> DpiAppResponse update_dpi_app(id, dpi_app_update_request=dpi_app_update_request)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dpi_app_response import DpiAppResponse
from openapi_client.models.dpi_app_update_request import DpiAppUpdateRequest
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
    api_instance = openapi_client.DpiAppApi(api_client)
    id = 'id_example' # str | 
    dpi_app_update_request = openapi_client.DpiAppUpdateRequest() # DpiAppUpdateRequest |  (optional)

    try:
        api_response = api_instance.update_dpi_app(id, dpi_app_update_request=dpi_app_update_request)
        print("The response of DpiAppApi->update_dpi_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DpiAppApi->update_dpi_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **dpi_app_update_request** | [**DpiAppUpdateRequest**](DpiAppUpdateRequest.md)|  | [optional] 

### Return type

[**DpiAppResponse**](DpiAppResponse.md)

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

