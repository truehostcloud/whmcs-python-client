# GetCurrenciesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**message** | **str** | Response message | [optional] 
**totalresults** | **int** | The total number of currencies available | [optional] 
**currencies** | [**GetCurrenciesResponseAllOfCurrencies**](GetCurrenciesResponseAllOfCurrencies.md) |  | [optional] 

## Example

```python
from whmcs_client.models.get_currencies_response import GetCurrenciesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCurrenciesResponse from a JSON string
get_currencies_response_instance = GetCurrenciesResponse.from_json(json)
# print the JSON string representation of the object
print(GetCurrenciesResponse.to_json())

# convert the object into a dict
get_currencies_response_dict = get_currencies_response_instance.to_dict()
# create an instance of GetCurrenciesResponse from a dict
get_currencies_response_from_dict = GetCurrenciesResponse.from_dict(get_currencies_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


