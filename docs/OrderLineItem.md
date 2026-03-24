# OrderLineItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The line item type (product, domain, addon) | [optional] 
**product** | **str** | The product name | [optional] 
**domain** | **str** | The associated domain | [optional] 
**billingcycle** | **str** | The billing cycle | [optional] 
**amount** | **str** | The line item amount | [optional] 
**status** | **str** | The line item status | [optional] 

## Example

```python
from whmcs_client.models.order_line_item import OrderLineItem

# TODO update the JSON string below
json = "{}"
# create an instance of OrderLineItem from a JSON string
order_line_item_instance = OrderLineItem.from_json(json)
# print the JSON string representation of the object
print(OrderLineItem.to_json())

# convert the object into a dict
order_line_item_dict = order_line_item_instance.to_dict()
# create an instance of OrderLineItem from a dict
order_line_item_from_dict = OrderLineItem.from_dict(order_line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


