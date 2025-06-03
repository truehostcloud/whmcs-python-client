# WHMCSErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | Always &#39;error&#39; for error responses | 
**message** | **str** | Error message describing what went wrong | 

## Example

```python
from whmcs_client.models.whmcs_error_response import WHMCSErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WHMCSErrorResponse from a JSON string
whmcs_error_response_instance = WHMCSErrorResponse.from_json(json)
# print the JSON string representation of the object
print(WHMCSErrorResponse.to_json())

# convert the object into a dict
whmcs_error_response_dict = whmcs_error_response_instance.to_dict()
# create an instance of WHMCSErrorResponse from a dict
whmcs_error_response_from_dict = WHMCSErrorResponse.from_dict(whmcs_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


