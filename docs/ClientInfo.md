# ClientInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The client ID | [optional] 
**firstname** | **str** | The client&#39;s first name | [optional] 
**lastname** | **str** | The client&#39;s last name | [optional] 
**companyname** | **str** | The client&#39;s company name | [optional] 
**email** | **str** | The client&#39;s email address | [optional] 
**datecreated** | **date** | The date the client was created | [optional] 
**groupid** | **int** | The client&#39;s group ID | [optional] 
**status** | **str** | The client&#39;s status (Active, Inactive, Closed) | [optional] 

## Example

```python
from whmcs_client.models.client_info import ClientInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClientInfo from a JSON string
client_info_instance = ClientInfo.from_json(json)
# print the JSON string representation of the object
print(ClientInfo.to_json())

# convert the object into a dict
client_info_dict = client_info_instance.to_dict()
# create an instance of ClientInfo from a dict
client_info_from_dict = ClientInfo.from_dict(client_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


