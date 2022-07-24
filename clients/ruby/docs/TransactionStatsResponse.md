# OpenapiClient::TransactionStatsResponse

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **total** | **Float** |  |  |
| **daily** | [**Array&lt;TransactionStatsResponseDailyInner&gt;**](TransactionStatsResponseDailyInner.md) |  |  |
| **monthly** | [**Array&lt;TransactionStatsResponseDailyInner&gt;**](TransactionStatsResponseDailyInner.md) |  |  |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::TransactionStatsResponse.new(
  total: null,
  daily: null,
  monthly: null
)
```

