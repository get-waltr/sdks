# OpenapiClient::AccountResponse

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **business_id** | **String** |  |  |
| **account_id** | **String** |  |  |
| **account_name** | **String** |  | [optional] |
| **created_at** | **Float** |  |  |
| **modified_at** | **Float** |  |  |
| **balance** | **Float** |  |  |
| **usage_billing_rate** | **Float** |  |  |
| **remaining_hours_on_balance** | **Float** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::AccountResponse.new(
  business_id: null,
  account_id: null,
  account_name: null,
  created_at: null,
  modified_at: null,
  balance: null,
  usage_billing_rate: null,
  remaining_hours_on_balance: null
)
```

