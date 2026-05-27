# TldPricingPeriodInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **int** | The number of days in the period | [optional] 
**price** | **str** | The price for the period | [optional] 

## Example

```python
from whmcs_client.models.tld_pricing_period_info import TldPricingPeriodInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TldPricingPeriodInfo from a JSON string
tld_pricing_period_info_instance = TldPricingPeriodInfo.from_json(json)
# print the JSON string representation of the object
print(TldPricingPeriodInfo.to_json())

# convert the object into a dict
tld_pricing_period_info_dict = tld_pricing_period_info_instance.to_dict()
# create an instance of TldPricingPeriodInfo from a dict
tld_pricing_period_info_from_dict = TldPricingPeriodInfo.from_dict(tld_pricing_period_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


