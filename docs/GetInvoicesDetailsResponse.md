# GetInvoicesDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**message** | **str** | Response message | [optional] 
**totalresults** | **int** | The total number of results available | [optional] 
**startnumber** | **int** | The starting number for the returned results | [optional] 
**numreturned** | **int** | The number of results returned | [optional] 
**invoices** | **object** | The invoices collection with embedded line items | [optional] 

## Example

```python
from whmcs_client.models.get_invoices_details_response import GetInvoicesDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoicesDetailsResponse from a JSON string
get_invoices_details_response_instance = GetInvoicesDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(GetInvoicesDetailsResponse.to_json())

# convert the object into a dict
get_invoices_details_response_dict = get_invoices_details_response_instance.to_dict()
# create an instance of GetInvoicesDetailsResponse from a dict
get_invoices_details_response_from_dict = GetInvoicesDetailsResponse.from_dict(get_invoices_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


