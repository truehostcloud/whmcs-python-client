# TldPricingInfoAddons


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns** | **bool** | Whether DNS addon pricing is available | [optional] 
**email** | **bool** | Whether email addon pricing is available | [optional] 
**idprotect** | **bool** | Whether ID protection addon pricing is available | [optional] 

## Example

```python
from whmcs_client.models.tld_pricing_info_addons import TldPricingInfoAddons

# TODO update the JSON string below
json = "{}"
# create an instance of TldPricingInfoAddons from a JSON string
tld_pricing_info_addons_instance = TldPricingInfoAddons.from_json(json)
# print the JSON string representation of the object
print(TldPricingInfoAddons.to_json())

# convert the object into a dict
tld_pricing_info_addons_dict = tld_pricing_info_addons_instance.to_dict()
# create an instance of TldPricingInfoAddons from a dict
tld_pricing_info_addons_from_dict = TldPricingInfoAddons.from_dict(tld_pricing_info_addons_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


