# OpenapiClient::UsageApi

All URIs are relative to *http://localhost:3333*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**accounts_account_id_usage_get**](UsageApi.md#accounts_account_id_usage_get) | **GET** /accounts/:accountId/usage | Get an Account&#39;s current Usage Billing Rate Adjustments |
| [**accounts_account_id_usage_post**](UsageApi.md#accounts_account_id_usage_post) | **POST** /accounts/:accountId/usage | Set an Account&#39;s Usage Billing Rate |


## accounts_account_id_usage_get

> <AccountUsageBillingAdjustmentsResponse> accounts_account_id_usage_get

Get an Account's current Usage Billing Rate Adjustments

Get an Account's current Usage Billing Rate Adjustments

### Examples

```ruby
require 'time'
require 'openapi_client'
# setup authorization
OpenapiClient.configure do |config|
  # Configure API key authorization: ApiKeyAuth
  config.api_key['ApiKeyAuth'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['ApiKeyAuth'] = 'Bearer'
end

api_instance = OpenapiClient::UsageApi.new

begin
  # Get an Account's current Usage Billing Rate Adjustments
  result = api_instance.accounts_account_id_usage_get
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling UsageApi->accounts_account_id_usage_get: #{e}"
end
```

#### Using the accounts_account_id_usage_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AccountUsageBillingAdjustmentsResponse>, Integer, Hash)> accounts_account_id_usage_get_with_http_info

```ruby
begin
  # Get an Account's current Usage Billing Rate Adjustments
  data, status_code, headers = api_instance.accounts_account_id_usage_get_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AccountUsageBillingAdjustmentsResponse>
rescue OpenapiClient::ApiError => e
  puts "Error when calling UsageApi->accounts_account_id_usage_get_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**AccountUsageBillingAdjustmentsResponse**](AccountUsageBillingAdjustmentsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf8


## accounts_account_id_usage_post

> Object accounts_account_id_usage_post(post_account_usage_billing_rate_adjustment_request)

Set an Account's Usage Billing Rate

Set an Account's Usage Billing Rate

### Examples

```ruby
require 'time'
require 'openapi_client'
# setup authorization
OpenapiClient.configure do |config|
  # Configure API key authorization: ApiKeyAuth
  config.api_key['ApiKeyAuth'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['ApiKeyAuth'] = 'Bearer'
end

api_instance = OpenapiClient::UsageApi.new
post_account_usage_billing_rate_adjustment_request = OpenapiClient::PostAccountUsageBillingRateAdjustmentRequest.new({billing_cost: 3.56}) # PostAccountUsageBillingRateAdjustmentRequest | 

begin
  # Set an Account's Usage Billing Rate
  result = api_instance.accounts_account_id_usage_post(post_account_usage_billing_rate_adjustment_request)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling UsageApi->accounts_account_id_usage_post: #{e}"
end
```

#### Using the accounts_account_id_usage_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> accounts_account_id_usage_post_with_http_info(post_account_usage_billing_rate_adjustment_request)

```ruby
begin
  # Set an Account's Usage Billing Rate
  data, status_code, headers = api_instance.accounts_account_id_usage_post_with_http_info(post_account_usage_billing_rate_adjustment_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue OpenapiClient::ApiError => e
  puts "Error when calling UsageApi->accounts_account_id_usage_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **post_account_usage_billing_rate_adjustment_request** | [**PostAccountUsageBillingRateAdjustmentRequest**](PostAccountUsageBillingRateAdjustmentRequest.md) |  |  |

### Return type

**Object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json; charset=utf8
- **Accept**: application/json; charset=utf8

