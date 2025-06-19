# CurrencyInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The currency ID | [optional] 
**code** | **str** | The currency code (e.g., USD, EUR, GBP) | [optional] 
**prefix** | **str** | The currency prefix symbol (e.g., $, €, £) | [optional] 
**suffix** | **str** | The currency suffix (e.g., \&quot; USD\&quot;) | [optional] 
**format** | **int** | The currency format setting | [optional] 
**rate** | **str** | The currency exchange rate | [optional] 

## Example

```python
from whmcs_client.models.currency_info import CurrencyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyInfo from a JSON string
currency_info_instance = CurrencyInfo.from_json(json)
# print the JSON string representation of the object
print(CurrencyInfo.to_json())

# convert the object into a dict
currency_info_dict = currency_info_instance.to_dict()
# create an instance of CurrencyInfo from a dict
currency_info_from_dict = CurrencyInfo.from_dict(currency_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


