# DomainInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The domain ID | [optional] 
**userid** | **int** | The client ID that owns the domain | [optional] 
**orderid** | **int** | The order ID associated with the domain | [optional] 
**regtype** | **str** | The registration type, such as Register or Transfer | [optional] 
**domainname** | **str** | The domain name | [optional] 
**registrar** | **str** | The registrar module name | [optional] 
**regperiod** | **int** | The registration period | [optional] 
**firstpaymentamount** | **float** | The first payment amount | [optional] 
**recurringamount** | **float** | The recurring amount | [optional] 
**paymentmethod** | **str** | The payment method code | [optional] 
**paymentmethodname** | **str** | The payment method name | [optional] 
**regdate** | **date** | The registration date | [optional] 
**expirydate** | **date** | The expiration date | [optional] 
**nextduedate** | **date** | The next due date | [optional] 
**status** | **str** | The domain status | [optional] 
**subscriptionid** | **str** | The subscription identifier | [optional] 
**promoid** | **int** | The promotion ID | [optional] 
**dnsmanagement** | **bool** | Whether DNS management is enabled | [optional] 
**emailforwarding** | **bool** | Whether email forwarding is enabled | [optional] 
**idprotection** | **bool** | Whether ID protection is enabled | [optional] 
**donotrenew** | **bool** | Whether the domain should not renew | [optional] 
**notes** | **str** | Internal notes for the domain | [optional] 

## Example

```python
from whmcs_client.models.domain_info import DomainInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DomainInfo from a JSON string
domain_info_instance = DomainInfo.from_json(json)
# print the JSON string representation of the object
print(DomainInfo.to_json())

# convert the object into a dict
domain_info_dict = domain_info_instance.to_dict()
# create an instance of DomainInfo from a dict
domain_info_from_dict = DomainInfo.from_dict(domain_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


