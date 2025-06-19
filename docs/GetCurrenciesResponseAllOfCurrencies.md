# GetCurrenciesResponseAllOfCurrencies


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | [**List[CurrencyInfo]**](CurrencyInfo.md) | Array of currency information | [optional] 

## Example

```python
from whmcs_client.models.get_currencies_response_all_of_currencies import GetCurrenciesResponseAllOfCurrencies

# TODO update the JSON string below
json = "{}"
# create an instance of GetCurrenciesResponseAllOfCurrencies from a JSON string
get_currencies_response_all_of_currencies_instance = GetCurrenciesResponseAllOfCurrencies.from_json(json)
# print the JSON string representation of the object
print(GetCurrenciesResponseAllOfCurrencies.to_json())

# convert the object into a dict
get_currencies_response_all_of_currencies_dict = get_currencies_response_all_of_currencies_instance.to_dict()
# create an instance of GetCurrenciesResponseAllOfCurrencies from a dict
get_currencies_response_all_of_currencies_from_dict = GetCurrenciesResponseAllOfCurrencies.from_dict(get_currencies_response_all_of_currencies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


