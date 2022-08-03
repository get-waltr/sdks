# OpenapiClient::TransactionsApi

All URIs are relative to *http://localhost:3333*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**transactions_get**](TransactionsApi.md#transactions_get) | **GET** /transactions | Get all Transactions for a Business |
| [**transactions_post**](TransactionsApi.md#transactions_post) | **POST** /transactions | Creates a Transaction for an Business |
| [**transactions_transaction_id_delete**](TransactionsApi.md#transactions_transaction_id_delete) | **DELETE** /transactions/:transactionId | Delete Transaction for an Business |
| [**transactions_transaction_id_get**](TransactionsApi.md#transactions_transaction_id_get) | **GET** /transactions/:transactionId | Get a Transaction for a Business |
| [**transactions_transaction_id_patch**](TransactionsApi.md#transactions_transaction_id_patch) | **PATCH** /transactions/:transactionId | Update a Transaction for a Business |


## transactions_get

> <AllTransactionsResponse> transactions_get

Get all Transactions for a Business

Get all Transactions for a Business

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

api_instance = OpenapiClient::TransactionsApi.new

begin
  # Get all Transactions for a Business
  result = api_instance.transactions_get
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling TransactionsApi->transactions_get: #{e}"
end
```

#### Using the transactions_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<AllTransactionsResponse>, Integer, Hash)> transactions_get_with_http_info

```ruby
begin
  # Get all Transactions for a Business
  data, status_code, headers = api_instance.transactions_get_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <AllTransactionsResponse>
rescue OpenapiClient::ApiError => e
  puts "Error when calling TransactionsApi->transactions_get_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**AllTransactionsResponse**](AllTransactionsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf8


## transactions_post

> <TransactionResponse> transactions_post(post_transaction_request)

Creates a Transaction for an Business

Creates a Transaction for an Business

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

api_instance = OpenapiClient::TransactionsApi.new
post_transaction_request = OpenapiClient::PostTransactionRequest.new({account_id: 'account_id_example', amount: 3.56}) # PostTransactionRequest | 

begin
  # Creates a Transaction for an Business
  result = api_instance.transactions_post(post_transaction_request)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling TransactionsApi->transactions_post: #{e}"
end
```

#### Using the transactions_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TransactionResponse>, Integer, Hash)> transactions_post_with_http_info(post_transaction_request)

```ruby
begin
  # Creates a Transaction for an Business
  data, status_code, headers = api_instance.transactions_post_with_http_info(post_transaction_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TransactionResponse>
rescue OpenapiClient::ApiError => e
  puts "Error when calling TransactionsApi->transactions_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **post_transaction_request** | [**PostTransactionRequest**](PostTransactionRequest.md) |  |  |

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json; charset=utf8
- **Accept**: application/json; charset=utf8


## transactions_transaction_id_delete

> Object transactions_transaction_id_delete

Delete Transaction for an Business

Delete Transaction for an Business

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

api_instance = OpenapiClient::TransactionsApi.new

begin
  # Delete Transaction for an Business
  result = api_instance.transactions_transaction_id_delete
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling TransactionsApi->transactions_transaction_id_delete: #{e}"
end
```

#### Using the transactions_transaction_id_delete_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(Object, Integer, Hash)> transactions_transaction_id_delete_with_http_info

```ruby
begin
  # Delete Transaction for an Business
  data, status_code, headers = api_instance.transactions_transaction_id_delete_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => Object
rescue OpenapiClient::ApiError => e
  puts "Error when calling TransactionsApi->transactions_transaction_id_delete_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf8


## transactions_transaction_id_get

> <TransactionResponse> transactions_transaction_id_get

Get a Transaction for a Business

Get a Transaction for a Business

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

api_instance = OpenapiClient::TransactionsApi.new

begin
  # Get a Transaction for a Business
  result = api_instance.transactions_transaction_id_get
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling TransactionsApi->transactions_transaction_id_get: #{e}"
end
```

#### Using the transactions_transaction_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TransactionResponse>, Integer, Hash)> transactions_transaction_id_get_with_http_info

```ruby
begin
  # Get a Transaction for a Business
  data, status_code, headers = api_instance.transactions_transaction_id_get_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TransactionResponse>
rescue OpenapiClient::ApiError => e
  puts "Error when calling TransactionsApi->transactions_transaction_id_get_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf8


## transactions_transaction_id_patch

> <TransactionResponse> transactions_transaction_id_patch(patch_transaction_request)

Update a Transaction for a Business

Update a Transaction for a Business

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

api_instance = OpenapiClient::TransactionsApi.new
patch_transaction_request = OpenapiClient::PatchTransactionRequest.new # PatchTransactionRequest | 

begin
  # Update a Transaction for a Business
  result = api_instance.transactions_transaction_id_patch(patch_transaction_request)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling TransactionsApi->transactions_transaction_id_patch: #{e}"
end
```

#### Using the transactions_transaction_id_patch_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TransactionResponse>, Integer, Hash)> transactions_transaction_id_patch_with_http_info(patch_transaction_request)

```ruby
begin
  # Update a Transaction for a Business
  data, status_code, headers = api_instance.transactions_transaction_id_patch_with_http_info(patch_transaction_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TransactionResponse>
rescue OpenapiClient::ApiError => e
  puts "Error when calling TransactionsApi->transactions_transaction_id_patch_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **patch_transaction_request** | [**PatchTransactionRequest**](PatchTransactionRequest.md) |  |  |

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json; charset=utf8
- **Accept**: application/json; charset=utf8

