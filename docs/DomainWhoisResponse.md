# DomainWhoisResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**message** | **str** | Response message | [optional] 
**status** | **str** | The registration status | [optional] 
**whois** | **str** | Whois server response | [optional] 

## Example

```python
from whmcs_client.models.domain_whois_response import DomainWhoisResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainWhoisResponse from a JSON string
domain_whois_response_instance = DomainWhoisResponse.from_json(json)
# print the JSON string representation of the object
print(DomainWhoisResponse.to_json())

# convert the object into a dict
domain_whois_response_dict = domain_whois_response_instance.to_dict()
# create an instance of DomainWhoisResponse from a dict
domain_whois_response_from_dict = DomainWhoisResponse.from_dict(domain_whois_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


