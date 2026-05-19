# GetClientsProductsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**message** | **str** | Response message | [optional] 
**products** | **object** | The products collection | [optional] 

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


