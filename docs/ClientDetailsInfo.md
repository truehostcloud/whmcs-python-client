# ClientDetailsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The client email address | [optional] 
**phonenumber** | **str** | Phone number | [optional] 

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


