# InvoiceCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice** | [**InvoiceCollectionInvoice**](InvoiceCollectionInvoice.md) |  | [optional] 

## Example

```python
from whmcs_client.models.invoice_collection import InvoiceCollection

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceCollection from a JSON string
invoice_collection_instance = InvoiceCollection.from_json(json)
# print the JSON string representation of the object
print(InvoiceCollection.to_json())

# convert the object into a dict
invoice_collection_dict = invoice_collection_instance.to_dict()
# create an instance of InvoiceCollection from a dict
invoice_collection_from_dict = InvoiceCollection.from_dict(invoice_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


