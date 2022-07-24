# OpenAPI\Client\BusinessesApi

All URIs are relative to http://localhost.

Method | HTTP request | Description
------------- | ------------- | -------------
[**businessBusinessIdSettingsGet()**](BusinessesApi.md#businessBusinessIdSettingsGet) | **GET** /business/:businessId/settings | Get Settings for a business
[**businessesBusinessIdGet()**](BusinessesApi.md#businessesBusinessIdGet) | **GET** /businesses/:businessId | Get Business Details
[**businessesBusinessIdPatch()**](BusinessesApi.md#businessesBusinessIdPatch) | **PATCH** /businesses/:businessId | Update Business Details


## `businessBusinessIdSettingsGet()`

```php
businessBusinessIdSettingsGet(): \OpenAPI\Client\Model\BusinessSettingsResponse
```

Get Settings for a business

Get Settings for a business

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\BusinessesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->businessBusinessIdSettingsGet();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BusinessesApi->businessBusinessIdSettingsGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\OpenAPI\Client\Model\BusinessSettingsResponse**](../Model/BusinessSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `businessesBusinessIdGet()`

```php
businessesBusinessIdGet(): \OpenAPI\Client\Model\BusinessResponse
```

Get Business Details

Use this to get the name and other business details. Here is a link: [to google](https://google.com). Let's see if it works.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\BusinessesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);

try {
    $result = $apiInstance->businessesBusinessIdGet();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BusinessesApi->businessesBusinessIdGet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\OpenAPI\Client\Model\BusinessResponse**](../Model/BusinessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `businessesBusinessIdPatch()`

```php
businessesBusinessIdPatch($patch_business_request): \OpenAPI\Client\Model\BusinessResponse
```

Update Business Details

Update Business Details

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');



$apiInstance = new OpenAPI\Client\Api\BusinessesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$patch_business_request = new \OpenAPI\Client\Model\PatchBusinessRequest(); // \OpenAPI\Client\Model\PatchBusinessRequest

try {
    $result = $apiInstance->businessesBusinessIdPatch($patch_business_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BusinessesApi->businessesBusinessIdPatch: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_business_request** | [**\OpenAPI\Client\Model\PatchBusinessRequest**](../Model/PatchBusinessRequest.md)|  |

### Return type

[**\OpenAPI\Client\Model\BusinessResponse**](../Model/BusinessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
