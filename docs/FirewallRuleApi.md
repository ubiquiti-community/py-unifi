# openapi_client.FirewallRuleApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_firewall_rule**](FirewallRuleApi.md#create_firewall_rule) | **POST** /rest/firewallrule | 
[**delete_firewall_rule**](FirewallRuleApi.md#delete_firewall_rule) | **DELETE** /rest/firewallrule/{id} | 
[**get_firewall_rule**](FirewallRuleApi.md#get_firewall_rule) | **GET** /rest/firewallrule/{id} | 
[**list_firewall_rule**](FirewallRuleApi.md#list_firewall_rule) | **GET** /rest/firewallrule | 
[**update_firewall_rule**](FirewallRuleApi.md#update_firewall_rule) | **PUT** /rest/firewallrule/{id} | 


# **create_firewall_rule**
> FirewallRuleResponse create_firewall_rule(firewall_rule=firewall_rule)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.firewall_rule import FirewallRule
from openapi_client.models.firewall_rule_response import FirewallRuleResponse
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
    api_instance = openapi_client.FirewallRuleApi(api_client)
    firewall_rule = openapi_client.FirewallRule() # FirewallRule |  (optional)

    try:
        api_response = api_instance.create_firewall_rule(firewall_rule=firewall_rule)
        print("The response of FirewallRuleApi->create_firewall_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallRuleApi->create_firewall_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_rule** | [**FirewallRule**](FirewallRule.md)|  | [optional] 

### Return type

[**FirewallRuleResponse**](FirewallRuleResponse.md)

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

# **delete_firewall_rule**
> FirewallRuleResponse delete_firewall_rule(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.firewall_rule_response import FirewallRuleResponse
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
    api_instance = openapi_client.FirewallRuleApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.delete_firewall_rule(id)
        print("The response of FirewallRuleApi->delete_firewall_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallRuleApi->delete_firewall_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FirewallRuleResponse**](FirewallRuleResponse.md)

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

# **get_firewall_rule**
> FirewallRuleResponse get_firewall_rule(id)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.firewall_rule_response import FirewallRuleResponse
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
    api_instance = openapi_client.FirewallRuleApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_firewall_rule(id)
        print("The response of FirewallRuleApi->get_firewall_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallRuleApi->get_firewall_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FirewallRuleResponse**](FirewallRuleResponse.md)

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

# **list_firewall_rule**
> FirewallRuleResponse list_firewall_rule()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.firewall_rule_response import FirewallRuleResponse
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
    api_instance = openapi_client.FirewallRuleApi(api_client)

    try:
        api_response = api_instance.list_firewall_rule()
        print("The response of FirewallRuleApi->list_firewall_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallRuleApi->list_firewall_rule: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FirewallRuleResponse**](FirewallRuleResponse.md)

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

# **update_firewall_rule**
> FirewallRuleResponse update_firewall_rule(id, firewall_rule_update_request=firewall_rule_update_request)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.firewall_rule_response import FirewallRuleResponse
from openapi_client.models.firewall_rule_update_request import FirewallRuleUpdateRequest
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
    api_instance = openapi_client.FirewallRuleApi(api_client)
    id = 'id_example' # str | 
    firewall_rule_update_request = openapi_client.FirewallRuleUpdateRequest() # FirewallRuleUpdateRequest |  (optional)

    try:
        api_response = api_instance.update_firewall_rule(id, firewall_rule_update_request=firewall_rule_update_request)
        print("The response of FirewallRuleApi->update_firewall_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallRuleApi->update_firewall_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **firewall_rule_update_request** | [**FirewallRuleUpdateRequest**](FirewallRuleUpdateRequest.md)|  | [optional] 

### Return type

[**FirewallRuleResponse**](FirewallRuleResponse.md)

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

