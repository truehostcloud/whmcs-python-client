# AffiliateInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The affiliate ID | [optional] 
**var_date** | **date** | The affiliate date | [optional] 
**clientid** | **int** | The client ID | [optional] 
**visitors** | **int** | The visitor count | [optional] 
**paytype** | **str** | The affiliate pay type | [optional] 
**payamount** | **float** | The payout amount | [optional] 
**onetime** | **int** | Whether the affiliate is one time | [optional] 
**balance** | **float** | The current balance | [optional] 
**withdrawn** | **float** | The withdrawn amount | [optional] 
**created_at** | **str** | The creation timestamp | [optional] 
**updated_at** | **str** | The last update timestamp | [optional] 

## Example

```python
from whmcs_client.models.affiliate_info import AffiliateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AffiliateInfo from a JSON string
affiliate_info_instance = AffiliateInfo.from_json(json)
# print the JSON string representation of the object
print(AffiliateInfo.to_json())

# convert the object into a dict
affiliate_info_dict = affiliate_info_instance.to_dict()
# create an instance of AffiliateInfo from a dict
affiliate_info_from_dict = AffiliateInfo.from_dict(affiliate_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


