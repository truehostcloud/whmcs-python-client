# AddClientRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Admin username/API identifier | 
**password** | **str** | Admin password/API secret | 
**accesskey** | **str** | Optional API access key | [optional] 
**responsetype** | **str** | Response format | [optional] [default to 'json']
**action** | **str** | Must be &#39;AddClient&#39; | 
**owner_user_id** | **int** | The ID of the user that should own the client | [optional] 
**firstname** | **str** | First name of the client | 
**lastname** | **str** | Last name of the client | 
**companyname** | **str** | Company name | [optional] 
**email** | **str** | Email address of the client | 
**address1** | **str** | Address line 1 | 
**address2** | **str** | Address line 2 | [optional] 
**city** | **str** | City | 
**state** | **str** | State | 
**postcode** | **str** | Postal code | 
**country** | **str** | 2 character ISO country code | 
**phonenumber** | **str** | Phone number | 
**tax_id** | **str** | Client&#39;s tax ID | [optional] 
**password2** | **str** | Password for the new user account | [optional] 
**securityqid** | **int** | Security question ID | [optional] 
**securityqans** | **str** | Security question answer | [optional] 
**currency** | **int** | Currency ID | [optional] 
**groupid** | **int** | Client group ID | [optional] 
**customfields** | **str** | Base64 encoded serialized array of custom field values | [optional] 
**language** | **str** | Default language setting | [optional] 
**clientip** | **str** | Originating IP address | [optional] 
**notes** | **str** | Admin only notes | [optional] 
**marketingoptin** | **bool** | Opt-in to marketing emails | [optional] 
**noemail** | **bool** | Do not send welcome email | [optional] 
**skipvalidation** | **bool** | Do not enforce required fields | [optional] 

## Example

```python
from whmcs_client.models.add_client_request import AddClientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddClientRequest from a JSON string
add_client_request_instance = AddClientRequest.from_json(json)
# print the JSON string representation of the object
print(AddClientRequest.to_json())

# convert the object into a dict
add_client_request_dict = add_client_request_instance.to_dict()
# create an instance of AddClientRequest from a dict
add_client_request_from_dict = AddClientRequest.from_dict(add_client_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


