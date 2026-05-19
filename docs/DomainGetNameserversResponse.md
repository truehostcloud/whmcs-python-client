# DomainGetNameserversResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**message** | **str** | Response message | [optional] 
**ns1** | **str** | The first nameserver on the domain | [optional] 
**ns2** | **str** | The second nameserver on the domain | [optional] 
**ns3** | **str** | The third nameserver on the domain | [optional] 
**ns4** | **str** | The fourth nameserver on the domain | [optional] 
**ns5** | **str** | The fifth nameserver on the domain | [optional] 

## Example

```python
from whmcs_client.models.domain_get_nameservers_response import DomainGetNameserversResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainGetNameserversResponse from a JSON string
domain_get_nameservers_response_instance = DomainGetNameserversResponse.from_json(json)
# print the JSON string representation of the object
print(DomainGetNameserversResponse.to_json())

# convert the object into a dict
domain_get_nameservers_response_dict = domain_get_nameservers_response_instance.to_dict()
# create an instance of DomainGetNameserversResponse from a dict
domain_get_nameservers_response_from_dict = DomainGetNameserversResponse.from_dict(domain_get_nameservers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


