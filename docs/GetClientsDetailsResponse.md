# GetClientsDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**message** | **str** | Response message | [optional] 
**client** | [**ClientDetailsInfo**](ClientDetailsInfo.md) |  | [optional] 
**stats** | **Dict[str, object]** |  | [optional] 

## Example

```python
from whmcs_client.models.get_clients_details_response import GetClientsDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsDetailsResponse from a JSON string
get_clients_details_response_instance = GetClientsDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(GetClientsDetailsResponse.to_json())

# convert the object into a dict
get_clients_details_response_dict = get_clients_details_response_instance.to_dict()
# create an instance of GetClientsDetailsResponse from a dict
get_clients_details_response_from_dict = GetClientsDetailsResponse.from_dict(get_clients_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


