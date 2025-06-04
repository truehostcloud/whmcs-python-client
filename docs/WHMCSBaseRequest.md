# WHMCSBaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Admin username/API identifier | 
**password** | **str** | Admin password/API secret | 
**accesskey** | **str** | Optional API access key | [optional] 
**responsetype** | **str** | Response format | [optional] [default to 'json']

## Example

```python
from whmcs_client.models.whmcs_base_request import WHMCSBaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WHMCSBaseRequest from a JSON string
whmcs_base_request_instance = WHMCSBaseRequest.from_json(json)
# print the JSON string representation of the object
print(WHMCSBaseRequest.to_json())

# convert the object into a dict
whmcs_base_request_dict = whmcs_base_request_instance.to_dict()
# create an instance of WHMCSBaseRequest from a dict
whmcs_base_request_from_dict = WHMCSBaseRequest.from_dict(whmcs_base_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


