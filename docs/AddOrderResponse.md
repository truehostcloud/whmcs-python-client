# AddOrderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | The result of the operation | 
**action** | **str** | Always &#39;AddOrder&#39; for AddOrder responses | 
**warnings** | **List[str]** | Any warning messages | [optional] 
**message** | **str** | Success or error message | [optional] 
**orderid** | **str** | The Order ID for the created order | [optional] 
**serviceids** | **str** | The Service ID(s) created by the order | [optional] 
**addonids** | **str** | The Addon ID(s) created by the order | [optional] 
**domainids** | **str** | The Domain ID(s) created by the order | [optional] 
**invoiceid** | **int** | The Invoice ID created for the order | [optional] 

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


