# GetClientsDomainsResponseAllOfDomainsOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | [**List[DomainInfo]**](DomainInfo.md) | Array of domains that match the criteria passed | [optional] 

## Example

```python
from whmcs_client.models.get_clients_domains_response_all_of_domains_one_of import GetClientsDomainsResponseAllOfDomainsOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsDomainsResponseAllOfDomainsOneOf from a JSON string
get_clients_domains_response_all_of_domains_one_of_instance = GetClientsDomainsResponseAllOfDomainsOneOf.from_json(json)
# print the JSON string representation of the object
print(GetClientsDomainsResponseAllOfDomainsOneOf.to_json())

# convert the object into a dict
get_clients_domains_response_all_of_domains_one_of_dict = get_clients_domains_response_all_of_domains_one_of_instance.to_dict()
# create an instance of GetClientsDomainsResponseAllOfDomainsOneOf from a dict
get_clients_domains_response_all_of_domains_one_of_from_dict = GetClientsDomainsResponseAllOfDomainsOneOf.from_dict(get_clients_domains_response_all_of_domains_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


