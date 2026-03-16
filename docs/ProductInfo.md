# ProductInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ProductInfoId**](ProductInfoId.md) |  | [optional] 
**qty** | [**ProductInfoQty**](ProductInfoQty.md) |  | [optional] 
**clientid** | [**ProductInfoClientid**](ProductInfoClientid.md) |  | [optional] 
**orderid** | [**ProductInfoOrderid**](ProductInfoOrderid.md) |  | [optional] 
**ordernumber** | **str** | The order number | [optional] 
**pid** | [**ProductInfoPid**](ProductInfoPid.md) |  | [optional] 
**regdate** | **date** | The registration date | [optional] 
**name** | **str** | The product name | [optional] 
**translated_name** | **str** | The translated product name | [optional] 
**groupname** | **str** | The product group name | [optional] 
**translated_groupname** | **str** | The translated product group name | [optional] 
**domain** | **str** | The associated domain name | [optional] 
**dedicatedip** | **str** | The dedicated IP address | [optional] 
**serverid** | [**ProductInfoServerid**](ProductInfoServerid.md) |  | [optional] 
**servername** | **str** | The server name | [optional] 
**serverip** | **str** | The server IP | [optional] 
**serverhostname** | **str** | The server hostname | [optional] 
**suspensionreason** | **str** | Suspension reason | [optional] 
**firstpaymentamount** | **str** | The first payment amount | [optional] 
**recurringamount** | **str** | The recurring amount | [optional] 
**paymentmethod** | **str** | The payment method | [optional] 
**paymentmethodname** | **str** | The human-readable payment method name | [optional] 
**billingcycle** | **str** | The billing cycle | [optional] 
**nextduedate** | **date** | The next due date | [optional] 
**status** | **str** | The service status | [optional] 
**username** | **str** | The service username | [optional] 
**password** | **str** | The service password placeholder | [optional] 
**subscriptionid** | **str** | The subscription ID | [optional] 
**promoid** | [**ProductInfoPromoid**](ProductInfoPromoid.md) |  | [optional] 
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


