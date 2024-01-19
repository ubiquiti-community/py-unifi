# openapi_client.UserGroupApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_group**](UserGroupApi.md#create_user_group) | **POST** /rest/usergroup | 
[**delete_user_group**](UserGroupApi.md#delete_user_group) | **DELETE** /rest/usergroup/{id} | 
[**get_user_group**](UserGroupApi.md#get_user_group) | **GET** /rest/usergroup/{id} | 
[**list_user_group**](UserGroupApi.md#list_user_group) | **GET** /rest/usergroup | 
[**update_user_group**](UserGroupApi.md#update_user_group) | **PUT** /rest/usergroup/{id} | 


# **create_user_group**
> UserGroupResponse create_user_group(user_group=user_group)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.user_group import UserGroup
from openapi_client.models.user_group_response import UserGroupResponse
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
    api_instance = openapi_client.UserGroupApi(api_client)
    user_group = openapi_client.UserGroup() # UserGroup |  (optional)

    try:
        api_response = api_instance.create_user_group(user_group=user_group)
        print("The response of UserGroupApi->create_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupApi->create_user_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group** | [**UserGroup**](UserGroup.md)|  | [optional] 

### Return type

[**UserGroupResponse**](UserGroupResponse.md)

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

# **delete_user_group**
> UserGroupResponse delete_user_group(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.user_group_response import UserGroupResponse
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
    api_instance = openapi_client.UserGroupApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.delete_user_group(id)
        print("The response of UserGroupApi->delete_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupApi->delete_user_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**UserGroupResponse**](UserGroupResponse.md)

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

# **get_user_group**
> UserGroupResponse get_user_group(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.user_group_response import UserGroupResponse
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
    api_instance = openapi_client.UserGroupApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_user_group(id)
        print("The response of UserGroupApi->get_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupApi->get_user_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**UserGroupResponse**](UserGroupResponse.md)

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

# **list_user_group**
> UserGroupResponse list_user_group()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.user_group_response import UserGroupResponse
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
    api_instance = openapi_client.UserGroupApi(api_client)

    try:
        api_response = api_instance.list_user_group()
        print("The response of UserGroupApi->list_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupApi->list_user_group: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserGroupResponse**](UserGroupResponse.md)

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

# **update_user_group**
> UserGroupResponse update_user_group(id, user_group_update_request=user_group_update_request)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.user_group_response import UserGroupResponse
from openapi_client.models.user_group_update_request import UserGroupUpdateRequest
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
    api_instance = openapi_client.UserGroupApi(api_client)
    id = 'id_example' # str | 
    user_group_update_request = openapi_client.UserGroupUpdateRequest() # UserGroupUpdateRequest |  (optional)

    try:
        api_response = api_instance.update_user_group(id, user_group_update_request=user_group_update_request)
        print("The response of UserGroupApi->update_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupApi->update_user_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **user_group_update_request** | [**UserGroupUpdateRequest**](UserGroupUpdateRequest.md)|  | [optional] 

### Return type

[**UserGroupResponse**](UserGroupResponse.md)

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

