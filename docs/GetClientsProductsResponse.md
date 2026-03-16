# GetClientsProductsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**message** | **str** | Response message | [optional] 
**clientid** | [**GetClientsProductsResponseAllOfClientid**](GetClientsProductsResponseAllOfClientid.md) |  | [optional] 
**serviceid** | [**GetClientsProductsResponseAllOfServiceid**](GetClientsProductsResponseAllOfServiceid.md) |  | [optional] 
**pid** | [**GetClientsProductsResponseAllOfPid**](GetClientsProductsResponseAllOfPid.md) |  | [optional] 
**domain** | **str** |  | [optional] 
**totalresults** | **int** | The total number of results available | [optional] 
**startnumber** | **int** | The starting number for the returned results | [optional] 
**numreturned** | **int** | The number of results returned | [optional] 
**products** | [**ProductCollection**](ProductCollection.md) |  | [optional] 

## Example

```python
from whmcs_client.models.get_clients_products_response import GetClientsProductsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsProductsResponse from a JSON string
get_clients_products_response_instance = GetClientsProductsResponse.from_json(json)
# print the JSON string representation of the object
print(GetClientsProductsResponse.to_json())

# convert the object into a dict
get_clients_products_response_dict = get_clients_products_response_instance.to_dict()
# create an instance of GetClientsProductsResponse from a dict
get_clients_products_response_from_dict = GetClientsProductsResponse.from_dict(get_clients_products_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


