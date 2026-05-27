# GetProductsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**message** | **str** | Response message | [optional] 
**totalresults** | **int** | The total number of results available | [optional] 
**startnumber** | **int** | The starting number for the returned results | [optional] 
**numreturned** | **int** | The number of results returned | [optional] 
**products** | **object** | The products collection | [optional] 

## Example

```python
from whmcs_client.models.get_products_response import GetProductsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductsResponse from a JSON string
get_products_response_instance = GetProductsResponse.from_json(json)
# print the JSON string representation of the object
print(GetProductsResponse.to_json())

# convert the object into a dict
get_products_response_dict = get_products_response_instance.to_dict()
# create an instance of GetProductsResponse from a dict
get_products_response_from_dict = GetProductsResponse.from_dict(get_products_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


