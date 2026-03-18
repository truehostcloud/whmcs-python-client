# ProductCollectionProduct

Array of product information or a single product object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The service ID | [optional] 
**qty** | **str** | The service quantity | [optional] 
**clientid** | **str** | The client ID | [optional] 
**orderid** | **str** | The order ID | [optional] 
**ordernumber** | **str** | The order number | [optional] 
**pid** | **str** | The product ID | [optional] 
**regdate** | **str** | The registration date (YYYY-MM-DD, may be 0000-00-00) | [optional] 
**name** | **str** | The product name | [optional] 
**translated_name** | **str** | The translated product name | [optional] 
**groupname** | **str** | The product group name | [optional] 
**translated_groupname** | **str** | The translated product group name | [optional] 
**domain** | **str** | The associated domain name | [optional] 
**dedicatedip** | **str** | The dedicated IP address | [optional] 
**serverid** | **str** | The server ID | [optional] 
**servername** | **str** | The server name | [optional] 
**serverip** | **str** | The server IP | [optional] 
**serverhostname** | **str** | The server hostname | [optional] 
**suspensionreason** | **str** | Suspension reason | [optional] 
**firstpaymentamount** | **str** | The first payment amount | [optional] 
**recurringamount** | **str** | The recurring amount | [optional] 
**paymentmethod** | **str** | The payment method | [optional] 
**paymentmethodname** | **str** | The human-readable payment method name | [optional] 
**billingcycle** | **str** | The billing cycle | [optional] 
**nextduedate** | **str** | The next due date (YYYY-MM-DD, may be 0000-00-00) | [optional] 
**status** | **str** | The service status | [optional] 
**username** | **str** | The service username | [optional] 
**password** | **str** | The service password placeholder | [optional] 
**subscriptionid** | **str** | The subscription ID | [optional] 
**promoid** | **str** | The promotion ID | [optional] 
**overideautosuspend** | **str** | Whether autosuspend is overridden | [optional] 
**overidesuspenduntil** | **str** | Suspend override until date | [optional] 
**ns1** | **str** | Nameserver 1 | [optional] 
**ns2** | **str** | Nameserver 2 | [optional] 
**assignedips** | **str** | Assigned IPs | [optional] 
**notes** | **str** | Product notes | [optional] 
**diskusage** | **str** | Disk usage | [optional] 
**disklimit** | **str** | Disk limit | [optional] 
**bwusage** | **str** | Bandwidth usage | [optional] 
**bwlimit** | **str** | Bandwidth limit | [optional] 
**lastupdate** | **str** | Last update timestamp | [optional] 
**customfields** | **Dict[str, object]** | Custom field values for the product | [optional] 
**configoptions** | **Dict[str, object]** | Configurable option values for the product | [optional] 

## Example

```python
from whmcs_client.models.product_collection_product import ProductCollectionProduct

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCollectionProduct from a JSON string
product_collection_product_instance = ProductCollectionProduct.from_json(json)
# print the JSON string representation of the object
print(ProductCollectionProduct.to_json())

# convert the object into a dict
product_collection_product_dict = product_collection_product_instance.to_dict()
# create an instance of ProductCollectionProduct from a dict
product_collection_product_from_dict = ProductCollectionProduct.from_dict(product_collection_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


