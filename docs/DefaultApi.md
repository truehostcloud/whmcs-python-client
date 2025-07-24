# whmcs_client.DefaultApi

All URIs are relative to *https://your-whmcs-instance.com/includes*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_client**](DefaultApi.md#add_client) | **POST** /api.php?action&#x3D;AddClient | Add a new client
[**add_order**](DefaultApi.md#add_order) | **POST** /api.php?action&#x3D;AddOrder | Create a new order
[**get_clients**](DefaultApi.md#get_clients) | **POST** /api.php?action&#x3D;GetClients | Get clients
[**get_currencies**](DefaultApi.md#get_currencies) | **POST** /api.php?action&#x3D;GetCurrencies | Get currencies
[**update_client**](DefaultApi.md#update_client) | **POST** /api.php?action&#x3D;UpdateClient | Update client details


# **add_client**
> AddClientResponse add_client(username, password, firstname, lastname, email, address1, city, state, postcode, country, phonenumber, accesskey=accesskey, responsetype=responsetype, owner_user_id=owner_user_id, companyname=companyname, address2=address2, tax_id=tax_id, password2=password2, securityqid=securityqid, securityqans=securityqans, currency=currency, groupid=groupid, customfields=customfields, language=language, clientip=clientip, notes=notes, marketingoptin=marketingoptin, noemail=noemail, skipvalidation=skipvalidation)

Add a new client

Creates a new client account in WHMCS

### Example


```python
import whmcs_client
from whmcs_client.models.add_client_response import AddClientResponse
from whmcs_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://your-whmcs-instance.com/includes
# See configuration.py for a list of all supported configuration parameters.
configuration = whmcs_client.Configuration(
    host = "https://your-whmcs-instance.com/includes"
)


# Enter a context with an instance of the API client
with whmcs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = whmcs_client.DefaultApi(api_client)
    username = 'username_example' # str | Admin username/API identifier
    password = 'password_example' # str | Admin password/API secret
    firstname = 'firstname_example' # str | First name of the client
    lastname = 'lastname_example' # str | Last name of the client
    email = 'email_example' # str | Email address of the client
    address1 = 'address1_example' # str | Address line 1
    city = 'city_example' # str | City
    state = 'state_example' # str | State
    postcode = 'postcode_example' # str | Postal code
    country = 'country_example' # str | 2 character ISO country code
    phonenumber = 'phonenumber_example' # str | Phone number
    accesskey = 'accesskey_example' # str | Optional API access key (optional)
    responsetype = json # str | Response format (optional) (default to json)
    owner_user_id = 56 # int | The ID of the user that should own the client (optional)
    companyname = 'companyname_example' # str | Company name (optional)
    address2 = 'address2_example' # str | Address line 2 (optional)
    tax_id = 'tax_id_example' # str | Client's tax ID (optional)
    password2 = 'password2_example' # str | Password for the new user account (optional)
    securityqid = 56 # int | Security question ID (optional)
    securityqans = 'securityqans_example' # str | Security question answer (optional)
    currency = 56 # int | Currency ID (optional)
    groupid = 56 # int | Client group ID (optional)
    customfields = 'customfields_example' # str | Base64 encoded serialized array of custom field values (optional)
    language = 'language_example' # str | Default language setting (optional)
    clientip = 'clientip_example' # str | Originating IP address (optional)
    notes = 'notes_example' # str | Admin only notes (optional)
    marketingoptin = True # bool | Opt-in to marketing emails (optional)
    noemail = True # bool | Set to true to suppress the Order Confirmation email being sent (optional)
    skipvalidation = True # bool | Ignore required field validation (optional)

    try:
        # Add a new client
        api_response = api_instance.add_client(username, password, firstname, lastname, email, address1, city, state, postcode, country, phonenumber, accesskey=accesskey, responsetype=responsetype, owner_user_id=owner_user_id, companyname=companyname, address2=address2, tax_id=tax_id, password2=password2, securityqid=securityqid, securityqans=securityqans, currency=currency, groupid=groupid, customfields=customfields, language=language, clientip=clientip, notes=notes, marketingoptin=marketingoptin, noemail=noemail, skipvalidation=skipvalidation)
        print("The response of DefaultApi->add_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Admin username/API identifier | 
 **password** | **str**| Admin password/API secret | 
 **firstname** | **str**| First name of the client | 
 **lastname** | **str**| Last name of the client | 
 **email** | **str**| Email address of the client | 
 **address1** | **str**| Address line 1 | 
 **city** | **str**| City | 
 **state** | **str**| State | 
 **postcode** | **str**| Postal code | 
 **country** | **str**| 2 character ISO country code | 
 **phonenumber** | **str**| Phone number | 
 **accesskey** | **str**| Optional API access key | [optional] 
 **responsetype** | **str**| Response format | [optional] [default to json]
 **owner_user_id** | **int**| The ID of the user that should own the client | [optional] 
 **companyname** | **str**| Company name | [optional] 
 **address2** | **str**| Address line 2 | [optional] 
 **tax_id** | **str**| Client&#39;s tax ID | [optional] 
 **password2** | **str**| Password for the new user account | [optional] 
 **securityqid** | **int**| Security question ID | [optional] 
 **securityqans** | **str**| Security question answer | [optional] 
 **currency** | **int**| Currency ID | [optional] 
 **groupid** | **int**| Client group ID | [optional] 
 **customfields** | **str**| Base64 encoded serialized array of custom field values | [optional] 
 **language** | **str**| Default language setting | [optional] 
 **clientip** | **str**| Originating IP address | [optional] 
 **notes** | **str**| Admin only notes | [optional] 
 **marketingoptin** | **bool**| Opt-in to marketing emails | [optional] 
 **noemail** | **bool**| Set to true to suppress the Order Confirmation email being sent | [optional] 
 **skipvalidation** | **bool**| Ignore required field validation | [optional] 

### Return type

[**AddClientResponse**](AddClientResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client created successfully |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order**
> AddOrderResponse add_order(username, password, clientid, paymentmethod, accesskey=accesskey, responsetype=responsetype, clientemail=clientemail, pid=pid, qty=qty, domain=domain, billingcycle=billingcycle, domaintype=domaintype, regperiod=regperiod, idnlanguage=idnlanguage, eppcode=eppcode, nameserver1=nameserver1, nameserver2=nameserver2, nameserver3=nameserver3, nameserver4=nameserver4, nameserver5=nameserver5, configoptions=configoptions, priceoverride=priceoverride, promocode=promocode, promooverride=promooverride, affid=affid, noinvoice=noinvoice, noinvoiceemail=noinvoiceemail, addons=addons, addonsqty=addonsqty, hostname=hostname, ns1prefix=ns1prefix, ns2prefix=ns2prefix, rootpw=rootpw, contactid=contactid, dnsmanagement=dnsmanagement, domainfields=domainfields, emailforwarding=emailforwarding, idprotection=idprotection, domainpriceoverride=domainpriceoverride, domainrenewoverride=domainrenewoverride, domainrenewals=domainrenewals, addonid=addonid, addonidqty=addonidqty, serviceid=serviceid, addonids=addonids, addonidsqty=addonidsqty, serviceids=serviceids, servicerenewals=servicerenewals, addonrenewals=addonrenewals)

Create a new order

Places a new order for products/services

### Example


```python
import whmcs_client
from whmcs_client.models.add_order_response import AddOrderResponse
from whmcs_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://your-whmcs-instance.com/includes
# See configuration.py for a list of all supported configuration parameters.
configuration = whmcs_client.Configuration(
    host = "https://your-whmcs-instance.com/includes"
)


# Enter a context with an instance of the API client
with whmcs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = whmcs_client.DefaultApi(api_client)
    username = 'username_example' # str | Admin username/API identifier
    password = 'password_example' # str | Admin password/API secret
    clientid = None # object | The ID of the client to add the order for
    paymentmethod = 'paymentmethod_example' # str | The payment method for the order in the system format (e.g., paypal, mailin)
    accesskey = 'accesskey_example' # str | Optional API access key (optional)
    responsetype = json # str | Response format (optional) (default to json)
    clientemail = 'clientemail_example' # str | The email address of the client to update (optional)
    pid = [56] # List[int] | Array of product IDs to add to the order (optional)
    qty = [56] # List[int] | Array of product quantities (optional)
    domain = ['domain_example'] # List[str] | Array of domain names associated with the products/domains (optional)
    billingcycle = ['billingcycle_example'] # List[str] | Array of billing cycles for the products (optional)
    domaintype = ['domaintype_example'] # List[str] | For domain registrations, array of register or transfer values (optional)
    regperiod = [56] # List[int] | For domain registrations, the registration periods for the domains (optional)
    idnlanguage = ['idnlanguage_example'] # List[str] | For IDN domain registrations, the language codes for the domains (optional)
    eppcode = ['eppcode_example'] # List[str] | For domain transfers, the EPP codes for the domains being transferred (optional)
    nameserver1 = 'nameserver1_example' # str | The first nameserver to apply to all domains in the order (optional)
    nameserver2 = 'nameserver2_example' # str | The second nameserver to apply to all domains in the order (optional)
    nameserver3 = 'nameserver3_example' # str | The third nameserver to apply to all domains in the order (optional)
    nameserver4 = 'nameserver4_example' # str | The fourth nameserver to apply to all domains in the order (optional)
    nameserver5 = 'nameserver5_example' # str | The fifth nameserver to apply to all domains in the order (optional)
    configoptions = ['configoptions_example'] # List[str] | Array of base64 encoded serialized array of product configurable options values (optional)
    priceoverride = [3.4] # List[float] | Override the price of the product being ordered (optional)
    promocode = 'promocode_example' # str | The promotion code to apply to the order (optional)
    promooverride = True # bool | Should the promotion apply to the order even without matching promotional products (optional)
    affid = 56 # int | The affiliate ID to associate with the order (optional)
    noinvoice = True # bool | Set to true to suppress the invoice generating for the whole order (optional)
    noinvoiceemail = True # bool | Set to true to suppress the Invoice Created email being sent for the order (optional)
    addons = ['addons_example'] # List[str] | Array of comma separated lists of addons to create on order with the products (optional)
    addonsqty = ['addonsqty_example'] # List[str] | Array of comma-separated lists of quantities for addons associated with products (optional)
    hostname = ['hostname_example'] # List[str] | Array of hostnames for VPS/Dedicated Server orders (optional)
    ns1prefix = ['ns1prefix_example'] # List[str] | Array of first nameserver prefixes for VPS/Dedicated servers (e.g., ns1 in ns1.hostname.com) (optional)
    ns2prefix = ['ns2prefix_example'] # List[str] | Array of second nameserver prefixes for VPS/Dedicated servers (e.g., ns2 in ns2.hostname.com) (optional)
    rootpw = ['rootpw_example'] # List[str] | Array of desired root passwords for VPS/Dedicated servers (optional)
    contactid = 56 # int | The ID of the contact, associated with the client, that should apply to all domains in the order (optional)
    dnsmanagement = [True] # List[bool] | Add DNS Management to the Domain Order (optional)
    domainfields = ['domainfields_example'] # List[str] | Array of base64 encoded serialized array of TLD Specific Field Values (optional)
    emailforwarding = [True] # List[bool] | Add Email Forwarding to the Domain Order (optional)
    idprotection = [True] # List[bool] | Add ID Protection to the Domain Order (optional)
    domainpriceoverride = [3.4] # List[float] | Override the price of the registration price on the domain being ordered (optional)
    domainrenewoverride = [3.4] # List[float] | Override the price of the renewal price on the domain being ordered (optional)
    domainrenewals = None # Dict[str, int] | A name -> value object of domainName -> renewalPeriod renewals to add an order for (optional)
    addonid = 56 # int | The Addon ID for an Addon Only Order (optional)
    addonidqty = 56 # int | The quantity of addons in an addon-only order (optional)
    serviceid = 56 # int | The service ID for the addon only order (optional)
    addonids = [56] # List[int] | Array of addon IDs for an Addon Only Order (optional)
    addonidsqty = [56] # List[int] | Array of quantities for an addon-only order (optional)
    serviceids = [56] # List[int] | Array of service IDs to associate the addons for an Addon Only order (optional)
    servicerenewals = [56] # List[int] | Array of service IDs to be on-demand renewed (optional)
    addonrenewals = [56] # List[int] | Array of service addon IDs to be on-demand renewed (optional)

    try:
        # Create a new order
        api_response = api_instance.add_order(username, password, clientid, paymentmethod, accesskey=accesskey, responsetype=responsetype, clientemail=clientemail, pid=pid, qty=qty, domain=domain, billingcycle=billingcycle, domaintype=domaintype, regperiod=regperiod, idnlanguage=idnlanguage, eppcode=eppcode, nameserver1=nameserver1, nameserver2=nameserver2, nameserver3=nameserver3, nameserver4=nameserver4, nameserver5=nameserver5, configoptions=configoptions, priceoverride=priceoverride, promocode=promocode, promooverride=promooverride, affid=affid, noinvoice=noinvoice, noinvoiceemail=noinvoiceemail, addons=addons, addonsqty=addonsqty, hostname=hostname, ns1prefix=ns1prefix, ns2prefix=ns2prefix, rootpw=rootpw, contactid=contactid, dnsmanagement=dnsmanagement, domainfields=domainfields, emailforwarding=emailforwarding, idprotection=idprotection, domainpriceoverride=domainpriceoverride, domainrenewoverride=domainrenewoverride, domainrenewals=domainrenewals, addonid=addonid, addonidqty=addonidqty, serviceid=serviceid, addonids=addonids, addonidsqty=addonidsqty, serviceids=serviceids, servicerenewals=servicerenewals, addonrenewals=addonrenewals)
        print("The response of DefaultApi->add_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Admin username/API identifier | 
 **password** | **str**| Admin password/API secret | 
 **clientid** | [**object**](object.md)| The ID of the client to add the order for | 
 **paymentmethod** | **str**| The payment method for the order in the system format (e.g., paypal, mailin) | 
 **accesskey** | **str**| Optional API access key | [optional] 
 **responsetype** | **str**| Response format | [optional] [default to json]
 **clientemail** | **str**| The email address of the client to update | [optional] 
 **pid** | [**List[int]**](int.md)| Array of product IDs to add to the order | [optional] 
 **qty** | [**List[int]**](int.md)| Array of product quantities | [optional] 
 **domain** | [**List[str]**](str.md)| Array of domain names associated with the products/domains | [optional] 
 **billingcycle** | [**List[str]**](str.md)| Array of billing cycles for the products | [optional] 
 **domaintype** | [**List[str]**](str.md)| For domain registrations, array of register or transfer values | [optional] 
 **regperiod** | [**List[int]**](int.md)| For domain registrations, the registration periods for the domains | [optional] 
 **idnlanguage** | [**List[str]**](str.md)| For IDN domain registrations, the language codes for the domains | [optional] 
 **eppcode** | [**List[str]**](str.md)| For domain transfers, the EPP codes for the domains being transferred | [optional] 
 **nameserver1** | **str**| The first nameserver to apply to all domains in the order | [optional] 
 **nameserver2** | **str**| The second nameserver to apply to all domains in the order | [optional] 
 **nameserver3** | **str**| The third nameserver to apply to all domains in the order | [optional] 
 **nameserver4** | **str**| The fourth nameserver to apply to all domains in the order | [optional] 
 **nameserver5** | **str**| The fifth nameserver to apply to all domains in the order | [optional] 
 **configoptions** | [**List[str]**](str.md)| Array of base64 encoded serialized array of product configurable options values | [optional] 
 **priceoverride** | [**List[float]**](float.md)| Override the price of the product being ordered | [optional] 
 **promocode** | **str**| The promotion code to apply to the order | [optional] 
 **promooverride** | **bool**| Should the promotion apply to the order even without matching promotional products | [optional] 
 **affid** | **int**| The affiliate ID to associate with the order | [optional] 
 **noinvoice** | **bool**| Set to true to suppress the invoice generating for the whole order | [optional] 
 **noinvoiceemail** | **bool**| Set to true to suppress the Invoice Created email being sent for the order | [optional] 
 **addons** | [**List[str]**](str.md)| Array of comma separated lists of addons to create on order with the products | [optional] 
 **addonsqty** | [**List[str]**](str.md)| Array of comma-separated lists of quantities for addons associated with products | [optional] 
 **hostname** | [**List[str]**](str.md)| Array of hostnames for VPS/Dedicated Server orders | [optional] 
 **ns1prefix** | [**List[str]**](str.md)| Array of first nameserver prefixes for VPS/Dedicated servers (e.g., ns1 in ns1.hostname.com) | [optional] 
 **ns2prefix** | [**List[str]**](str.md)| Array of second nameserver prefixes for VPS/Dedicated servers (e.g., ns2 in ns2.hostname.com) | [optional] 
 **rootpw** | [**List[str]**](str.md)| Array of desired root passwords for VPS/Dedicated servers | [optional] 
 **contactid** | **int**| The ID of the contact, associated with the client, that should apply to all domains in the order | [optional] 
 **dnsmanagement** | [**List[bool]**](bool.md)| Add DNS Management to the Domain Order | [optional] 
 **domainfields** | [**List[str]**](str.md)| Array of base64 encoded serialized array of TLD Specific Field Values | [optional] 
 **emailforwarding** | [**List[bool]**](bool.md)| Add Email Forwarding to the Domain Order | [optional] 
 **idprotection** | [**List[bool]**](bool.md)| Add ID Protection to the Domain Order | [optional] 
 **domainpriceoverride** | [**List[float]**](float.md)| Override the price of the registration price on the domain being ordered | [optional] 
 **domainrenewoverride** | [**List[float]**](float.md)| Override the price of the renewal price on the domain being ordered | [optional] 
 **domainrenewals** | [**Dict[str, int]**](Dict.md)| A name -&gt; value object of domainName -&gt; renewalPeriod renewals to add an order for | [optional] 
 **addonid** | **int**| The Addon ID for an Addon Only Order | [optional] 
 **addonidqty** | **int**| The quantity of addons in an addon-only order | [optional] 
 **serviceid** | **int**| The service ID for the addon only order | [optional] 
 **addonids** | [**List[int]**](int.md)| Array of addon IDs for an Addon Only Order | [optional] 
 **addonidsqty** | [**List[int]**](int.md)| Array of quantities for an addon-only order | [optional] 
 **serviceids** | [**List[int]**](int.md)| Array of service IDs to associate the addons for an Addon Only order | [optional] 
 **servicerenewals** | [**List[int]**](int.md)| Array of service IDs to be on-demand renewed | [optional] 
 **addonrenewals** | [**List[int]**](int.md)| Array of service addon IDs to be on-demand renewed | [optional] 

### Return type

[**AddOrderResponse**](AddOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order created successfully |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clients**
> GetClientsResponse get_clients(username, password, accesskey=accesskey, responsetype=responsetype, limitstart=limitstart, limitnum=limitnum, sorting=sorting, status=status, search=search, orderby=orderby)

Get clients

Obtain the clients that match passed criteria

### Example


```python
import whmcs_client
from whmcs_client.models.get_clients_response import GetClientsResponse
from whmcs_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://your-whmcs-instance.com/includes
# See configuration.py for a list of all supported configuration parameters.
configuration = whmcs_client.Configuration(
    host = "https://your-whmcs-instance.com/includes"
)


# Enter a context with an instance of the API client
with whmcs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = whmcs_client.DefaultApi(api_client)
    username = 'username_example' # str | Admin username/API identifier
    password = 'password_example' # str | Admin password/API secret
    accesskey = 'accesskey_example' # str | Optional API access key (optional)
    responsetype = json # str | Response format (optional) (default to json)
    limitstart = 0 # int | The offset for the returned log data (optional) (default to 0)
    limitnum = 25 # int | The number of records to return (optional) (default to 25)
    sorting = ASC # str | The direction to sort the results. ASC or DESC. (optional) (default to ASC)
    status = 'status_example' # str | Optional desired Client Status. 'Active', 'Inactive', or 'Closed'. (optional)
    search = 'search_example' # str | The search term to look for at the start of email, firstname, lastname, fullname or companyname (optional)
    orderby = 'orderby_example' # str | The column to order by. id, firstname, lastname, companyname, email, groupid, datecreated, status (optional)

    try:
        # Get clients
        api_response = api_instance.get_clients(username, password, accesskey=accesskey, responsetype=responsetype, limitstart=limitstart, limitnum=limitnum, sorting=sorting, status=status, search=search, orderby=orderby)
        print("The response of DefaultApi->get_clients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_clients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Admin username/API identifier | 
 **password** | **str**| Admin password/API secret | 
 **accesskey** | **str**| Optional API access key | [optional] 
 **responsetype** | **str**| Response format | [optional] [default to json]
 **limitstart** | **int**| The offset for the returned log data | [optional] [default to 0]
 **limitnum** | **int**| The number of records to return | [optional] [default to 25]
 **sorting** | **str**| The direction to sort the results. ASC or DESC. | [optional] [default to ASC]
 **status** | **str**| Optional desired Client Status. &#39;Active&#39;, &#39;Inactive&#39;, or &#39;Closed&#39;. | [optional] 
 **search** | **str**| The search term to look for at the start of email, firstname, lastname, fullname or companyname | [optional] 
 **orderby** | **str**| The column to order by. id, firstname, lastname, companyname, email, groupid, datecreated, status | [optional] 

### Return type

[**GetClientsResponse**](GetClientsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Clients retrieved successfully |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currencies**
> GetCurrenciesResponse get_currencies(username, password, accesskey=accesskey, responsetype=responsetype)

Get currencies

Obtain the currencies configured in the system

### Example


```python
import whmcs_client
from whmcs_client.models.get_currencies_response import GetCurrenciesResponse
from whmcs_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://your-whmcs-instance.com/includes
# See configuration.py for a list of all supported configuration parameters.
configuration = whmcs_client.Configuration(
    host = "https://your-whmcs-instance.com/includes"
)


# Enter a context with an instance of the API client
with whmcs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = whmcs_client.DefaultApi(api_client)
    username = 'username_example' # str | Admin username/API identifier
    password = 'password_example' # str | Admin password/API secret
    accesskey = 'accesskey_example' # str | Optional API access key (optional)
    responsetype = json # str | Response format (optional) (default to json)

    try:
        # Get currencies
        api_response = api_instance.get_currencies(username, password, accesskey=accesskey, responsetype=responsetype)
        print("The response of DefaultApi->get_currencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_currencies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Admin username/API identifier | 
 **password** | **str**| Admin password/API secret | 
 **accesskey** | **str**| Optional API access key | [optional] 
 **responsetype** | **str**| Response format | [optional] [default to json]

### Return type

[**GetCurrenciesResponse**](GetCurrenciesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Currencies retrieved successfully |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client**
> UpdateClientResponse update_client(username, password, clientid, accesskey=accesskey, responsetype=responsetype, clientemail=clientemail, firstname=firstname, lastname=lastname, companyname=companyname, email=email, address1=address1, address2=address2, city=city, state=state, postcode=postcode, country=country, phonenumber=phonenumber, tax_id=tax_id, password2=password2, securityqid=securityqid, securityqans=securityqans, currency=currency, groupid=groupid, customfields=customfields, language=language, clientip=clientip, notes=notes, status=status, paymentmethod=paymentmethod, email_preferences_general=email_preferences_general, email_preferences_product=email_preferences_product, email_preferences_domain=email_preferences_domain, email_preferences_invoice=email_preferences_invoice, email_preferences_support=email_preferences_support, email_preferences_affiliate=email_preferences_affiliate, clearcreditcard=clearcreditcard, latefeeoveride=latefeeoveride, overideduenotices=overideduenotices, taxexempt=taxexempt, separateinvoices=separateinvoices, disableautocc=disableautocc, overrideautoclose=overrideautoclose)

Update client details

Modifies an existing client's information

### Example


```python
import whmcs_client
from whmcs_client.models.update_client_response import UpdateClientResponse
from whmcs_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://your-whmcs-instance.com/includes
# See configuration.py for a list of all supported configuration parameters.
configuration = whmcs_client.Configuration(
    host = "https://your-whmcs-instance.com/includes"
)


# Enter a context with an instance of the API client
with whmcs_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = whmcs_client.DefaultApi(api_client)
    username = 'username_example' # str | Admin username/API identifier
    password = 'password_example' # str | Admin password/API secret
    clientid = None # object | The ID of the client to update
    accesskey = 'accesskey_example' # str | Optional API access key (optional)
    responsetype = json # str | Response format (optional) (default to json)
    clientemail = 'clientemail_example' # str | The email address of the client to update (optional)
    firstname = 'firstname_example' # str | First name of the client (optional)
    lastname = 'lastname_example' # str | Last name of the client (optional)
    companyname = 'companyname_example' # str | Company name (optional)
    email = 'email_example' # str | Email address of the client (optional)
    address1 = 'address1_example' # str | Address line 1 (optional)
    address2 = 'address2_example' # str | Address line 2 (optional)
    city = 'city_example' # str | City (optional)
    state = 'state_example' # str | State (optional)
    postcode = 'postcode_example' # str | Postal code (optional)
    country = 'country_example' # str | 2 character ISO country code (optional)
    phonenumber = 'phonenumber_example' # str | Phone number (optional)
    tax_id = 'tax_id_example' # str | Client's tax ID (optional)
    password2 = 'password2_example' # str | Password for the new user account (optional)
    securityqid = 56 # int | Security question ID (optional)
    securityqans = 'securityqans_example' # str | Security question answer (optional)
    currency = 56 # int | Currency ID (optional)
    groupid = 56 # int | Client group ID (optional)
    customfields = 'customfields_example' # str | Base64 encoded serialized array of custom field values (optional)
    language = 'language_example' # str | Default language setting (optional)
    clientip = 'clientip_example' # str | Originating IP address (optional)
    notes = 'notes_example' # str | Admin only notes (optional)
    status = 'status_example' # str | The status (e.g., Active) (optional)
    paymentmethod = 'paymentmethod_example' # str | The payment method for the order in the system format (e.g., paypal, mailin) (optional)
    email_preferences_general = True # bool | Receive general emails (optional)
    email_preferences_product = True # bool | Receive product emails (optional)
    email_preferences_domain = True # bool | Receive domain emails (optional)
    email_preferences_invoice = True # bool | Receive invoice emails (optional)
    email_preferences_support = True # bool | Receive support emails (optional)
    email_preferences_affiliate = True # bool | Receive affiliate emails (optional)
    clearcreditcard = True # bool | Clear stored credit card details (optional)
    latefeeoveride = True # bool | Override Late Fees setting (optional)
    overideduenotices = True # bool | Override Overdue Notices setting (optional)
    taxexempt = True # bool | Exempt from tax collections (optional)
    separateinvoices = True # bool | Group items into one invoice (optional)
    disableautocc = True # bool | Enable/disable automatic credit card processing (optional)
    overrideautoclose = True # bool | Enable/disable automatic account closure (optional)

    try:
        # Update client details
        api_response = api_instance.update_client(username, password, clientid, accesskey=accesskey, responsetype=responsetype, clientemail=clientemail, firstname=firstname, lastname=lastname, companyname=companyname, email=email, address1=address1, address2=address2, city=city, state=state, postcode=postcode, country=country, phonenumber=phonenumber, tax_id=tax_id, password2=password2, securityqid=securityqid, securityqans=securityqans, currency=currency, groupid=groupid, customfields=customfields, language=language, clientip=clientip, notes=notes, status=status, paymentmethod=paymentmethod, email_preferences_general=email_preferences_general, email_preferences_product=email_preferences_product, email_preferences_domain=email_preferences_domain, email_preferences_invoice=email_preferences_invoice, email_preferences_support=email_preferences_support, email_preferences_affiliate=email_preferences_affiliate, clearcreditcard=clearcreditcard, latefeeoveride=latefeeoveride, overideduenotices=overideduenotices, taxexempt=taxexempt, separateinvoices=separateinvoices, disableautocc=disableautocc, overrideautoclose=overrideautoclose)
        print("The response of DefaultApi->update_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Admin username/API identifier | 
 **password** | **str**| Admin password/API secret | 
 **clientid** | [**object**](object.md)| The ID of the client to update | 
 **accesskey** | **str**| Optional API access key | [optional] 
 **responsetype** | **str**| Response format | [optional] [default to json]
 **clientemail** | **str**| The email address of the client to update | [optional] 
 **firstname** | **str**| First name of the client | [optional] 
 **lastname** | **str**| Last name of the client | [optional] 
 **companyname** | **str**| Company name | [optional] 
 **email** | **str**| Email address of the client | [optional] 
 **address1** | **str**| Address line 1 | [optional] 
 **address2** | **str**| Address line 2 | [optional] 
 **city** | **str**| City | [optional] 
 **state** | **str**| State | [optional] 
 **postcode** | **str**| Postal code | [optional] 
 **country** | **str**| 2 character ISO country code | [optional] 
 **phonenumber** | **str**| Phone number | [optional] 
 **tax_id** | **str**| Client&#39;s tax ID | [optional] 
 **password2** | **str**| Password for the new user account | [optional] 
 **securityqid** | **int**| Security question ID | [optional] 
 **securityqans** | **str**| Security question answer | [optional] 
 **currency** | **int**| Currency ID | [optional] 
 **groupid** | **int**| Client group ID | [optional] 
 **customfields** | **str**| Base64 encoded serialized array of custom field values | [optional] 
 **language** | **str**| Default language setting | [optional] 
 **clientip** | **str**| Originating IP address | [optional] 
 **notes** | **str**| Admin only notes | [optional] 
 **status** | **str**| The status (e.g., Active) | [optional] 
 **paymentmethod** | **str**| The payment method for the order in the system format (e.g., paypal, mailin) | [optional] 
 **email_preferences_general** | **bool**| Receive general emails | [optional] 
 **email_preferences_product** | **bool**| Receive product emails | [optional] 
 **email_preferences_domain** | **bool**| Receive domain emails | [optional] 
 **email_preferences_invoice** | **bool**| Receive invoice emails | [optional] 
 **email_preferences_support** | **bool**| Receive support emails | [optional] 
 **email_preferences_affiliate** | **bool**| Receive affiliate emails | [optional] 
 **clearcreditcard** | **bool**| Clear stored credit card details | [optional] 
 **latefeeoveride** | **bool**| Override Late Fees setting | [optional] 
 **overideduenotices** | **bool**| Override Overdue Notices setting | [optional] 
 **taxexempt** | **bool**| Exempt from tax collections | [optional] 
 **separateinvoices** | **bool**| Group items into one invoice | [optional] 
 **disableautocc** | **bool**| Enable/disable automatic credit card processing | [optional] 
 **overrideautoclose** | **bool**| Enable/disable automatic account closure | [optional] 

### Return type

[**UpdateClientResponse**](UpdateClientResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client updated successfully |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

