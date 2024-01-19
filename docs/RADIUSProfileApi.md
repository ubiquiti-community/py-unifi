# openapi_client.RADIUSProfileApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_radius_profile**](RADIUSProfileApi.md#create_radius_profile) | **POST** /rest/radiusprofile | 
[**delete_radius_profile**](RADIUSProfileApi.md#delete_radius_profile) | **DELETE** /rest/radiusprofile/{id} | 
[**get_radius_profile**](RADIUSProfileApi.md#get_radius_profile) | **GET** /rest/radiusprofile/{id} | 
[**list_radius_profile**](RADIUSProfileApi.md#list_radius_profile) | **GET** /rest/radiusprofile | 
[**update_radius_profile**](RADIUSProfileApi.md#update_radius_profile) | **PUT** /rest/radiusprofile/{id} | 


# **create_radius_profile**
> RADIUSProfileResponse create_radius_profile(radius_profile=radius_profile)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.radius_profile import RADIUSProfile
from openapi_client.models.radius_profile_response import RADIUSProfileResponse
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
    api_instance = openapi_client.RADIUSProfileApi(api_client)
    radius_profile = openapi_client.RADIUSProfile() # RADIUSProfile |  (optional)

    try:
        api_response = api_instance.create_radius_profile(radius_profile=radius_profile)
        print("The response of RADIUSProfileApi->create_radius_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RADIUSProfileApi->create_radius_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radius_profile** | [**RADIUSProfile**](RADIUSProfile.md)|  | [optional] 

### Return type

[**RADIUSProfileResponse**](RADIUSProfileResponse.md)

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

# **delete_radius_profile**
> RADIUSProfileResponse delete_radius_profile(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.radius_profile_response import RADIUSProfileResponse
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
    api_instance = openapi_client.RADIUSProfileApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.delete_radius_profile(id)
        print("The response of RADIUSProfileApi->delete_radius_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RADIUSProfileApi->delete_radius_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**RADIUSProfileResponse**](RADIUSProfileResponse.md)

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

# **get_radius_profile**
> RADIUSProfileResponse get_radius_profile(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.radius_profile_response import RADIUSProfileResponse
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
    api_instance = openapi_client.RADIUSProfileApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_radius_profile(id)
        print("The response of RADIUSProfileApi->get_radius_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RADIUSProfileApi->get_radius_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**RADIUSProfileResponse**](RADIUSProfileResponse.md)

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

# **list_radius_profile**
> RADIUSProfileResponse list_radius_profile()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.radius_profile_response import RADIUSProfileResponse
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
    api_instance = openapi_client.RADIUSProfileApi(api_client)

    try:
        api_response = api_instance.list_radius_profile()
        print("The response of RADIUSProfileApi->list_radius_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RADIUSProfileApi->list_radius_profile: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RADIUSProfileResponse**](RADIUSProfileResponse.md)

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

# **update_radius_profile**
> RADIUSProfileResponse update_radius_profile(id, radius_profile_update_request=radius_profile_update_request)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.radius_profile_response import RADIUSProfileResponse
from openapi_client.models.radius_profile_update_request import RADIUSProfileUpdateRequest
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
    api_instance = openapi_client.RADIUSProfileApi(api_client)
    id = 'id_example' # str | 
    radius_profile_update_request = openapi_client.RADIUSProfileUpdateRequest() # RADIUSProfileUpdateRequest |  (optional)

    try:
        api_response = api_instance.update_radius_profile(id, radius_profile_update_request=radius_profile_update_request)
        print("The response of RADIUSProfileApi->update_radius_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RADIUSProfileApi->update_radius_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **radius_profile_update_request** | [**RADIUSProfileUpdateRequest**](RADIUSProfileUpdateRequest.md)|  | [optional] 

### Return type

[**RADIUSProfileResponse**](RADIUSProfileResponse.md)

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

