# unifi_client.ChannelPlanApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_channel_plan**](ChannelPlanApi.md#create_channel_plan) | **POST** /rest/channelplan | 
[**delete_channel_plan**](ChannelPlanApi.md#delete_channel_plan) | **DELETE** /rest/channelplan/{id} | 
[**get_channel_plan**](ChannelPlanApi.md#get_channel_plan) | **GET** /rest/channelplan/{id} | 
[**list_channel_plan**](ChannelPlanApi.md#list_channel_plan) | **GET** /rest/channelplan | 
[**update_channel_plan**](ChannelPlanApi.md#update_channel_plan) | **PUT** /rest/channelplan/{id} | 


# **create_channel_plan**
> ChannelPlanResponse create_channel_plan(channel_plan=channel_plan)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.channel_plan import ChannelPlan
from unifi_client.models.channel_plan_response import ChannelPlanResponse
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
    api_instance = unifi_client.ChannelPlanApi(api_client)
    channel_plan = unifi_client.ChannelPlan() # ChannelPlan |  (optional)

    try:
        api_response = await api_instance.create_channel_plan(channel_plan=channel_plan)
        print("The response of ChannelPlanApi->create_channel_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelPlanApi->create_channel_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_plan** | [**ChannelPlan**](ChannelPlan.md)|  | [optional] 

### Return type

[**ChannelPlanResponse**](ChannelPlanResponse.md)

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

# **delete_channel_plan**
> ChannelPlanResponse delete_channel_plan(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.channel_plan_response import ChannelPlanResponse
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
    api_instance = unifi_client.ChannelPlanApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.delete_channel_plan(id)
        print("The response of ChannelPlanApi->delete_channel_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelPlanApi->delete_channel_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ChannelPlanResponse**](ChannelPlanResponse.md)

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

# **get_channel_plan**
> ChannelPlanResponse get_channel_plan(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.channel_plan_response import ChannelPlanResponse
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
    api_instance = unifi_client.ChannelPlanApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.get_channel_plan(id)
        print("The response of ChannelPlanApi->get_channel_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelPlanApi->get_channel_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ChannelPlanResponse**](ChannelPlanResponse.md)

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

# **list_channel_plan**
> ChannelPlanResponse list_channel_plan()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.channel_plan_response import ChannelPlanResponse
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
    api_instance = unifi_client.ChannelPlanApi(api_client)

    try:
        api_response = await api_instance.list_channel_plan()
        print("The response of ChannelPlanApi->list_channel_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelPlanApi->list_channel_plan: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ChannelPlanResponse**](ChannelPlanResponse.md)

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

# **update_channel_plan**
> ChannelPlanResponse update_channel_plan(id, channel_plan_update_request=channel_plan_update_request)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.channel_plan_response import ChannelPlanResponse
from unifi_client.models.channel_plan_update_request import ChannelPlanUpdateRequest
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
    api_instance = unifi_client.ChannelPlanApi(api_client)
    id = 'id_example' # str | 
    channel_plan_update_request = unifi_client.ChannelPlanUpdateRequest() # ChannelPlanUpdateRequest |  (optional)

    try:
        api_response = await api_instance.update_channel_plan(id, channel_plan_update_request=channel_plan_update_request)
        print("The response of ChannelPlanApi->update_channel_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelPlanApi->update_channel_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **channel_plan_update_request** | [**ChannelPlanUpdateRequest**](ChannelPlanUpdateRequest.md)|  | [optional] 

### Return type

[**ChannelPlanResponse**](ChannelPlanResponse.md)

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

