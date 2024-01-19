# unifi_client.MediaFileApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_media_file**](MediaFileApi.md#create_media_file) | **POST** /rest/mediafile | 
[**delete_media_file**](MediaFileApi.md#delete_media_file) | **DELETE** /rest/mediafile/{id} | 
[**get_media_file**](MediaFileApi.md#get_media_file) | **GET** /rest/mediafile/{id} | 
[**list_media_file**](MediaFileApi.md#list_media_file) | **GET** /rest/mediafile | 
[**update_media_file**](MediaFileApi.md#update_media_file) | **PUT** /rest/mediafile/{id} | 


# **create_media_file**
> MediaFileResponse create_media_file(media_file=media_file)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.media_file import MediaFile
from unifi_client.models.media_file_response import MediaFileResponse
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
    api_instance = unifi_client.MediaFileApi(api_client)
    media_file = unifi_client.MediaFile() # MediaFile |  (optional)

    try:
        api_response = await api_instance.create_media_file(media_file=media_file)
        print("The response of MediaFileApi->create_media_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaFileApi->create_media_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_file** | [**MediaFile**](MediaFile.md)|  | [optional] 

### Return type

[**MediaFileResponse**](MediaFileResponse.md)

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

# **delete_media_file**
> MediaFileResponse delete_media_file(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.media_file_response import MediaFileResponse
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
    api_instance = unifi_client.MediaFileApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.delete_media_file(id)
        print("The response of MediaFileApi->delete_media_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaFileApi->delete_media_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**MediaFileResponse**](MediaFileResponse.md)

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

# **get_media_file**
> MediaFileResponse get_media_file(id)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.media_file_response import MediaFileResponse
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
    api_instance = unifi_client.MediaFileApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.get_media_file(id)
        print("The response of MediaFileApi->get_media_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaFileApi->get_media_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**MediaFileResponse**](MediaFileResponse.md)

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

# **list_media_file**
> MediaFileResponse list_media_file()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.media_file_response import MediaFileResponse
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
    api_instance = unifi_client.MediaFileApi(api_client)

    try:
        api_response = await api_instance.list_media_file()
        print("The response of MediaFileApi->list_media_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaFileApi->list_media_file: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MediaFileResponse**](MediaFileResponse.md)

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

# **update_media_file**
> MediaFileResponse update_media_file(id, media_file_update_request=media_file_update_request)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.media_file_response import MediaFileResponse
from unifi_client.models.media_file_update_request import MediaFileUpdateRequest
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
    api_instance = unifi_client.MediaFileApi(api_client)
    id = 'id_example' # str | 
    media_file_update_request = unifi_client.MediaFileUpdateRequest() # MediaFileUpdateRequest |  (optional)

    try:
        api_response = await api_instance.update_media_file(id, media_file_update_request=media_file_update_request)
        print("The response of MediaFileApi->update_media_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaFileApi->update_media_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **media_file_update_request** | [**MediaFileUpdateRequest**](MediaFileUpdateRequest.md)|  | [optional] 

### Return type

[**MediaFileResponse**](MediaFileResponse.md)

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

