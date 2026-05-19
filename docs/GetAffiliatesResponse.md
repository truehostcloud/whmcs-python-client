# GetAffiliatesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**message** | **str** | Response message | [optional] 
**totalresults** | **int** | The total number of results available | [optional] 
**startnumber** | **int** | The starting number for the returned results | [optional] 
**numreturned** | **int** | The number of results returned | [optional] 
**affiliates** | [**GetAffiliatesResponseAllOfAffiliates**](GetAffiliatesResponseAllOfAffiliates.md) |  | [optional] 

## Example

```python
from whmcs_client.models.get_affiliates_response import GetAffiliatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAffiliatesResponse from a JSON string
get_affiliates_response_instance = GetAffiliatesResponse.from_json(json)
# print the JSON string representation of the object
print(GetAffiliatesResponse.to_json())

# convert the object into a dict
get_affiliates_response_dict = get_affiliates_response_instance.to_dict()
# create an instance of GetAffiliatesResponse from a dict
get_affiliates_response_from_dict = GetAffiliatesResponse.from_dict(get_affiliates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


