# OpenAPI\Client\TransactionsApi

All URIs are relative to http://localhost:3333.

Method | HTTP request | Description
------------- | ------------- | -------------
[**transactionsGet()**](TransactionsApi.md#transactionsGet) | **GET** /transactions | Get all Transactions for a Business
[**transactionsPost()**](TransactionsApi.md#transactionsPost) | **POST** /transactions | Creates a Transaction for an Business
[**transactionsStatsGet()**](TransactionsApi.md#transactionsStatsGet) | **GET** /transactions/stats | Get stats for all Transactions
[**transactionsTransactionIdDelete()**](TransactionsApi.md#transactionsTransactionIdDelete) | **DELETE** /transactions/:transactionId | Delete Transaction for an Business
[**transactionsTransactionIdGet()**](TransactionsApi.md#transactionsTransactionIdGet) | **GET** /transactions/:transactionId | Get a Transaction for a Business
[**transactionsTransactionIdPatch()**](TransactionsApi.md#transactionsTransactionIdPatch) | **PATCH** /transactions/:transactionId | Update a Transaction for a Business


## `transactionsGet()`

```php
transactionsGet(): \OpenAPI\Client\Model\AllTransactionsResponse
```

Get all Transactions for a Business

Get all Transactions for a Business

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: ApiKeyAuth
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('X-API-Key', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('X-API-Key', 'Bearer');


$apiInstance = new OpenAPI\Client\Api\TransactionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->transactionsGet();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TransactionsApi->transactionsGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\OpenAPI\Client\Model\AllTransactionsResponse**](../Model/AllTransactionsResponse.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `transactionsPost()`

```php
transactionsPost($post_transaction_request): \OpenAPI\Client\Model\TransactionResponse
```

Creates a Transaction for an Business

Creates a Transaction for an Business

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: ApiKeyAuth
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('X-API-Key', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('X-API-Key', 'Bearer');


$apiInstance = new OpenAPI\Client\Api\TransactionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$post_transaction_request = new \OpenAPI\Client\Model\PostTransactionRequest(); // \OpenAPI\Client\Model\PostTransactionRequest

try {
    $result = $apiInstance->transactionsPost($post_transaction_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TransactionsApi->transactionsPost: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_transaction_request** | [**\OpenAPI\Client\Model\PostTransactionRequest**](../Model/PostTransactionRequest.md)|  |

### Return type

[**\OpenAPI\Client\Model\TransactionResponse**](../Model/TransactionResponse.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `transactionsStatsGet()`

```php
transactionsStatsGet(): \OpenAPI\Client\Model\TransactionStatsResponse
```

Get stats for all Transactions

Get stats for all Transactions

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: ApiKeyAuth
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('X-API-Key', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('X-API-Key', 'Bearer');


$apiInstance = new OpenAPI\Client\Api\TransactionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->transactionsStatsGet();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TransactionsApi->transactionsStatsGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\OpenAPI\Client\Model\TransactionStatsResponse**](../Model/TransactionStatsResponse.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `transactionsTransactionIdDelete()`

```php
transactionsTransactionIdDelete(): object
```

Delete Transaction for an Business

Delete Transaction for an Business

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: ApiKeyAuth
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('X-API-Key', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('X-API-Key', 'Bearer');


$apiInstance = new OpenAPI\Client\Api\TransactionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->transactionsTransactionIdDelete();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TransactionsApi->transactionsTransactionIdDelete: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `transactionsTransactionIdGet()`

```php
transactionsTransactionIdGet(): \OpenAPI\Client\Model\TransactionResponse
```

Get a Transaction for a Business

Get a Transaction for a Business

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: ApiKeyAuth
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('X-API-Key', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('X-API-Key', 'Bearer');


$apiInstance = new OpenAPI\Client\Api\TransactionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->transactionsTransactionIdGet();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TransactionsApi->transactionsTransactionIdGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\OpenAPI\Client\Model\TransactionResponse**](../Model/TransactionResponse.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `transactionsTransactionIdPatch()`

```php
transactionsTransactionIdPatch($patch_transaction_request): \OpenAPI\Client\Model\TransactionResponse
```

Update a Transaction for a Business

Update a Transaction for a Business

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: ApiKeyAuth
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('X-API-Key', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('X-API-Key', 'Bearer');


$apiInstance = new OpenAPI\Client\Api\TransactionsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$patch_transaction_request = new \OpenAPI\Client\Model\PatchTransactionRequest(); // \OpenAPI\Client\Model\PatchTransactionRequest

try {
    $result = $apiInstance->transactionsTransactionIdPatch($patch_transaction_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling TransactionsApi->transactionsTransactionIdPatch: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_transaction_request** | [**\OpenAPI\Client\Model\PatchTransactionRequest**](../Model/PatchTransactionRequest.md)|  |

### Return type

[**\OpenAPI\Client\Model\TransactionResponse**](../Model/TransactionResponse.md)

### Authorization

[ApiKeyAuth](../../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
