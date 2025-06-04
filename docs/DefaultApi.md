# whmcs_client.DefaultApi

All URIs are relative to *https://your-whmcs-instance.com/includes*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_client**](DefaultApi.md#add_client) | **POST** /AddClient | Add a new client
[**add_order**](DefaultApi.md#add_order) | **POST** /AddOrder | Create a new order
[**update_client**](DefaultApi.md#update_client) | **POST** /UpdateClient | Update client details

# **add_client**
> AddClientResponse add_client()

Add a new client

Creates a new client account in WHMCS

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
    # Add a new client
    api_response = api_instance.add_client()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_client: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AddClientResponse**](AddClientResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order**
> AddOrderResponse add_order()

Create a new order

Places a new order for products/services

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
    # Create a new order
    api_response = api_instance.add_order()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_order: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AddOrderResponse**](AddOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client**
> UpdateClientResponse update_client()

Update client details

Modifies an existing client's information

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
    # Update client details
    api_response = api_instance.update_client()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_client: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UpdateClientResponse**](UpdateClientResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

