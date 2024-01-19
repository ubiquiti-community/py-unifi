# unifi_client.SettingMagicSiteToSiteVpnApi

All URIs are relative to *https://unifi.ui.com/proxy/network/api/s/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_magic_site_to_site_vpn**](SettingMagicSiteToSiteVpnApi.md#get_setting_magic_site_to_site_vpn) | **GET** /get/setting/magic_site_to_site_vpn | 
[**update_setting_magic_site_to_site_vpn**](SettingMagicSiteToSiteVpnApi.md#update_setting_magic_site_to_site_vpn) | **PUT** /set/setting/magic_site_to_site_vpn | 


# **get_setting_magic_site_to_site_vpn**
> SettingMagicSiteToSiteVpnResponse get_setting_magic_site_to_site_vpn()



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_magic_site_to_site_vpn_response import SettingMagicSiteToSiteVpnResponse
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
    api_instance = unifi_client.SettingMagicSiteToSiteVpnApi(api_client)

    try:
        api_response = await api_instance.get_setting_magic_site_to_site_vpn()
        print("The response of SettingMagicSiteToSiteVpnApi->get_setting_magic_site_to_site_vpn:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingMagicSiteToSiteVpnApi->get_setting_magic_site_to_site_vpn: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingMagicSiteToSiteVpnResponse**](SettingMagicSiteToSiteVpnResponse.md)

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

# **update_setting_magic_site_to_site_vpn**
> SettingMagicSiteToSiteVpnResponse update_setting_magic_site_to_site_vpn(setting_magic_site_to_site_vpn=setting_magic_site_to_site_vpn)



### Example


```python
import time
import os
import unifi_client
from unifi_client.models.setting_magic_site_to_site_vpn import SettingMagicSiteToSiteVpn
from unifi_client.models.setting_magic_site_to_site_vpn_response import SettingMagicSiteToSiteVpnResponse
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
    api_instance = unifi_client.SettingMagicSiteToSiteVpnApi(api_client)
    setting_magic_site_to_site_vpn = unifi_client.SettingMagicSiteToSiteVpn() # SettingMagicSiteToSiteVpn |  (optional)

    try:
        api_response = await api_instance.update_setting_magic_site_to_site_vpn(setting_magic_site_to_site_vpn=setting_magic_site_to_site_vpn)
        print("The response of SettingMagicSiteToSiteVpnApi->update_setting_magic_site_to_site_vpn:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingMagicSiteToSiteVpnApi->update_setting_magic_site_to_site_vpn: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_magic_site_to_site_vpn** | [**SettingMagicSiteToSiteVpn**](SettingMagicSiteToSiteVpn.md)|  | [optional] 

### Return type

[**SettingMagicSiteToSiteVpnResponse**](SettingMagicSiteToSiteVpnResponse.md)

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

