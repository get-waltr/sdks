# OpenapiClient::PatchTransactionRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **account_id** | **String** |  | [optional] |
| **amount** | **Float** |  | [optional] |
| **note** | **String** |  | [optional] |
| **payment_provider** | [**PaymentProvider**](PaymentProvider.md) |  | [optional] |
| **payment_id** | **String** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::PatchTransactionRequest.new(
  account_id: null,
  amount: null,
  note: null,
  payment_provider: null,
  payment_id: null
)
```

