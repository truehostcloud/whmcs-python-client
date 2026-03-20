# InvoiceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The invoice ID | [optional] 
**userid** | **int** | The client ID linked to the invoice | [optional] 
**var_date** | **str** | The invoice date (YYYY-MM-DD) | [optional] 
**duedate** | **str** | The invoice due date (YYYY-MM-DD, may be 0000-00-00) | [optional] 
**var_date** | **str** | Fallback invoice date field | [optional] 
**created_at** | **str** | Invoice creation timestamp | [optional] 
**total** | **str** | The invoice total amount | [optional] 
**status** | **str** | The invoice status | [optional] 
**currencycode** | **str** | The invoice currency code | [optional] 

## Example

```python
from whmcs_client.models.invoice_info import InvoiceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceInfo from a JSON string
invoice_info_instance = InvoiceInfo.from_json(json)
# print the JSON string representation of the object
print(InvoiceInfo.to_json())

# convert the object into a dict
invoice_info_dict = invoice_info_instance.to_dict()
# create an instance of InvoiceInfo from a dict
invoice_info_from_dict = InvoiceInfo.from_dict(invoice_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


