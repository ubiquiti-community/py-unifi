# unifi_client.ScheduleTaskApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_schedule_task**](ScheduleTaskApi.md#create_schedule_task) | **POST** /rest/scheduletask | 
[**delete_schedule_task**](ScheduleTaskApi.md#delete_schedule_task) | **DELETE** /rest/scheduletask/{id} | 
[**get_schedule_task**](ScheduleTaskApi.md#get_schedule_task) | **GET** /rest/scheduletask/{id} | 
[**list_schedule_task**](ScheduleTaskApi.md#list_schedule_task) | **GET** /rest/scheduletask | 
[**update_schedule_task**](ScheduleTaskApi.md#update_schedule_task) | **PUT** /rest/scheduletask/{id} | 


# **create_schedule_task**
> ScheduleTaskResponse create_schedule_task(schedule_task=schedule_task)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.schedule_task import ScheduleTask
from unifi_client.models.schedule_task_response import ScheduleTaskResponse
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
    api_instance = unifi_client.ScheduleTaskApi(api_client)
    schedule_task = unifi_client.ScheduleTask() # ScheduleTask |  (optional)

    try:
        api_response = await api_instance.create_schedule_task(schedule_task=schedule_task)
        print("The response of ScheduleTaskApi->create_schedule_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleTaskApi->create_schedule_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_task** | [**ScheduleTask**](ScheduleTask.md)|  | [optional] 

### Return type

[**ScheduleTaskResponse**](ScheduleTaskResponse.md)

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

# **delete_schedule_task**
> ScheduleTaskResponse delete_schedule_task(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.schedule_task_response import ScheduleTaskResponse
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
    api_instance = unifi_client.ScheduleTaskApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.delete_schedule_task(id)
        print("The response of ScheduleTaskApi->delete_schedule_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleTaskApi->delete_schedule_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ScheduleTaskResponse**](ScheduleTaskResponse.md)

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

# **get_schedule_task**
> ScheduleTaskResponse get_schedule_task(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.schedule_task_response import ScheduleTaskResponse
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
    api_instance = unifi_client.ScheduleTaskApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.get_schedule_task(id)
        print("The response of ScheduleTaskApi->get_schedule_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleTaskApi->get_schedule_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ScheduleTaskResponse**](ScheduleTaskResponse.md)

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

# **list_schedule_task**
> ScheduleTaskResponse list_schedule_task()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.schedule_task_response import ScheduleTaskResponse
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
    api_instance = unifi_client.ScheduleTaskApi(api_client)

    try:
        api_response = await api_instance.list_schedule_task()
        print("The response of ScheduleTaskApi->list_schedule_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleTaskApi->list_schedule_task: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ScheduleTaskResponse**](ScheduleTaskResponse.md)

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

# **update_schedule_task**
> ScheduleTaskResponse update_schedule_task(id, schedule_task_update_request=schedule_task_update_request)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.schedule_task_response import ScheduleTaskResponse
from unifi_client.models.schedule_task_update_request import ScheduleTaskUpdateRequest
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
    api_instance = unifi_client.ScheduleTaskApi(api_client)
    id = 'id_example' # str | 
    schedule_task_update_request = unifi_client.ScheduleTaskUpdateRequest() # ScheduleTaskUpdateRequest |  (optional)

    try:
        api_response = await api_instance.update_schedule_task(id, schedule_task_update_request=schedule_task_update_request)
        print("The response of ScheduleTaskApi->update_schedule_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleTaskApi->update_schedule_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **schedule_task_update_request** | [**ScheduleTaskUpdateRequest**](ScheduleTaskUpdateRequest.md)|  | [optional] 

### Return type

[**ScheduleTaskResponse**](ScheduleTaskResponse.md)

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

