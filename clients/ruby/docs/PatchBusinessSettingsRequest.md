# OpenapiClient::PatchBusinessSettingsRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **currency_label** | **String** |  | [optional] |
| **currency_label_suffixed** | **Boolean** |  | [optional] |
| **accounts_overdraftable** | **Boolean** |  | [optional] |
| **billing_type** | [**BillingType**](BillingType.md) |  | [optional] |
| **payment_providers** | **Array&lt;String&gt;** |  | [optional] |
| **stripe_sandbox_publishable_key** | **String** |  | [optional] |
| **stripe_sandbox_secret_key** | **String** |  | [optional] |
| **stripe_publishable_key** | **String** |  | [optional] |
| **stripe_secret_key** | **String** |  | [optional] |
| **paypal_client_id** | **String** |  | [optional] |
| **paypal_client_secret** | **String** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::PatchBusinessSettingsRequest.new(
  currency_label: null,
  currency_label_suffixed: null,
  accounts_overdraftable: null,
  billing_type: null,
  payment_providers: null,
  stripe_sandbox_publishable_key: null,
  stripe_sandbox_secret_key: null,
  stripe_publishable_key: null,
  stripe_secret_key: null,
  paypal_client_id: null,
  paypal_client_secret: null
)
```

