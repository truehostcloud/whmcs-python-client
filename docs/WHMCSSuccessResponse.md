# WHMCSSuccessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**message** | **str** | Response message | [optional] 

## Example

```python
from whmcs_client.models.whmcs_success_response import WHMCSSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WHMCSSuccessResponse from a JSON string
whmcs_success_response_instance = WHMCSSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(WHMCSSuccessResponse.to_json())

# convert the object into a dict
whmcs_success_response_dict = whmcs_success_response_instance.to_dict()
# create an instance of WHMCSSuccessResponse from a dict
whmcs_success_response_from_dict = WHMCSSuccessResponse.from_dict(whmcs_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


