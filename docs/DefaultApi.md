# whmcs_client.DefaultApi

All URIs are relative to *https://your-whmcs-instance.com/includes*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_post**](DefaultApi.md#api_post) | **POST** /api.php | Execute WHMCS API action


# **api_post**
> WHMCSSuccessResponse api_post(api_post_request)

Execute WHMCS API action

Executes a WHMCS API action. The specific action is determined by the 'action' field
in the request body. Different actions have different required and optional parameters.


### Example


```python
import whmcs_client
from whmcs_client.models.api_post_request import ApiPostRequest
from whmcs_client.models.whmcs_success_response import WHMCSSuccessResponse
from whmcs_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://your-whmcs-instance.com/includes
# See configuration.py for a list of all supported configuration parameters.
configuration = whmcs_client.Configuration(
    host = "https://your-whmcs-instance.com/includes"
)


# Enter a context with an instance of the API client
with whmcs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = whmcs_client.DefaultApi(api_client)
    api_post_request = whmcs_client.ApiPostRequest() # ApiPostRequest | 

    try:
        # Execute WHMCS API action
        api_response = api_instance.api_post(api_post_request)
        print("The response of DefaultApi->api_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_post_request** | [**ApiPostRequest**](ApiPostRequest.md)|  | 

### Return type

[**WHMCSSuccessResponse**](WHMCSSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request - Invalid parameters or malformed request |  -  |
**401** | Authentication failed |  -  |
**403** | Access denied - Insufficient permissions |  -  |
**404** | Resource not found |  -  |
**422** | Validation error - Required fields missing or invalid |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

