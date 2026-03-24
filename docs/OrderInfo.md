# OrderInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The order ID | [optional] 
**ordernum** | **str** | The order number | [optional] 
**var_date** | **str** | The order date (YYYY-MM-DD HH:MM:SS) | [optional] 
**amount** | **str** | The order total amount | [optional] 
**paymentmethod** | **str** | The payment method identifier | [optional] 
**invoiceid** | **int** | The linked invoice ID | [optional] 
**status** | **str** | The order status (Active, Pending, Fraud, Cancelled) | [optional] 
**name** | **str** | The client name on the order | [optional] 
**lineitems** | **object** | The order line items collection | [optional] 

## Example

```python
from whmcs_client.models.order_info import OrderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderInfo from a JSON string
order_info_instance = OrderInfo.from_json(json)
# print the JSON string representation of the object
print(OrderInfo.to_json())

# convert the object into a dict
order_info_dict = order_info_instance.to_dict()
# create an instance of OrderInfo from a dict
order_info_from_dict = OrderInfo.from_dict(order_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


