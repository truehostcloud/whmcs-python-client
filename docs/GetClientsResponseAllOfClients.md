# GetClientsResponseAllOfClients


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client** | [**List[ClientInfo]**](ClientInfo.md) | Array of client information | [optional] 

## Example

```python
from whmcs_client.models.get_clients_response_all_of_clients import GetClientsResponseAllOfClients

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsResponseAllOfClients from a JSON string
get_clients_response_all_of_clients_instance = GetClientsResponseAllOfClients.from_json(json)
# print the JSON string representation of the object
print(GetClientsResponseAllOfClients.to_json())

# convert the object into a dict
get_clients_response_all_of_clients_dict = get_clients_response_all_of_clients_instance.to_dict()
# create an instance of GetClientsResponseAllOfClients from a dict
get_clients_response_all_of_clients_from_dict = GetClientsResponseAllOfClients.from_dict(get_clients_response_all_of_clients_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


