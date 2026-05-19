# GetAffiliatesResponseAllOfAffiliates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliate** | [**List[AffiliateInfo]**](AffiliateInfo.md) | The affiliates entries returned | [optional] 

## Example

```python
from whmcs_client.models.get_affiliates_response_all_of_affiliates import GetAffiliatesResponseAllOfAffiliates

# TODO update the JSON string below
json = "{}"
# create an instance of GetAffiliatesResponseAllOfAffiliates from a JSON string
get_affiliates_response_all_of_affiliates_instance = GetAffiliatesResponseAllOfAffiliates.from_json(json)
# print the JSON string representation of the object
print(GetAffiliatesResponseAllOfAffiliates.to_json())

# convert the object into a dict
get_affiliates_response_all_of_affiliates_dict = get_affiliates_response_all_of_affiliates_instance.to_dict()
# create an instance of GetAffiliatesResponseAllOfAffiliates from a dict
get_affiliates_response_all_of_affiliates_from_dict = GetAffiliatesResponseAllOfAffiliates.from_dict(get_affiliates_response_all_of_affiliates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


