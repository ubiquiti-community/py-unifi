# unifi_client.DHCPOptionApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dhcp_option**](DHCPOptionApi.md#create_dhcp_option) | **POST** /rest/dhcpoption | 
[**delete_dhcp_option**](DHCPOptionApi.md#delete_dhcp_option) | **DELETE** /rest/dhcpoption/{id} | 
[**get_dhcp_option**](DHCPOptionApi.md#get_dhcp_option) | **GET** /rest/dhcpoption/{id} | 
[**list_dhcp_option**](DHCPOptionApi.md#list_dhcp_option) | **GET** /rest/dhcpoption | 
[**update_dhcp_option**](DHCPOptionApi.md#update_dhcp_option) | **PUT** /rest/dhcpoption/{id} | 


# **create_dhcp_option**
> DHCPOptionResponse create_dhcp_option(dhcp_option=dhcp_option)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.dhcp_option import DHCPOption
from unifi_client.models.dhcp_option_response import DHCPOptionResponse
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
    api_instance = unifi_client.DHCPOptionApi(api_client)
    dhcp_option = unifi_client.DHCPOption() # DHCPOption |  (optional)

    try:
        api_response = await api_instance.create_dhcp_option(dhcp_option=dhcp_option)
        print("The response of DHCPOptionApi->create_dhcp_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DHCPOptionApi->create_dhcp_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dhcp_option** | [**DHCPOption**](DHCPOption.md)|  | [optional] 

### Return type

[**DHCPOptionResponse**](DHCPOptionResponse.md)

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

# **delete_dhcp_option**
> DHCPOptionResponse delete_dhcp_option(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.dhcp_option_response import DHCPOptionResponse
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
    api_instance = unifi_client.DHCPOptionApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.delete_dhcp_option(id)
        print("The response of DHCPOptionApi->delete_dhcp_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DHCPOptionApi->delete_dhcp_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DHCPOptionResponse**](DHCPOptionResponse.md)

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

# **get_dhcp_option**
> DHCPOptionResponse get_dhcp_option(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.dhcp_option_response import DHCPOptionResponse
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
    api_instance = unifi_client.DHCPOptionApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.get_dhcp_option(id)
        print("The response of DHCPOptionApi->get_dhcp_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DHCPOptionApi->get_dhcp_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DHCPOptionResponse**](DHCPOptionResponse.md)

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

# **list_dhcp_option**
> DHCPOptionResponse list_dhcp_option()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.dhcp_option_response import DHCPOptionResponse
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
    api_instance = unifi_client.DHCPOptionApi(api_client)

    try:
        api_response = await api_instance.list_dhcp_option()
        print("The response of DHCPOptionApi->list_dhcp_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DHCPOptionApi->list_dhcp_option: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DHCPOptionResponse**](DHCPOptionResponse.md)

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

# **update_dhcp_option**
> DHCPOptionResponse update_dhcp_option(id, dhcp_option_update_request=dhcp_option_update_request)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.dhcp_option_response import DHCPOptionResponse
from unifi_client.models.dhcp_option_update_request import DHCPOptionUpdateRequest
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
    api_instance = unifi_client.DHCPOptionApi(api_client)
    id = 'id_example' # str | 
    dhcp_option_update_request = unifi_client.DHCPOptionUpdateRequest() # DHCPOptionUpdateRequest |  (optional)

    try:
        api_response = await api_instance.update_dhcp_option(id, dhcp_option_update_request=dhcp_option_update_request)
        print("The response of DHCPOptionApi->update_dhcp_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DHCPOptionApi->update_dhcp_option: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **dhcp_option_update_request** | [**DHCPOptionUpdateRequest**](DHCPOptionUpdateRequest.md)|  | [optional] 

### Return type

[**DHCPOptionResponse**](DHCPOptionResponse.md)

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

