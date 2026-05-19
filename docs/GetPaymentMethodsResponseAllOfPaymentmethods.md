# GetPaymentMethodsResponseAllOfPaymentmethods


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paymentmethod** | [**List[PaymentMethodInfo]**](PaymentMethodInfo.md) | An array of available payment methods | [optional] 

## Example

```python
from whmcs_client.models.get_payment_methods_response_all_of_paymentmethods import GetPaymentMethodsResponseAllOfPaymentmethods

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentMethodsResponseAllOfPaymentmethods from a JSON string
get_payment_methods_response_all_of_paymentmethods_instance = GetPaymentMethodsResponseAllOfPaymentmethods.from_json(json)
# print the JSON string representation of the object
print(GetPaymentMethodsResponseAllOfPaymentmethods.to_json())

# convert the object into a dict
get_payment_methods_response_all_of_paymentmethods_dict = get_payment_methods_response_all_of_paymentmethods_instance.to_dict()
# create an instance of GetPaymentMethodsResponseAllOfPaymentmethods from a dict
get_payment_methods_response_all_of_paymentmethods_from_dict = GetPaymentMethodsResponseAllOfPaymentmethods.from_dict(get_payment_methods_response_all_of_paymentmethods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


