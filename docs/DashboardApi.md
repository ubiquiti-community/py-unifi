# openapi_client.DashboardApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dashboard**](DashboardApi.md#create_dashboard) | **POST** /rest/dashboard | 
[**delete_dashboard**](DashboardApi.md#delete_dashboard) | **DELETE** /rest/dashboard/{id} | 
[**get_dashboard**](DashboardApi.md#get_dashboard) | **GET** /rest/dashboard/{id} | 
[**list_dashboard**](DashboardApi.md#list_dashboard) | **GET** /rest/dashboard | 
[**update_dashboard**](DashboardApi.md#update_dashboard) | **PUT** /rest/dashboard/{id} | 


# **create_dashboard**
> DashboardResponse create_dashboard(dashboard=dashboard)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dashboard import Dashboard
from openapi_client.models.dashboard_response import DashboardResponse
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
    api_instance = openapi_client.DashboardApi(api_client)
    dashboard = openapi_client.Dashboard() # Dashboard |  (optional)

    try:
        api_response = api_instance.create_dashboard(dashboard=dashboard)
        print("The response of DashboardApi->create_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->create_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard** | [**Dashboard**](Dashboard.md)|  | [optional] 

### Return type

[**DashboardResponse**](DashboardResponse.md)

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

# **delete_dashboard**
> DashboardResponse delete_dashboard(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dashboard_response import DashboardResponse
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
    api_instance = openapi_client.DashboardApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.delete_dashboard(id)
        print("The response of DashboardApi->delete_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->delete_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DashboardResponse**](DashboardResponse.md)

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

# **get_dashboard**
> DashboardResponse get_dashboard(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dashboard_response import DashboardResponse
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
    api_instance = openapi_client.DashboardApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_dashboard(id)
        print("The response of DashboardApi->get_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->get_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DashboardResponse**](DashboardResponse.md)

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

# **list_dashboard**
> DashboardResponse list_dashboard()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dashboard_response import DashboardResponse
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
    api_instance = openapi_client.DashboardApi(api_client)

    try:
        api_response = api_instance.list_dashboard()
        print("The response of DashboardApi->list_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->list_dashboard: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DashboardResponse**](DashboardResponse.md)

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

# **update_dashboard**
> DashboardResponse update_dashboard(id, dashboard_update_request=dashboard_update_request)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dashboard_response import DashboardResponse
from openapi_client.models.dashboard_update_request import DashboardUpdateRequest
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
    api_instance = openapi_client.DashboardApi(api_client)
    id = 'id_example' # str | 
    dashboard_update_request = openapi_client.DashboardUpdateRequest() # DashboardUpdateRequest |  (optional)

    try:
        api_response = api_instance.update_dashboard(id, dashboard_update_request=dashboard_update_request)
        print("The response of DashboardApi->update_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->update_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **dashboard_update_request** | [**DashboardUpdateRequest**](DashboardUpdateRequest.md)|  | [optional] 

### Return type

[**DashboardResponse**](DashboardResponse.md)

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

