# PaymentMethodInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module** | **str** | The payment method module name | [optional] 
**displayname** | **str** | The payment method display name | [optional] 

## Example

```python
from whmcs_client.models.payment_method_info import PaymentMethodInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodInfo from a JSON string
payment_method_info_instance = PaymentMethodInfo.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodInfo.to_json())

# convert the object into a dict
payment_method_info_dict = payment_method_info_instance.to_dict()
# create an instance of PaymentMethodInfo from a dict
payment_method_info_from_dict = PaymentMethodInfo.from_dict(payment_method_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


