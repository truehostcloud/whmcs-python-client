# WHMCSBaseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | Result status (success or error) | [optional] 
**message** | **str** | Response message | [optional] 

## Example

```python
from whmcs_client.models.whmcs_base_response import WHMCSBaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WHMCSBaseResponse from a JSON string
whmcs_base_response_instance = WHMCSBaseResponse.from_json(json)
# print the JSON string representation of the object
print(WHMCSBaseResponse.to_json())

# convert the object into a dict
whmcs_base_response_dict = whmcs_base_response_instance.to_dict()
# create an instance of WHMCSBaseResponse from a dict
whmcs_base_response_from_dict = WHMCSBaseResponse.from_dict(whmcs_base_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


