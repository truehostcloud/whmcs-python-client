# InvoiceItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The line item ID | [optional] 
**type** | **str** | The line item type (e.g., Hosting, Domain) | [optional] 
**relid** | **int** | The related service or domain ID | [optional] 
**description** | **str** | Human-readable description including billing period | [optional] 
**amount** | **str** | The line item amount | [optional] 
**taxed** | **int** | Whether the item is taxed (0 or 1) | [optional] 

## Example

```python
from whmcs_client.models.invoice_item import InvoiceItem

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceItem from a JSON string
invoice_item_instance = InvoiceItem.from_json(json)
# print the JSON string representation of the object
print(InvoiceItem.to_json())

# convert the object into a dict
invoice_item_dict = invoice_item_instance.to_dict()
# create an instance of InvoiceItem from a dict
invoice_item_from_dict = InvoiceItem.from_dict(invoice_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


