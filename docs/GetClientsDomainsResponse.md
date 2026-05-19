# GetClientsDomainsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**message** | **str** | Response message | [optional] 
**clientid** | **int** | The specific client id searched for | [optional] 
**domainid** | **int** | The specific domain id searched for | [optional] 
**totalresults** | **int** | The total number of results available | [optional] 
**startnumber** | **int** | The starting number for the returned results | [optional] 
**numreturned** | **int** | The total number of results returned | [optional] 
**domains** | [**GetClientsDomainsResponseAllOfDomains**](GetClientsDomainsResponseAllOfDomains.md) |  | [optional] 

## Example

```python
from whmcs_client.models.get_clients_domains_response import GetClientsDomainsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsDomainsResponse from a JSON string
get_clients_domains_response_instance = GetClientsDomainsResponse.from_json(json)
# print the JSON string representation of the object
print(GetClientsDomainsResponse.to_json())

# convert the object into a dict
get_clients_domains_response_dict = get_clients_domains_response_instance.to_dict()
# create an instance of GetClientsDomainsResponse from a dict
get_clients_domains_response_from_dict = GetClientsDomainsResponse.from_dict(get_clients_domains_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


