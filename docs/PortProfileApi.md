# unifi_client.PortProfileApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_port_profile**](PortProfileApi.md#create_port_profile) | **POST** /rest/portconf | 
[**delete_port_profile**](PortProfileApi.md#delete_port_profile) | **DELETE** /rest/portconf/{id} | 
[**get_port_profile**](PortProfileApi.md#get_port_profile) | **GET** /rest/portconf/{id} | 
[**list_port_profile**](PortProfileApi.md#list_port_profile) | **GET** /rest/portconf | 
[**update_port_profile**](PortProfileApi.md#update_port_profile) | **PUT** /rest/portconf/{id} | 


# **create_port_profile**
> PortProfileResponse create_port_profile(port_profile=port_profile)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.port_profile import PortProfile
from unifi_client.models.port_profile_response import PortProfileResponse
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
    api_instance = unifi_client.PortProfileApi(api_client)
    port_profile = unifi_client.PortProfile() # PortProfile |  (optional)

    try:
        api_response = await api_instance.create_port_profile(port_profile=port_profile)
        print("The response of PortProfileApi->create_port_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortProfileApi->create_port_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port_profile** | [**PortProfile**](PortProfile.md)|  | [optional] 

### Return type

[**PortProfileResponse**](PortProfileResponse.md)

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

# **delete_port_profile**
> PortProfileResponse delete_port_profile(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.port_profile_response import PortProfileResponse
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
    api_instance = unifi_client.PortProfileApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.delete_port_profile(id)
        print("The response of PortProfileApi->delete_port_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortProfileApi->delete_port_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PortProfileResponse**](PortProfileResponse.md)

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

# **get_port_profile**
> PortProfileResponse get_port_profile(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.port_profile_response import PortProfileResponse
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
    api_instance = unifi_client.PortProfileApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.get_port_profile(id)
        print("The response of PortProfileApi->get_port_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortProfileApi->get_port_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PortProfileResponse**](PortProfileResponse.md)

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

# **list_port_profile**
> PortProfileResponse list_port_profile()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.port_profile_response import PortProfileResponse
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
    api_instance = unifi_client.PortProfileApi(api_client)

    try:
        api_response = await api_instance.list_port_profile()
        print("The response of PortProfileApi->list_port_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortProfileApi->list_port_profile: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PortProfileResponse**](PortProfileResponse.md)

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

# **update_port_profile**
> PortProfileResponse update_port_profile(id, port_profile_update_request=port_profile_update_request)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.port_profile_response import PortProfileResponse
from unifi_client.models.port_profile_update_request import PortProfileUpdateRequest
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
    api_instance = unifi_client.PortProfileApi(api_client)
    id = 'id_example' # str | 
    port_profile_update_request = unifi_client.PortProfileUpdateRequest() # PortProfileUpdateRequest |  (optional)

    try:
        api_response = await api_instance.update_port_profile(id, port_profile_update_request=port_profile_update_request)
        print("The response of PortProfileApi->update_port_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortProfileApi->update_port_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **port_profile_update_request** | [**PortProfileUpdateRequest**](PortProfileUpdateRequest.md)|  | [optional] 

### Return type

[**PortProfileResponse**](PortProfileResponse.md)

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

