# unifi_client.FirewallGroupApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_firewall_group**](FirewallGroupApi.md#create_firewall_group) | **POST** /rest/firewallgroup | 
[**delete_firewall_group**](FirewallGroupApi.md#delete_firewall_group) | **DELETE** /rest/firewallgroup/{id} | 
[**get_firewall_group**](FirewallGroupApi.md#get_firewall_group) | **GET** /rest/firewallgroup/{id} | 
[**list_firewall_group**](FirewallGroupApi.md#list_firewall_group) | **GET** /rest/firewallgroup | 
[**update_firewall_group**](FirewallGroupApi.md#update_firewall_group) | **PUT** /rest/firewallgroup/{id} | 


# **create_firewall_group**
> FirewallGroupResponse create_firewall_group(firewall_group=firewall_group)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.firewall_group import FirewallGroup
from unifi_client.models.firewall_group_response import FirewallGroupResponse
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
    api_instance = unifi_client.FirewallGroupApi(api_client)
    firewall_group = unifi_client.FirewallGroup() # FirewallGroup |  (optional)

    try:
        api_response = await api_instance.create_firewall_group(firewall_group=firewall_group)
        print("The response of FirewallGroupApi->create_firewall_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallGroupApi->create_firewall_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_group** | [**FirewallGroup**](FirewallGroup.md)|  | [optional] 

### Return type

[**FirewallGroupResponse**](FirewallGroupResponse.md)

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

# **delete_firewall_group**
> FirewallGroupResponse delete_firewall_group(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.firewall_group_response import FirewallGroupResponse
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
    api_instance = unifi_client.FirewallGroupApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.delete_firewall_group(id)
        print("The response of FirewallGroupApi->delete_firewall_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallGroupApi->delete_firewall_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FirewallGroupResponse**](FirewallGroupResponse.md)

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

# **get_firewall_group**
> FirewallGroupResponse get_firewall_group(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.firewall_group_response import FirewallGroupResponse
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
    api_instance = unifi_client.FirewallGroupApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.get_firewall_group(id)
        print("The response of FirewallGroupApi->get_firewall_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallGroupApi->get_firewall_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FirewallGroupResponse**](FirewallGroupResponse.md)

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

# **list_firewall_group**
> FirewallGroupResponse list_firewall_group()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.firewall_group_response import FirewallGroupResponse
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
    api_instance = unifi_client.FirewallGroupApi(api_client)

    try:
        api_response = await api_instance.list_firewall_group()
        print("The response of FirewallGroupApi->list_firewall_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallGroupApi->list_firewall_group: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FirewallGroupResponse**](FirewallGroupResponse.md)

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

# **update_firewall_group**
> FirewallGroupResponse update_firewall_group(id, firewall_group_update_request=firewall_group_update_request)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.firewall_group_response import FirewallGroupResponse
from unifi_client.models.firewall_group_update_request import FirewallGroupUpdateRequest
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
    api_instance = unifi_client.FirewallGroupApi(api_client)
    id = 'id_example' # str | 
    firewall_group_update_request = unifi_client.FirewallGroupUpdateRequest() # FirewallGroupUpdateRequest |  (optional)

    try:
        api_response = await api_instance.update_firewall_group(id, firewall_group_update_request=firewall_group_update_request)
        print("The response of FirewallGroupApi->update_firewall_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallGroupApi->update_firewall_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **firewall_group_update_request** | [**FirewallGroupUpdateRequest**](FirewallGroupUpdateRequest.md)|  | [optional] 

### Return type

[**FirewallGroupResponse**](FirewallGroupResponse.md)

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

