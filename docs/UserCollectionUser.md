# UserCollectionUser

Array of user information or a single user object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The user ID | [optional] 
**name** | **str** | The user name | [optional] 
**email** | **str** | The user email | [optional] 
**is_owner** | **bool** | Whether the user is the account owner | [optional] 

## Example

```python
from whmcs_client.models.user_collection_user import UserCollectionUser

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionUser from a JSON string
user_collection_user_instance = UserCollectionUser.from_json(json)
# print the JSON string representation of the object
print(UserCollectionUser.to_json())

# convert the object into a dict
user_collection_user_dict = user_collection_user_instance.to_dict()
# create an instance of UserCollectionUser from a dict
user_collection_user_from_dict = UserCollectionUser.from_dict(user_collection_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


