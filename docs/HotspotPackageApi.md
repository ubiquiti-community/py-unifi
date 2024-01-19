# unifi_client.HotspotPackageApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_hotspot_package**](HotspotPackageApi.md#create_hotspot_package) | **POST** /rest/hotspotpackage | 
[**delete_hotspot_package**](HotspotPackageApi.md#delete_hotspot_package) | **DELETE** /rest/hotspotpackage/{id} | 
[**get_hotspot_package**](HotspotPackageApi.md#get_hotspot_package) | **GET** /rest/hotspotpackage/{id} | 
[**list_hotspot_package**](HotspotPackageApi.md#list_hotspot_package) | **GET** /rest/hotspotpackage | 
[**update_hotspot_package**](HotspotPackageApi.md#update_hotspot_package) | **PUT** /rest/hotspotpackage/{id} | 


# **create_hotspot_package**
> HotspotPackageResponse create_hotspot_package(hotspot_package=hotspot_package)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.hotspot_package import HotspotPackage
from unifi_client.models.hotspot_package_response import HotspotPackageResponse
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
    api_instance = unifi_client.HotspotPackageApi(api_client)
    hotspot_package = unifi_client.HotspotPackage() # HotspotPackage |  (optional)

    try:
        api_response = await api_instance.create_hotspot_package(hotspot_package=hotspot_package)
        print("The response of HotspotPackageApi->create_hotspot_package:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HotspotPackageApi->create_hotspot_package: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hotspot_package** | [**HotspotPackage**](HotspotPackage.md)|  | [optional] 

### Return type

[**HotspotPackageResponse**](HotspotPackageResponse.md)

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

# **delete_hotspot_package**
> HotspotPackageResponse delete_hotspot_package(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.hotspot_package_response import HotspotPackageResponse
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
    api_instance = unifi_client.HotspotPackageApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.delete_hotspot_package(id)
        print("The response of HotspotPackageApi->delete_hotspot_package:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HotspotPackageApi->delete_hotspot_package: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**HotspotPackageResponse**](HotspotPackageResponse.md)

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

# **get_hotspot_package**
> HotspotPackageResponse get_hotspot_package(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.hotspot_package_response import HotspotPackageResponse
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
    api_instance = unifi_client.HotspotPackageApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.get_hotspot_package(id)
        print("The response of HotspotPackageApi->get_hotspot_package:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HotspotPackageApi->get_hotspot_package: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**HotspotPackageResponse**](HotspotPackageResponse.md)

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

# **list_hotspot_package**
> HotspotPackageResponse list_hotspot_package()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.hotspot_package_response import HotspotPackageResponse
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
    api_instance = unifi_client.HotspotPackageApi(api_client)

    try:
        api_response = await api_instance.list_hotspot_package()
        print("The response of HotspotPackageApi->list_hotspot_package:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HotspotPackageApi->list_hotspot_package: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HotspotPackageResponse**](HotspotPackageResponse.md)

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

# **update_hotspot_package**
> HotspotPackageResponse update_hotspot_package(id, hotspot_package_update_request=hotspot_package_update_request)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.hotspot_package_response import HotspotPackageResponse
from unifi_client.models.hotspot_package_update_request import HotspotPackageUpdateRequest
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
    api_instance = unifi_client.HotspotPackageApi(api_client)
    id = 'id_example' # str | 
    hotspot_package_update_request = unifi_client.HotspotPackageUpdateRequest() # HotspotPackageUpdateRequest |  (optional)

    try:
        api_response = await api_instance.update_hotspot_package(id, hotspot_package_update_request=hotspot_package_update_request)
        print("The response of HotspotPackageApi->update_hotspot_package:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HotspotPackageApi->update_hotspot_package: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **hotspot_package_update_request** | [**HotspotPackageUpdateRequest**](HotspotPackageUpdateRequest.md)|  | [optional] 

### Return type

[**HotspotPackageResponse**](HotspotPackageResponse.md)

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

