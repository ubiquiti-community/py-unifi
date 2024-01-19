# openapi_client.SettingSnmpApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_snmp**](SettingSnmpApi.md#get_setting_snmp) | **GET** /get/setting/snmp | 
[**update_setting_snmp**](SettingSnmpApi.md#update_setting_snmp) | **PUT** /set/setting/snmp | 


# **get_setting_snmp**
> SettingSnmpResponse get_setting_snmp()



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_snmp_response import SettingSnmpResponse
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
    api_instance = openapi_client.SettingSnmpApi(api_client)

    try:
        api_response = api_instance.get_setting_snmp()
        print("The response of SettingSnmpApi->get_setting_snmp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingSnmpApi->get_setting_snmp: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingSnmpResponse**](SettingSnmpResponse.md)

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

# **update_setting_snmp**
> SettingSnmpResponse update_setting_snmp(setting_snmp=setting_snmp)



### Example


```python
import time
import os
import openapi_client
from openapi_client.models.setting_snmp import SettingSnmp
from openapi_client.models.setting_snmp_response import SettingSnmpResponse
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
    api_instance = openapi_client.SettingSnmpApi(api_client)
    setting_snmp = openapi_client.SettingSnmp() # SettingSnmp |  (optional)

    try:
        api_response = api_instance.update_setting_snmp(setting_snmp=setting_snmp)
        print("The response of SettingSnmpApi->update_setting_snmp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingSnmpApi->update_setting_snmp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_snmp** | [**SettingSnmp**](SettingSnmp.md)|  | [optional] 

### Return type

[**SettingSnmpResponse**](SettingSnmpResponse.md)

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

