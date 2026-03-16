# ClientDetailsStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numdueinvoices** | **int** |  | [optional] 
**dueinvoicesbalance** | **str** |  | [optional] 
**incredit** | **bool** |  | [optional] 
**creditbalance** | **str** |  | [optional] 
**gross_revenue** | **str** |  | [optional] 
**expenses** | **str** |  | [optional] 
**income** | **str** |  | [optional] 
**numoverdueinvoices** | **int** |  | [optional] 
**overdueinvoicesbalance** | **str** |  | [optional] 
**num_draft_invoices** | **int** |  | [optional] 
**draft_invoices_balance** | **str** |  | [optional] 
**numunpaidinvoices** | **int** |  | [optional] 
**unpaidinvoicesamount** | **str** |  | [optional] 
**numpaidinvoices** | **int** |  | [optional] 
**paidinvoicesamount** | **str** |  | [optional] 
**numcancelledinvoices** | **int** |  | [optional] 
**cancelledinvoicesamount** | **str** |  | [optional] 
**numrefundedinvoices** | **int** |  | [optional] 
**refundedinvoicesamount** | **str** |  | [optional] 
**numcollectionsinvoices** | **int** |  | [optional] 
**collectionsinvoicesamount** | **str** |  | [optional] 
**numpaymentpendinginvoices** | **int** |  | [optional] 
**paymentpendinginvoicesamount** | **str** |  | [optional] 
**productsnumactivehosting** | **int** |  | [optional] 
**productsnumhosting** | **int** |  | [optional] 
**productsnumactivereseller** | **int** |  | [optional] 
**productsnumreseller** | **int** |  | [optional] 
**productsnumactiveservers** | **int** |  | [optional] 
**productsnumservers** | **int** |  | [optional] 
**productsnumactiveother** | **int** |  | [optional] 
**productsnumother** | **int** |  | [optional] 
**productsnumactive** | **int** |  | [optional] 
**productsnumtotal** | **int** |  | [optional] 
**numactivedomains** | **int** |  | [optional] 
**numdomains** | **int** |  | [optional] 
**numacceptedquotes** | **int** |  | [optional] 
**numquotes** | **int** |  | [optional] 
**numtickets** | **int** |  | [optional] 
**numactivetickets** | **int** |  | [optional] 
**numaffiliatesignups** | **int** |  | [optional] 
**is_affiliate** | **bool** |  | [optional] 

## Example

```python
from whmcs_client.models.client_details_stats import ClientDetailsStats

# TODO update the JSON string below
json = "{}"
# create an instance of ClientDetailsStats from a JSON string
client_details_stats_instance = ClientDetailsStats.from_json(json)
# print the JSON string representation of the object
print(ClientDetailsStats.to_json())

# convert the object into a dict
client_details_stats_dict = client_details_stats_instance.to_dict()
# create an instance of ClientDetailsStats from a dict
client_details_stats_from_dict = ClientDetailsStats.from_dict(client_details_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


