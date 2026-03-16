# ClientDetailsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** | The client ID | [optional] 
**owner_user_id** | **int** | The owning user ID | [optional] 
**userid** | **int** | The client ID alias | [optional] 
**id** | **int** | The client ID | [optional] 
**uuid** | **str** | The client UUID | [optional] 
**firstname** | **str** | The client first name | [optional] 
**lastname** | **str** | The client last name | [optional] 
**fullname** | **str** | The client full name | [optional] 
**companyname** | **str** | The client company name | [optional] 
**email** | **str** | The client email address | [optional] 
**address1** | **str** | Address line 1 | [optional] 
**address2** | **str** | Address line 2 | [optional] 
**city** | **str** | City | [optional] 
**fullstate** | **str** | Full state name | [optional] 
**state** | **str** | State code or value | [optional] 
**postcode** | **str** | Post code | [optional] 
**countrycode** | **str** | Country code | [optional] 
**country** | **str** | Country | [optional] 
**phonenumber** | **str** | Phone number | [optional] 
**tax_id** | **str** | Tax ID | [optional] 
**email_preferences** | [**EmailPreferences**](EmailPreferences.md) |  | [optional] 
**statecode** | **str** | State code | [optional] 
**countryname** | **str** | Country name | [optional] 
**phonecc** | **str** | Phone country code | [optional] 
**phonenumberformatted** | **str** | Formatted phone number | [optional] 
**telephone_number** | **str** | Alternate formatted phone number | [optional] 
**billingcid** | **int** | Billing contact ID | [optional] 
**notes** | **str** | Admin notes | [optional] 
**currency** | **int** | Currency ID | [optional] 
**defaultgateway** | **str** | Default gateway | [optional] 
**groupid** | **int** | Group ID | [optional] 
**status** | **str** | Client status | [optional] 
**credit** | **str** | Credit balance | [optional] 
**taxexempt** | **bool** | Whether the client is tax exempt | [optional] 
**latefeeoveride** | **bool** | Whether late fees are overridden | [optional] 
**overideduenotices** | **bool** | Whether due notices are overridden | [optional] 
**separateinvoices** | **bool** | Whether invoices are separated | [optional] 
**disableautocc** | **bool** | Whether auto credit card processing is disabled | [optional] 
**emailoptout** | **bool** | Whether the client has opted out of emails | [optional] 
**marketing_emails_opt_in** | **bool** | Whether the client has opted in to marketing emails | [optional] 
**overrideautoclose** | **bool** | Whether auto close is overridden | [optional] 
**allow_single_sign_on** | [**ClientDetailsInfoAllowSingleSignOn**](ClientDetailsInfoAllowSingleSignOn.md) |  | [optional] 
**email_verified** | **bool** | Whether the email is verified | [optional] 
**language** | **str** | Preferred language | [optional] 
**is_opted_in_to_marketing_emails** | **bool** | Alternate marketing opt-in flag | [optional] 
**lastlogin** | **str** | Last login summary | [optional] 
**currency_code** | **str** | Currency code | [optional] 
**customfields** | [**ClientDetailsInfoCustomfields**](ClientDetailsInfoCustomfields.md) |  | [optional] 
**users** | [**UserCollection**](UserCollection.md) |  | [optional] 

## Example

```python
from whmcs_client.models.client_details_info import ClientDetailsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClientDetailsInfo from a JSON string
client_details_info_instance = ClientDetailsInfo.from_json(json)
# print the JSON string representation of the object
print(ClientDetailsInfo.to_json())

# convert the object into a dict
client_details_info_dict = client_details_info_instance.to_dict()
# create an instance of ClientDetailsInfo from a dict
client_details_info_from_dict = ClientDetailsInfo.from_dict(client_details_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


