# unifi_client.DpiGroupApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dpi_group**](DpiGroupApi.md#create_dpi_group) | **POST** /rest/dpigroup | 
[**delete_dpi_group**](DpiGroupApi.md#delete_dpi_group) | **DELETE** /rest/dpigroup/{id} | 
[**get_dpi_group**](DpiGroupApi.md#get_dpi_group) | **GET** /rest/dpigroup/{id} | 
[**list_dpi_group**](DpiGroupApi.md#list_dpi_group) | **GET** /rest/dpigroup | 
[**update_dpi_group**](DpiGroupApi.md#update_dpi_group) | **PUT** /rest/dpigroup/{id} | 


# **create_dpi_group**
> DpiGroupResponse create_dpi_group(dpi_group=dpi_group)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.dpi_group import DpiGroup
from unifi_client.models.dpi_group_response import DpiGroupResponse
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
    api_instance = unifi_client.DpiGroupApi(api_client)
    dpi_group = unifi_client.DpiGroup() # DpiGroup |  (optional)

    try:
        api_response = await api_instance.create_dpi_group(dpi_group=dpi_group)
        print("The response of DpiGroupApi->create_dpi_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DpiGroupApi->create_dpi_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dpi_group** | [**DpiGroup**](DpiGroup.md)|  | [optional] 

### Return type

[**DpiGroupResponse**](DpiGroupResponse.md)

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

# **delete_dpi_group**
> DpiGroupResponse delete_dpi_group(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.dpi_group_response import DpiGroupResponse
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
    api_instance = unifi_client.DpiGroupApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.delete_dpi_group(id)
        print("The response of DpiGroupApi->delete_dpi_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DpiGroupApi->delete_dpi_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DpiGroupResponse**](DpiGroupResponse.md)

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

# **get_dpi_group**
> DpiGroupResponse get_dpi_group(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.dpi_group_response import DpiGroupResponse
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
    api_instance = unifi_client.DpiGroupApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.get_dpi_group(id)
        print("The response of DpiGroupApi->get_dpi_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DpiGroupApi->get_dpi_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DpiGroupResponse**](DpiGroupResponse.md)

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

# **list_dpi_group**
> DpiGroupResponse list_dpi_group()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.dpi_group_response import DpiGroupResponse
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
    api_instance = unifi_client.DpiGroupApi(api_client)

    try:
        api_response = await api_instance.list_dpi_group()
        print("The response of DpiGroupApi->list_dpi_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DpiGroupApi->list_dpi_group: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DpiGroupResponse**](DpiGroupResponse.md)

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

# **update_dpi_group**
> DpiGroupResponse update_dpi_group(id, dpi_group_update_request=dpi_group_update_request)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.dpi_group_response import DpiGroupResponse
from unifi_client.models.dpi_group_update_request import DpiGroupUpdateRequest
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
    api_instance = unifi_client.DpiGroupApi(api_client)
    id = 'id_example' # str | 
    dpi_group_update_request = unifi_client.DpiGroupUpdateRequest() # DpiGroupUpdateRequest |  (optional)

    try:
        api_response = await api_instance.update_dpi_group(id, dpi_group_update_request=dpi_group_update_request)
        print("The response of DpiGroupApi->update_dpi_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DpiGroupApi->update_dpi_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **dpi_group_update_request** | [**DpiGroupUpdateRequest**](DpiGroupUpdateRequest.md)|  | [optional] 

### Return type

[**DpiGroupResponse**](DpiGroupResponse.md)

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

