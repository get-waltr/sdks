# OpenapiClient::PostAccountRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **account_id** | **String** | This is your own internal account ID. We will index it based upon your business ID. |  |
| **account_name** | **String** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::PostAccountRequest.new(
  account_id: null,
  account_name: null
)
```

