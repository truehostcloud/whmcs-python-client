# AddClientRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Must be &#x27;AddClient&#x27; | [default to 'AddClient']
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
**tax_id** | **str** | Client&#x27;s tax ID | [optional] 
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
**noemail** | **bool** | Set to true to suppress the Order Confirmation email being sent | [optional] 
**skipvalidation** | **bool** | Ignore required field validation | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

