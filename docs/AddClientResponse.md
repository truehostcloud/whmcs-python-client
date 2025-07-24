# AddClientResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**message** | **str** | Response message | [optional] 
**clientid** | [**AddClientResponseAllOfClientid**](AddClientResponseAllOfClientid.md) |  | [optional] 
**owner_user_id** | **int** | The ID of the user that owns the client | [optional] 

## Example

```python
from whmcs_client.models.add_client_response import AddClientResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddClientResponse from a JSON string
add_client_response_instance = AddClientResponse.from_json(json)
# print the JSON string representation of the object
print(AddClientResponse.to_json())

# convert the object into a dict
add_client_response_dict = add_client_response_instance.to_dict()
# create an instance of AddClientResponse from a dict
add_client_response_from_dict = AddClientResponse.from_dict(add_client_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


