# TldPricingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tld** | **str** | The TLD | [optional] 
**categories** | **List[str]** | The TLD categories | [optional] 
**addons** | [**TldPricingInfoAddons**](TldPricingInfoAddons.md) |  | [optional] 
**group** | **str** | The TLD group | [optional] 
**register** | **Dict[str, str]** | Registration pricing keyed by term | [optional] 
**transfer** | **Dict[str, str]** | Transfer pricing keyed by term | [optional] 
**renew** | **Dict[str, str]** | Renewal pricing keyed by term | [optional] 
**grace_period** | [**TldPricingPeriodInfo**](TldPricingPeriodInfo.md) |  | [optional] 
**redemption_period** | [**TldPricingPeriodInfo**](TldPricingPeriodInfo.md) |  | [optional] 

## Example

```python
from whmcs_client.models.tld_pricing_info import TldPricingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TldPricingInfo from a JSON string
tld_pricing_info_instance = TldPricingInfo.from_json(json)
# print the JSON string representation of the object
print(TldPricingInfo.to_json())

# convert the object into a dict
tld_pricing_info_dict = tld_pricing_info_instance.to_dict()
# create an instance of TldPricingInfo from a dict
tld_pricing_info_from_dict = TldPricingInfo.from_dict(tld_pricing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


