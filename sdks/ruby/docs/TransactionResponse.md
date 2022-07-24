# OpenapiClient::TransactionResponse

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **transaction_id** | **String** |  |  |
| **account_id** | **String** |  |  |
| **business_id** | **String** |  |  |
| **amount** | **Float** |  |  |
| **note** | **String** |  | [optional] |
| **payment_provider** | **String** |  | [optional] |
| **payment_id** | **String** |  | [optional] |
| **created_at** | **Float** |  |  |
| **modified_at** | **Float** |  |  |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::TransactionResponse.new(
  transaction_id: null,
  account_id: null,
  business_id: null,
  amount: null,
  note: null,
  payment_provider: null,
  payment_id: null,
  created_at: null,
  modified_at: null
)
```

