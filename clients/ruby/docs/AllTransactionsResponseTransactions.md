# OpenapiClient::AllTransactionsResponseTransactions

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **items** | [**Array&lt;TransactionResponse&gt;**](TransactionResponse.md) |  |  |
| **count** | **Float** |  |  |
| **scanned_count** | **Float** |  |  |
| **last_evaluated_key** | **Hash&lt;String, String&gt;** |  |  |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::AllTransactionsResponseTransactions.new(
  items: null,
  count: null,
  scanned_count: null,
  last_evaluated_key: null
)
```

