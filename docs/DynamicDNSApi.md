# openapi_client.DynamicDNSApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dynamic_dns**](DynamicDNSApi.md#create_dynamic_dns) | **POST** /rest/dynamicdns | 
[**delete_dynamic_dns**](DynamicDNSApi.md#delete_dynamic_dns) | **DELETE** /rest/dynamicdns/{id} | 
[**get_dynamic_dns**](DynamicDNSApi.md#get_dynamic_dns) | **GET** /rest/dynamicdns/{id} | 
[**list_dynamic_dns**](DynamicDNSApi.md#list_dynamic_dns) | **GET** /rest/dynamicdns | 
[**update_dynamic_dns**](DynamicDNSApi.md#update_dynamic_dns) | **PUT** /rest/dynamicdns/{id} | 


# **create_dynamic_dns**
> DynamicDNSResponse create_dynamic_dns(dynamic_dns=dynamic_dns)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dynamic_dns import DynamicDNS
from openapi_client.models.dynamic_dns_response import DynamicDNSResponse
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
    api_instance = openapi_client.DynamicDNSApi(api_client)
    dynamic_dns = openapi_client.DynamicDNS() # DynamicDNS |  (optional)

    try:
        api_response = api_instance.create_dynamic_dns(dynamic_dns=dynamic_dns)
        print("The response of DynamicDNSApi->create_dynamic_dns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicDNSApi->create_dynamic_dns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_dns** | [**DynamicDNS**](DynamicDNS.md)|  | [optional] 

### Return type

[**DynamicDNSResponse**](DynamicDNSResponse.md)

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

# **delete_dynamic_dns**
> DynamicDNSResponse delete_dynamic_dns(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dynamic_dns_response import DynamicDNSResponse
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
    api_instance = openapi_client.DynamicDNSApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.delete_dynamic_dns(id)
        print("The response of DynamicDNSApi->delete_dynamic_dns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicDNSApi->delete_dynamic_dns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DynamicDNSResponse**](DynamicDNSResponse.md)

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

# **get_dynamic_dns**
> DynamicDNSResponse get_dynamic_dns(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dynamic_dns_response import DynamicDNSResponse
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
    api_instance = openapi_client.DynamicDNSApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_dynamic_dns(id)
        print("The response of DynamicDNSApi->get_dynamic_dns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicDNSApi->get_dynamic_dns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DynamicDNSResponse**](DynamicDNSResponse.md)

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

# **list_dynamic_dns**
> DynamicDNSResponse list_dynamic_dns()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dynamic_dns_response import DynamicDNSResponse
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
    api_instance = openapi_client.DynamicDNSApi(api_client)

    try:
        api_response = api_instance.list_dynamic_dns()
        print("The response of DynamicDNSApi->list_dynamic_dns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicDNSApi->list_dynamic_dns: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DynamicDNSResponse**](DynamicDNSResponse.md)

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

# **update_dynamic_dns**
> DynamicDNSResponse update_dynamic_dns(id, dynamic_dns_update_request=dynamic_dns_update_request)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.dynamic_dns_response import DynamicDNSResponse
from openapi_client.models.dynamic_dns_update_request import DynamicDNSUpdateRequest
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
    api_instance = openapi_client.DynamicDNSApi(api_client)
    id = 'id_example' # str | 
    dynamic_dns_update_request = openapi_client.DynamicDNSUpdateRequest() # DynamicDNSUpdateRequest |  (optional)

    try:
        api_response = api_instance.update_dynamic_dns(id, dynamic_dns_update_request=dynamic_dns_update_request)
        print("The response of DynamicDNSApi->update_dynamic_dns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicDNSApi->update_dynamic_dns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **dynamic_dns_update_request** | [**DynamicDNSUpdateRequest**](DynamicDNSUpdateRequest.md)|  | [optional] 

### Return type

[**DynamicDNSResponse**](DynamicDNSResponse.md)

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

