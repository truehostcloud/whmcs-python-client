# AddOrderRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Must be &#x27;AddOrder&#x27; | [default to 'AddOrder']
**clientid** | **int** | The ID of the client to add the order for | 
**clientemail** | **str** | The email address of the client to update | [optional] 
**paymentmethod** | **str** | The payment method for the order in the system format (e.g., paypal, mailin) | 
**pid** | **list[int]** | Array of product IDs to add to the order | [optional] 
**qty** | **list[int]** | Array of product quantities | [optional] 
**domain** | **list[str]** | Array of domain names associated with the products/domains | [optional] 
**billingcycle** | **list[str]** | Array of billing cycles for the products | [optional] 
**domaintype** | **list[str]** | For domain registrations, array of register or transfer values | [optional] 
**regperiod** | **list[int]** | For domain registrations, the registration periods for the domains | [optional] 
**idnlanguage** | **list[str]** | For IDN domain registrations, the language codes for the domains | [optional] 
**eppcode** | **list[str]** | For domain transfers, the EPP codes for the domains being transferred | [optional] 
**nameserver1** | **str** | The first nameserver to apply to all domains in the order | [optional] 
**nameserver2** | **str** | The second nameserver to apply to all domains in the order | [optional] 
**nameserver3** | **str** | The third nameserver to apply to all domains in the order | [optional] 
**nameserver4** | **str** | The fourth nameserver to apply to all domains in the order | [optional] 
**nameserver5** | **str** | The fifth nameserver to apply to all domains in the order | [optional] 
**configoptions** | **list[str]** | Array of base64 encoded serialized array of product configurable options values | [optional] 
**priceoverride** | **list[float]** | Override the price of the product being ordered | [optional] 
**promocode** | **str** | The promotion code to apply to the order | [optional] 
**promooverride** | **bool** | Should the promotion apply to the order even without matching promotional products | [optional] 
**affid** | **int** | The affiliate ID to associate with the order | [optional] 
**noinvoice** | **bool** | Set to true to suppress the invoice generating for the whole order | [optional] 
**noinvoiceemail** | **bool** | Set to true to suppress the Invoice Created email being sent for the order | [optional] 
**addons** | **list[str]** | Array of comma separated lists of addons to create on order with the products | [optional] 
**addonsqty** | **list[str]** | Array of comma-separated lists of quantities for addons associated with products | [optional] 
**hostname** | **list[str]** | Array of hostnames for VPS/Dedicated Server orders | [optional] 
**ns1prefix** | **list[str]** | Array of first nameserver prefixes for VPS/Dedicated servers (e.g., ns1 in ns1.hostname.com) | [optional] 
**ns2prefix** | **list[str]** | Array of second nameserver prefixes for VPS/Dedicated servers (e.g., ns2 in ns2.hostname.com) | [optional] 
**rootpw** | **list[str]** | Array of desired root passwords for VPS/Dedicated servers | [optional] 
**contactid** | **int** | The ID of the contact, associated with the client, that should apply to all domains in the order | [optional] 
**dnsmanagement** | **list[bool]** | Add DNS Management to the Domain Order | [optional] 
**domainfields** | **list[str]** | Array of base64 encoded serialized array of TLD Specific Field Values | [optional] 
**emailforwarding** | **list[bool]** | Add Email Forwarding to the Domain Order | [optional] 
**idprotection** | **list[bool]** | Add ID Protection to the Domain Order | [optional] 
**domainpriceoverride** | **list[float]** | Override the price of the registration price on the domain being ordered | [optional] 
**domainrenewoverride** | **list[float]** | Override the price of the renewal price on the domain being ordered | [optional] 
**domainrenewals** | **dict(str, int)** | A name -&gt; value object of domainName -&gt; renewalPeriod renewals to add an order for | [optional] 
**addonid** | **int** | The Addon ID for an Addon Only Order | [optional] 
**addonidqty** | **int** | The quantity of addons in an addon-only order | [optional] 
**serviceid** | **int** | The service ID for the addon only order | [optional] 
**addonids** | **list[int]** | Array of addon IDs for an Addon Only Order | [optional] 
**addonidsqty** | **list[int]** | Array of quantities for an addon-only order | [optional] 
**serviceids** | **list[int]** | Array of service IDs to associate the addons for an Addon Only order | [optional] 
**servicerenewals** | **list[int]** | Array of service IDs to be on-demand renewed | [optional] 
**addonrenewals** | **list[int]** | Array of service addon IDs to be on-demand renewed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

