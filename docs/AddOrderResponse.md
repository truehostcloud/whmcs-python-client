# AddOrderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**message** | **str** | Response message | [optional] 
**orderid** | **int** | The ID of the newly created order | [optional] 
**productids** | **List[int]** | Array of product IDs that were created | [optional] 
**addonids** | **List[int]** | Array of addon IDs that were created | [optional] 
**domainids** | **List[int]** | Array of domain IDs that were created | [optional] 
**invoiceid** | **int** | The invoice ID if an invoice was generated | [optional] 

## Example

```python
from whmcs_client.models.add_order_response import AddOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddOrderResponse from a JSON string
add_order_response_instance = AddOrderResponse.from_json(json)
# print the JSON string representation of the object
print(AddOrderResponse.to_json())

# convert the object into a dict
add_order_response_dict = add_order_response_instance.to_dict()
# create an instance of AddOrderResponse from a dict
add_order_response_from_dict = AddOrderResponse.from_dict(add_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


