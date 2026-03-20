# GetInvoicesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**message** | **str** | Response message | [optional] 
**totalresults** | **int** | The total number of results available | [optional] 
**startnumber** | **int** | The starting number for the returned results | [optional] 
**numreturned** | **int** | The number of results returned | [optional] 
**invoices** | **object** | The invoices collection | [optional] 

## Example

```python
from whmcs_client.models.get_invoices_response import GetInvoicesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoicesResponse from a JSON string
get_invoices_response_instance = GetInvoicesResponse.from_json(json)
# print the JSON string representation of the object
print(GetInvoicesResponse.to_json())

# convert the object into a dict
get_invoices_response_dict = get_invoices_response_instance.to_dict()
# create an instance of GetInvoicesResponse from a dict
get_invoices_response_from_dict = GetInvoicesResponse.from_dict(get_invoices_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


