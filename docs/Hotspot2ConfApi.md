# openapi_client.Hotspot2ConfApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_hotspot2_conf**](Hotspot2ConfApi.md#create_hotspot2_conf) | **POST** /rest/hotspot2conf | 
[**delete_hotspot2_conf**](Hotspot2ConfApi.md#delete_hotspot2_conf) | **DELETE** /rest/hotspot2conf/{id} | 
[**get_hotspot2_conf**](Hotspot2ConfApi.md#get_hotspot2_conf) | **GET** /rest/hotspot2conf/{id} | 
[**list_hotspot2_conf**](Hotspot2ConfApi.md#list_hotspot2_conf) | **GET** /rest/hotspot2conf | 
[**update_hotspot2_conf**](Hotspot2ConfApi.md#update_hotspot2_conf) | **PUT** /rest/hotspot2conf/{id} | 


# **create_hotspot2_conf**
> Hotspot2ConfResponse create_hotspot2_conf(hotspot2_conf=hotspot2_conf)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.hotspot2_conf import Hotspot2Conf
from openapi_client.models.hotspot2_conf_response import Hotspot2ConfResponse
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
    api_instance = openapi_client.Hotspot2ConfApi(api_client)
    hotspot2_conf = openapi_client.Hotspot2Conf() # Hotspot2Conf |  (optional)

    try:
        api_response = api_instance.create_hotspot2_conf(hotspot2_conf=hotspot2_conf)
        print("The response of Hotspot2ConfApi->create_hotspot2_conf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Hotspot2ConfApi->create_hotspot2_conf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hotspot2_conf** | [**Hotspot2Conf**](Hotspot2Conf.md)|  | [optional] 

### Return type

[**Hotspot2ConfResponse**](Hotspot2ConfResponse.md)

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

# **delete_hotspot2_conf**
> Hotspot2ConfResponse delete_hotspot2_conf(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.hotspot2_conf_response import Hotspot2ConfResponse
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
    api_instance = openapi_client.Hotspot2ConfApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.delete_hotspot2_conf(id)
        print("The response of Hotspot2ConfApi->delete_hotspot2_conf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Hotspot2ConfApi->delete_hotspot2_conf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Hotspot2ConfResponse**](Hotspot2ConfResponse.md)

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

# **get_hotspot2_conf**
> Hotspot2ConfResponse get_hotspot2_conf(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.hotspot2_conf_response import Hotspot2ConfResponse
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
    api_instance = openapi_client.Hotspot2ConfApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_hotspot2_conf(id)
        print("The response of Hotspot2ConfApi->get_hotspot2_conf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Hotspot2ConfApi->get_hotspot2_conf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Hotspot2ConfResponse**](Hotspot2ConfResponse.md)

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

# **list_hotspot2_conf**
> Hotspot2ConfResponse list_hotspot2_conf()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.hotspot2_conf_response import Hotspot2ConfResponse
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
    api_instance = openapi_client.Hotspot2ConfApi(api_client)

    try:
        api_response = api_instance.list_hotspot2_conf()
        print("The response of Hotspot2ConfApi->list_hotspot2_conf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Hotspot2ConfApi->list_hotspot2_conf: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Hotspot2ConfResponse**](Hotspot2ConfResponse.md)

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

# **update_hotspot2_conf**
> Hotspot2ConfResponse update_hotspot2_conf(id, hotspot2_conf_update_request=hotspot2_conf_update_request)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.hotspot2_conf_response import Hotspot2ConfResponse
from openapi_client.models.hotspot2_conf_update_request import Hotspot2ConfUpdateRequest
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
    api_instance = openapi_client.Hotspot2ConfApi(api_client)
    id = 'id_example' # str | 
    hotspot2_conf_update_request = openapi_client.Hotspot2ConfUpdateRequest() # Hotspot2ConfUpdateRequest |  (optional)

    try:
        api_response = api_instance.update_hotspot2_conf(id, hotspot2_conf_update_request=hotspot2_conf_update_request)
        print("The response of Hotspot2ConfApi->update_hotspot2_conf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Hotspot2ConfApi->update_hotspot2_conf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **hotspot2_conf_update_request** | [**Hotspot2ConfUpdateRequest**](Hotspot2ConfUpdateRequest.md)|  | [optional] 

### Return type

[**Hotspot2ConfResponse**](Hotspot2ConfResponse.md)

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

