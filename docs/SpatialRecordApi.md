# unifi_client.SpatialRecordApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_spatial_record**](SpatialRecordApi.md#create_spatial_record) | **POST** /rest/spatialrecord | 
[**delete_spatial_record**](SpatialRecordApi.md#delete_spatial_record) | **DELETE** /rest/spatialrecord/{id} | 
[**get_spatial_record**](SpatialRecordApi.md#get_spatial_record) | **GET** /rest/spatialrecord/{id} | 
[**list_spatial_record**](SpatialRecordApi.md#list_spatial_record) | **GET** /rest/spatialrecord | 
[**update_spatial_record**](SpatialRecordApi.md#update_spatial_record) | **PUT** /rest/spatialrecord/{id} | 


# **create_spatial_record**
> SpatialRecordResponse create_spatial_record(spatial_record=spatial_record)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.spatial_record import SpatialRecord
from unifi_client.models.spatial_record_response import SpatialRecordResponse
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
    api_instance = unifi_client.SpatialRecordApi(api_client)
    spatial_record = unifi_client.SpatialRecord() # SpatialRecord |  (optional)

    try:
        api_response = await api_instance.create_spatial_record(spatial_record=spatial_record)
        print("The response of SpatialRecordApi->create_spatial_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpatialRecordApi->create_spatial_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spatial_record** | [**SpatialRecord**](SpatialRecord.md)|  | [optional] 

### Return type

[**SpatialRecordResponse**](SpatialRecordResponse.md)

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

# **delete_spatial_record**
> SpatialRecordResponse delete_spatial_record(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.spatial_record_response import SpatialRecordResponse
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
    api_instance = unifi_client.SpatialRecordApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.delete_spatial_record(id)
        print("The response of SpatialRecordApi->delete_spatial_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpatialRecordApi->delete_spatial_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SpatialRecordResponse**](SpatialRecordResponse.md)

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

# **get_spatial_record**
> SpatialRecordResponse get_spatial_record(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.spatial_record_response import SpatialRecordResponse
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
    api_instance = unifi_client.SpatialRecordApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.get_spatial_record(id)
        print("The response of SpatialRecordApi->get_spatial_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpatialRecordApi->get_spatial_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SpatialRecordResponse**](SpatialRecordResponse.md)

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

# **list_spatial_record**
> SpatialRecordResponse list_spatial_record()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.spatial_record_response import SpatialRecordResponse
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
    api_instance = unifi_client.SpatialRecordApi(api_client)

    try:
        api_response = await api_instance.list_spatial_record()
        print("The response of SpatialRecordApi->list_spatial_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpatialRecordApi->list_spatial_record: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SpatialRecordResponse**](SpatialRecordResponse.md)

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

# **update_spatial_record**
> SpatialRecordResponse update_spatial_record(id, spatial_record_update_request=spatial_record_update_request)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.spatial_record_response import SpatialRecordResponse
from unifi_client.models.spatial_record_update_request import SpatialRecordUpdateRequest
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
    api_instance = unifi_client.SpatialRecordApi(api_client)
    id = 'id_example' # str | 
    spatial_record_update_request = unifi_client.SpatialRecordUpdateRequest() # SpatialRecordUpdateRequest |  (optional)

    try:
        api_response = await api_instance.update_spatial_record(id, spatial_record_update_request=spatial_record_update_request)
        print("The response of SpatialRecordApi->update_spatial_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpatialRecordApi->update_spatial_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **spatial_record_update_request** | [**SpatialRecordUpdateRequest**](SpatialRecordUpdateRequest.md)|  | [optional] 

### Return type

[**SpatialRecordResponse**](SpatialRecordResponse.md)

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

