# GetTransactionsResponseAllOfTransactions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**List[TransactionInfo]**](TransactionInfo.md) | An array of transactions matching the criteria passed | [optional] 

## Example

```python
from whmcs_client.models.get_transactions_response_all_of_transactions import GetTransactionsResponseAllOfTransactions

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionsResponseAllOfTransactions from a JSON string
get_transactions_response_all_of_transactions_instance = GetTransactionsResponseAllOfTransactions.from_json(json)
# print the JSON string representation of the object
print(GetTransactionsResponseAllOfTransactions.to_json())

# convert the object into a dict
get_transactions_response_all_of_transactions_dict = get_transactions_response_all_of_transactions_instance.to_dict()
# create an instance of GetTransactionsResponseAllOfTransactions from a dict
get_transactions_response_all_of_transactions_from_dict = GetTransactionsResponseAllOfTransactions.from_dict(get_transactions_response_all_of_transactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


