# openapi_client.VirtualDeviceApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_virtual_device**](VirtualDeviceApi.md#create_virtual_device) | **POST** /rest/virtualdevice | 
[**delete_virtual_device**](VirtualDeviceApi.md#delete_virtual_device) | **DELETE** /rest/virtualdevice/{id} | 
[**get_virtual_device**](VirtualDeviceApi.md#get_virtual_device) | **GET** /rest/virtualdevice/{id} | 
[**list_virtual_device**](VirtualDeviceApi.md#list_virtual_device) | **GET** /rest/virtualdevice | 
[**update_virtual_device**](VirtualDeviceApi.md#update_virtual_device) | **PUT** /rest/virtualdevice/{id} | 


# **create_virtual_device**
> VirtualDeviceResponse create_virtual_device(virtual_device=virtual_device)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.virtual_device import VirtualDevice
from openapi_client.models.virtual_device_response import VirtualDeviceResponse
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
    api_instance = openapi_client.VirtualDeviceApi(api_client)
    virtual_device = openapi_client.VirtualDevice() # VirtualDevice |  (optional)

    try:
        api_response = api_instance.create_virtual_device(virtual_device=virtual_device)
        print("The response of VirtualDeviceApi->create_virtual_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualDeviceApi->create_virtual_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_device** | [**VirtualDevice**](VirtualDevice.md)|  | [optional] 

### Return type

[**VirtualDeviceResponse**](VirtualDeviceResponse.md)

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

# **delete_virtual_device**
> VirtualDeviceResponse delete_virtual_device(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.virtual_device_response import VirtualDeviceResponse
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
    api_instance = openapi_client.VirtualDeviceApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.delete_virtual_device(id)
        print("The response of VirtualDeviceApi->delete_virtual_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualDeviceApi->delete_virtual_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**VirtualDeviceResponse**](VirtualDeviceResponse.md)

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

# **get_virtual_device**
> VirtualDeviceResponse get_virtual_device(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.virtual_device_response import VirtualDeviceResponse
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
    api_instance = openapi_client.VirtualDeviceApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_virtual_device(id)
        print("The response of VirtualDeviceApi->get_virtual_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualDeviceApi->get_virtual_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**VirtualDeviceResponse**](VirtualDeviceResponse.md)

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

# **list_virtual_device**
> VirtualDeviceResponse list_virtual_device()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.virtual_device_response import VirtualDeviceResponse
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
    api_instance = openapi_client.VirtualDeviceApi(api_client)

    try:
        api_response = api_instance.list_virtual_device()
        print("The response of VirtualDeviceApi->list_virtual_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualDeviceApi->list_virtual_device: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**VirtualDeviceResponse**](VirtualDeviceResponse.md)

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

# **update_virtual_device**
> VirtualDeviceResponse update_virtual_device(id, virtual_device_update_request=virtual_device_update_request)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.virtual_device_response import VirtualDeviceResponse
from openapi_client.models.virtual_device_update_request import VirtualDeviceUpdateRequest
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
    api_instance = openapi_client.VirtualDeviceApi(api_client)
    id = 'id_example' # str | 
    virtual_device_update_request = openapi_client.VirtualDeviceUpdateRequest() # VirtualDeviceUpdateRequest |  (optional)

    try:
        api_response = api_instance.update_virtual_device(id, virtual_device_update_request=virtual_device_update_request)
        print("The response of VirtualDeviceApi->update_virtual_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VirtualDeviceApi->update_virtual_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **virtual_device_update_request** | [**VirtualDeviceUpdateRequest**](VirtualDeviceUpdateRequest.md)|  | [optional] 

### Return type

[**VirtualDeviceResponse**](VirtualDeviceResponse.md)

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

