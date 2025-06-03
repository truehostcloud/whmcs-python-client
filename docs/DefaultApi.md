# whmcs_client.DefaultApi

All URIs are relative to *https://your-whmcs-instance.com/includes*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_post**](DefaultApi.md#api_post) | **POST** /api.php | WHMCS API endpoint

# **api_post**
> WHMCSSuccessResponse api_post()

WHMCS API endpoint

Main WHMCS API endpoint that accepts various actions based on the 'action' parameter. Each action has its own schema with specific required and optional fields. 

### Example
```python
from __future__ import print_function
import time
import whmcs_client
from whmcs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = whmcs_client.DefaultApi()

try:
    # WHMCS API endpoint
    api_response = api_instance.api_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WHMCSSuccessResponse**](WHMCSSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

