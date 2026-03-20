# ProductInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The product name | [optional] 
**recurringamount** | **str** | The recurring amount | [optional] 
**billingcycle** | **str** | The billing cycle | [optional] 
**nextduedate** | **str** | The next due date (YYYY-MM-DD, may be 0000-00-00) | [optional] 
**status** | **str** | The service status | [optional] 

## Example

```python
from whmcs_client.models.product_info import ProductInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProductInfo from a JSON string
product_info_instance = ProductInfo.from_json(json)
# print the JSON string representation of the object
print(ProductInfo.to_json())

# convert the object into a dict
product_info_dict = product_info_instance.to_dict()
# create an instance of ProductInfo from a dict
product_info_from_dict = ProductInfo.from_dict(product_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


