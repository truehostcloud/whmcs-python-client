# GetTLDPricingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**message** | **str** | Response message | [optional] 
**currency** | [**CurrencyInfo**](CurrencyInfo.md) |  | [optional] 
**pricing** | [**Dict[str, TldPricingInfo]**](TldPricingInfo.md) |  | [optional] 

## Example

```python
from whmcs_client.models.get_tld_pricing_response import GetTLDPricingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTLDPricingResponse from a JSON string
get_tld_pricing_response_instance = GetTLDPricingResponse.from_json(json)
# print the JSON string representation of the object
print(GetTLDPricingResponse.to_json())

# convert the object into a dict
get_tld_pricing_response_dict = get_tld_pricing_response_instance.to_dict()
# create an instance of GetTLDPricingResponse from a dict
get_tld_pricing_response_from_dict = GetTLDPricingResponse.from_dict(get_tld_pricing_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


