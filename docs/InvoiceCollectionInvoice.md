# InvoiceCollectionInvoice

Array of invoice information or a single invoice object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The invoice ID | [optional] 
**userid** | **int** | The client ID linked to the invoice | [optional] 
**firstname** | **str** | The client first name | [optional] 
**lastname** | **str** | The client last name | [optional] 
**companyname** | **str** | The client company name | [optional] 
**invoicenum** | **str** | The invoice number | [optional] 
**var_date** | **date** | The invoice date | [optional] 
**duedate** | **date** | The invoice due date | [optional] 
**datepaid** | **str** | The invoice paid timestamp | [optional] 
**last_capture_attempt** | **str** | The last payment capture attempt timestamp | [optional] 
**date_refunded** | **str** | The invoice refund timestamp | [optional] 
**date_cancelled** | **str** | The invoice cancellation timestamp | [optional] 
**subtotal** | **str** | The invoice subtotal amount | [optional] 
**credit** | **str** | The invoice credit amount | [optional] 
**tax** | **str** | The invoice tax amount | [optional] 
**tax2** | **str** | The invoice secondary tax amount | [optional] 
**total** | **str** | The invoice total amount | [optional] 
**taxrate** | **str** | The invoice tax rate | [optional] 
**taxrate2** | **str** | The invoice secondary tax rate | [optional] 
**status** | **str** | The invoice status | [optional] 
**paymentmethod** | **str** | The invoice payment method | [optional] 
**paymethodid** | [**InvoiceInfoPaymethodid**](InvoiceInfoPaymethodid.md) |  | [optional] 
**notes** | **str** | Invoice notes | [optional] 
**created_at** | **str** | The invoice creation timestamp | [optional] 
**updated_at** | **str** | The invoice update timestamp | [optional] 
**currencycode** | **str** | The invoice currency code | [optional] 
**currencyprefix** | **str** | The invoice currency prefix | [optional] 
**currencysuffix** | **str** | The invoice currency suffix | [optional] 

## Example

```python
from whmcs_client.models.invoice_collection_invoice import InvoiceCollectionInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceCollectionInvoice from a JSON string
invoice_collection_invoice_instance = InvoiceCollectionInvoice.from_json(json)
# print the JSON string representation of the object
print(InvoiceCollectionInvoice.to_json())

# convert the object into a dict
invoice_collection_invoice_dict = invoice_collection_invoice_instance.to_dict()
# create an instance of InvoiceCollectionInvoice from a dict
invoice_collection_invoice_from_dict = InvoiceCollectionInvoice.from_dict(invoice_collection_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


