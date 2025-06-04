# GetClientsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**message** | **str** | Response message | [optional] 
**totalresults** | **int** | The total number of results available | [optional] 
**startnumber** | **int** | The starting number for the returned results | [optional] 
**numreturned** | **int** | The number of results returned | [optional] 
**clients** | [**GetClientsResponseAllOfClients**](GetClientsResponseAllOfClients.md) |  | [optional] 

## Example

```python
from whmcs_client.models.get_clients_response import GetClientsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsResponse from a JSON string
get_clients_response_instance = GetClientsResponse.from_json(json)
# print the JSON string representation of the object
print(GetClientsResponse.to_json())

# convert the object into a dict
get_clients_response_dict = get_clients_response_instance.to_dict()
# create an instance of GetClientsResponse from a dict
get_clients_response_from_dict = GetClientsResponse.from_dict(get_clients_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


