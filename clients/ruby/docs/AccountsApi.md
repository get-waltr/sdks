# OpenapiClient::AccountsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**accounts_account_id_delete**](AccountsApi.md#accounts_account_id_delete) | **DELETE** /accounts/:accountId | Delete an Account of a Business |
| [**accounts_account_id_get**](AccountsApi.md#accounts_account_id_get) | **GET** /accounts/:accountId | Get an account for a Business |
| [**accounts_account_id_patch**](AccountsApi.md#accounts_account_id_patch) | **PATCH** /accounts/:accountId | Update Account for Business |
| [**accounts_account_id_transactions_get**](AccountsApi.md#accounts_account_id_transactions_get) | **GET** /accounts/:accountId/transactions | Get Transactions for an Account |
| [**accounts_get**](AccountsApi.md#accounts_get) | **GET** /accounts | Get all Accounts for a Business |
| [**accounts_post**](AccountsApi.md#accounts_post) | **POST** /accounts | Create an Account for a Business |
| [**accounts_stats_get**](AccountsApi.md#accounts_stats_get) | **GET** /accounts/stats | Get stats for all accounts |


## accounts_account_id_delete

> Object accounts_account_id_delete

Delete an Account of a Business

Delete an Account of a Business

### Examples

```ruby
require 'time'
require 'openapi_client'

api_instance = OpenapiClient::AccountsApi.new

begin
  # Delete an Account of a Business
  result = api_instance.accounts_account_id_delete
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling AccountsApi->accounts_account_id_delete: #{e}"
end
```

#### Using the accounts_account_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> accounts_account_id_delete_with_http_info

```ruby
begin
  # Delete an Account of a Business
  data, status_code, headers = api_instance.accounts_account_id_delete_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue OpenapiClient::ApiError => e
  puts "Error when calling AccountsApi->accounts_account_id_delete_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accounts_account_id_get

> <AccountResponse> accounts_account_id_get

Get an account for a Business

Get an account for a Business

### Examples

```ruby
require 'time'
require 'openapi_client'

api_instance = OpenapiClient::AccountsApi.new

begin
  # Get an account for a Business
  result = api_instance.accounts_account_id_get
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling AccountsApi->accounts_account_id_get: #{e}"
end
```

#### Using the accounts_account_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AccountResponse>, Integer, Hash)> accounts_account_id_get_with_http_info

```ruby
begin
  # Get an account for a Business
  data, status_code, headers = api_instance.accounts_account_id_get_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AccountResponse>
rescue OpenapiClient::ApiError => e
  puts "Error when calling AccountsApi->accounts_account_id_get_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**AccountResponse**](AccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accounts_account_id_patch

> <AccountResponse> accounts_account_id_patch(patch_account_request)

Update Account for Business

Update Account for Business

### Examples

```ruby
require 'time'
require 'openapi_client'

api_instance = OpenapiClient::AccountsApi.new
patch_account_request = OpenapiClient::PatchAccountRequest.new # PatchAccountRequest | 

begin
  # Update Account for Business
  result = api_instance.accounts_account_id_patch(patch_account_request)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling AccountsApi->accounts_account_id_patch: #{e}"
end
```

#### Using the accounts_account_id_patch_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AccountResponse>, Integer, Hash)> accounts_account_id_patch_with_http_info(patch_account_request)

```ruby
begin
  # Update Account for Business
  data, status_code, headers = api_instance.accounts_account_id_patch_with_http_info(patch_account_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AccountResponse>
rescue OpenapiClient::ApiError => e
  puts "Error when calling AccountsApi->accounts_account_id_patch_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **patch_account_request** | [**PatchAccountRequest**](PatchAccountRequest.md) |  |  |

### Return type

[**AccountResponse**](AccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## accounts_account_id_transactions_get

> <AllTransactionsResponse> accounts_account_id_transactions_get

Get Transactions for an Account

Get Transactions for an Account

### Examples

```ruby
require 'time'
require 'openapi_client'

api_instance = OpenapiClient::AccountsApi.new

begin
  # Get Transactions for an Account
  result = api_instance.accounts_account_id_transactions_get
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling AccountsApi->accounts_account_id_transactions_get: #{e}"
end
```

#### Using the accounts_account_id_transactions_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AllTransactionsResponse>, Integer, Hash)> accounts_account_id_transactions_get_with_http_info

```ruby
begin
  # Get Transactions for an Account
  data, status_code, headers = api_instance.accounts_account_id_transactions_get_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AllTransactionsResponse>
rescue OpenapiClient::ApiError => e
  puts "Error when calling AccountsApi->accounts_account_id_transactions_get_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**AllTransactionsResponse**](AllTransactionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accounts_get

> <AllAccountsResponse> accounts_get

Get all Accounts for a Business

Get all Accounts for a Business

### Examples

```ruby
require 'time'
require 'openapi_client'

api_instance = OpenapiClient::AccountsApi.new

begin
  # Get all Accounts for a Business
  result = api_instance.accounts_get
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling AccountsApi->accounts_get: #{e}"
end
```

#### Using the accounts_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AllAccountsResponse>, Integer, Hash)> accounts_get_with_http_info

```ruby
begin
  # Get all Accounts for a Business
  data, status_code, headers = api_instance.accounts_get_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AllAccountsResponse>
rescue OpenapiClient::ApiError => e
  puts "Error when calling AccountsApi->accounts_get_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**AllAccountsResponse**](AllAccountsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accounts_post

> <AccountResponse> accounts_post(post_account_request)

Create an Account for a Business

Create an Account for a Business

### Examples

```ruby
require 'time'
require 'openapi_client'

api_instance = OpenapiClient::AccountsApi.new
post_account_request = OpenapiClient::PostAccountRequest.new({account_id: 'account_id_example'}) # PostAccountRequest | 

begin
  # Create an Account for a Business
  result = api_instance.accounts_post(post_account_request)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling AccountsApi->accounts_post: #{e}"
end
```

#### Using the accounts_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AccountResponse>, Integer, Hash)> accounts_post_with_http_info(post_account_request)

```ruby
begin
  # Create an Account for a Business
  data, status_code, headers = api_instance.accounts_post_with_http_info(post_account_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AccountResponse>
rescue OpenapiClient::ApiError => e
  puts "Error when calling AccountsApi->accounts_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **post_account_request** | [**PostAccountRequest**](PostAccountRequest.md) |  |  |

### Return type

[**AccountResponse**](AccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## accounts_stats_get

> <AccountStatsResponse> accounts_stats_get

Get stats for all accounts

Get stats for all accounts

### Examples

```ruby
require 'time'
require 'openapi_client'

api_instance = OpenapiClient::AccountsApi.new

begin
  # Get stats for all accounts
  result = api_instance.accounts_stats_get
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling AccountsApi->accounts_stats_get: #{e}"
end
```

#### Using the accounts_stats_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AccountStatsResponse>, Integer, Hash)> accounts_stats_get_with_http_info

```ruby
begin
  # Get stats for all accounts
  data, status_code, headers = api_instance.accounts_stats_get_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AccountStatsResponse>
rescue OpenapiClient::ApiError => e
  puts "Error when calling AccountsApi->accounts_stats_get_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**AccountStatsResponse**](AccountStatsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

