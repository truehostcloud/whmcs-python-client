# ApiPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Admin username/API identifier | 
**password** | **str** | Admin password/API secret | 
**accesskey** | **str** | Optional API access key | [optional] 
**responsetype** | **str** | Response format | [optional] [default to 'json']
**action** | **str** | Must be &#39;AddOrder&#39; | 
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
**customfields** | **List[str]** | Array of base64 encoded serialized array of product custom field values | [optional] 
**language** | **str** | Default language setting | [optional] 
**clientip** | **str** | The IP address to associate with the order | [optional] 
**notes** | **str** | Admin only notes | [optional] 
**marketingoptin** | **bool** | Opt-in to marketing emails | [optional] 
**noemail** | **bool** | Set to true to suppress the Order Confirmation email being sent | [optional] 
**skipvalidation** | **bool** | Ignore required field validation | [optional] 
**clientid** | **int** | The ID of the client to add the order for | 
**clientemail** | **str** | The email address of the client to update | [optional] 
**status** | **str** | The status (e.g., Active) | [optional] 
**paymentmethod** | **str** | The payment method for the order in the system format (e.g., paypal, mailin) | 
**email_preferences_general** | **bool** | Receive general emails | [optional] 
**email_preferences_product** | **bool** | Receive product emails | [optional] 
**email_preferences_domain** | **bool** | Receive domain emails | [optional] 
**email_preferences_invoice** | **bool** | Receive invoice emails | [optional] 
**email_preferences_support** | **bool** | Receive support emails | [optional] 
**email_preferences_affiliate** | **bool** | Receive affiliate emails | [optional] 
**clearcreditcard** | **bool** | Clear stored credit card details | [optional] 
**latefeeoveride** | **bool** | Override Late Fees setting | [optional] 
**overideduenotices** | **bool** | Override Overdue Notices setting | [optional] 
**taxexempt** | **bool** | Exempt from tax collections | [optional] 
**separateinvoices** | **bool** | Group items into one invoice | [optional] 
**disableautocc** | **bool** | Enable/disable automatic credit card processing | [optional] 
**overrideautoclose** | **bool** | Enable/disable automatic account closure | [optional] 
**pid** | **List[int]** | Array of product IDs to add to the order | [optional] 
**qty** | **List[int]** | Array of product quantities | [optional] 
**domain** | **List[str]** | Array of domain names associated with the products/domains | [optional] 
**billingcycle** | **List[str]** | Array of billing cycles for the products | [optional] 
**domaintype** | **List[str]** | For domain registrations, array of register or transfer values | [optional] 
**regperiod** | **List[int]** | For domain registrations, the registration periods for the domains | [optional] 
**idnlanguage** | **List[str]** | For IDN domain registrations, the language codes for the domains | [optional] 
**eppcode** | **List[str]** | For domain transfers, the EPP codes for the domains being transferred | [optional] 
**nameserver1** | **str** | The first nameserver to apply to all domains in the order | [optional] 
**nameserver2** | **str** | The second nameserver to apply to all domains in the order | [optional] 
**nameserver3** | **str** | The third nameserver to apply to all domains in the order | [optional] 
**nameserver4** | **str** | The fourth nameserver to apply to all domains in the order | [optional] 
**nameserver5** | **str** | The fifth nameserver to apply to all domains in the order | [optional] 
**configoptions** | **List[str]** | Array of base64 encoded serialized array of product configurable options values | [optional] 
**priceoverride** | **List[float]** | Override the price of the product being ordered | [optional] 
**promocode** | **str** | The promotion code to apply to the order | [optional] 
**promooverride** | **bool** | Should the promotion apply to the order even without matching promotional products | [optional] 
**affid** | **int** | The affiliate ID to associate with the order | [optional] 
**noinvoice** | **bool** | Set to true to suppress the invoice generating for the whole order | [optional] 
**noinvoiceemail** | **bool** | Set to true to suppress the Invoice Created email being sent for the order | [optional] 
**addons** | **List[str]** | Array of comma separated lists of addons to create on order with the products | [optional] 
**addonsqty** | **List[str]** | Array of comma-separated lists of quantities for addons associated with products | [optional] 
**hostname** | **List[str]** | Array of hostnames for VPS/Dedicated Server orders | [optional] 
**ns1prefix** | **List[str]** | Array of first nameserver prefixes for VPS/Dedicated servers (e.g., ns1 in ns1.hostname.com) | [optional] 
**ns2prefix** | **List[str]** | Array of second nameserver prefixes for VPS/Dedicated servers (e.g., ns2 in ns2.hostname.com) | [optional] 
**rootpw** | **List[str]** | Array of desired root passwords for VPS/Dedicated servers | [optional] 
**contactid** | **int** | The ID of the contact, associated with the client, that should apply to all domains in the order | [optional] 
**dnsmanagement** | **List[bool]** | Add DNS Management to the Domain Order | [optional] 
**domainfields** | **List[str]** | Array of base64 encoded serialized array of TLD Specific Field Values | [optional] 
**emailforwarding** | **List[bool]** | Add Email Forwarding to the Domain Order | [optional] 
**idprotection** | **List[bool]** | Add ID Protection to the Domain Order | [optional] 
**domainpriceoverride** | **List[float]** | Override the price of the registration price on the domain being ordered | [optional] 
**domainrenewoverride** | **List[float]** | Override the price of the renewal price on the domain being ordered | [optional] 
**domainrenewals** | **Dict[str, int]** | A name -&gt; value object of domainName -&gt; renewalPeriod renewals to add an order for | [optional] 
**addonid** | **int** | The Addon ID for an Addon Only Order | [optional] 
**addonidqty** | **int** | The quantity of addons in an addon-only order | [optional] 
**serviceid** | **int** | The service ID for the addon only order | [optional] 
**addonids** | **List[int]** | Array of addon IDs for an Addon Only Order | [optional] 
**addonidsqty** | **List[int]** | Array of quantities for an addon-only order | [optional] 
**serviceids** | **List[int]** | Array of service IDs to associate the addons for an Addon Only order | [optional] 
**servicerenewals** | **List[int]** | Array of service IDs to be on-demand renewed | [optional] 
**addonrenewals** | **List[int]** | Array of service addon IDs to be on-demand renewed | [optional] 

## Example

```python
from whmcs_client.models.api_post_request import ApiPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPostRequest from a JSON string
api_post_request_instance = ApiPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiPostRequest.to_json())

# convert the object into a dict
api_post_request_dict = api_post_request_instance.to_dict()
# create an instance of ApiPostRequest from a dict
api_post_request_from_dict = ApiPostRequest.from_dict(api_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


