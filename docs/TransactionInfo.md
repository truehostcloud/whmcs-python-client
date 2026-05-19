# TransactionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The transaction ID | [optional] 
**userid** | **int** | The client ID | [optional] 
**currency** | **int** | The currency ID | [optional] 
**gateway** | **str** | The payment gateway | [optional] 
**var_date** | **str** | The transaction date and time | [optional] 
**description** | **str** | The transaction description | [optional] 
**amountin** | **float** | The amount in | [optional] 
**fees** | **float** | The transaction fees | [optional] 
**amountout** | **float** | The amount out | [optional] 
**rate** | **str** | The exchange rate | [optional] 
**transid** | **str** | The transaction identifier | [optional] 
**invoiceid** | **int** | The invoice ID | [optional] 
**refundid** | **int** | The refund ID | [optional] 

## Example

```python
from whmcs_client.models.transaction_info import TransactionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionInfo from a JSON string
transaction_info_instance = TransactionInfo.from_json(json)
# print the JSON string representation of the object
print(TransactionInfo.to_json())

# convert the object into a dict
transaction_info_dict = transaction_info_instance.to_dict()
# create an instance of TransactionInfo from a dict
transaction_info_from_dict = TransactionInfo.from_dict(transaction_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


