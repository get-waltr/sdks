# OpenapiClient::BusinessesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**business_business_id_settings_get**](BusinessesApi.md#business_business_id_settings_get) | **GET** /business/:businessId/settings | Get Settings for a business |
| [**businesses_business_id_get**](BusinessesApi.md#businesses_business_id_get) | **GET** /businesses/:businessId | Get Business Details |
| [**businesses_business_id_patch**](BusinessesApi.md#businesses_business_id_patch) | **PATCH** /businesses/:businessId | Update Business Details |


## business_business_id_settings_get

> <BusinessSettingsResponse> business_business_id_settings_get

Get Settings for a business

Get Settings for a business

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

api_instance = OpenapiClient::BusinessesApi.new

begin
  # Get Settings for a business
  result = api_instance.business_business_id_settings_get
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling BusinessesApi->business_business_id_settings_get: #{e}"
end
```

#### Using the business_business_id_settings_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BusinessSettingsResponse>, Integer, Hash)> business_business_id_settings_get_with_http_info

```ruby
begin
  # Get Settings for a business
  data, status_code, headers = api_instance.business_business_id_settings_get_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BusinessSettingsResponse>
rescue OpenapiClient::ApiError => e
  puts "Error when calling BusinessesApi->business_business_id_settings_get_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**BusinessSettingsResponse**](BusinessSettingsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## businesses_business_id_get

> <BusinessResponse> businesses_business_id_get

Get Business Details

 Use this to get the name and other business details. Here is a link: [to google](https://google.com). Let's see if it works. 

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

api_instance = OpenapiClient::BusinessesApi.new

begin
  # Get Business Details
  result = api_instance.businesses_business_id_get
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling BusinessesApi->businesses_business_id_get: #{e}"
end
```

#### Using the businesses_business_id_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BusinessResponse>, Integer, Hash)> businesses_business_id_get_with_http_info

```ruby
begin
  # Get Business Details
  data, status_code, headers = api_instance.businesses_business_id_get_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BusinessResponse>
rescue OpenapiClient::ApiError => e
  puts "Error when calling BusinessesApi->businesses_business_id_get_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**BusinessResponse**](BusinessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## businesses_business_id_patch

> <BusinessResponse> businesses_business_id_patch(patch_business_request)

Update Business Details

Update Business Details

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

api_instance = OpenapiClient::BusinessesApi.new
patch_business_request = OpenapiClient::PatchBusinessRequest.new # PatchBusinessRequest | 

begin
  # Update Business Details
  result = api_instance.businesses_business_id_patch(patch_business_request)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling BusinessesApi->businesses_business_id_patch: #{e}"
end
```

#### Using the businesses_business_id_patch_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BusinessResponse>, Integer, Hash)> businesses_business_id_patch_with_http_info(patch_business_request)

```ruby
begin
  # Update Business Details
  data, status_code, headers = api_instance.businesses_business_id_patch_with_http_info(patch_business_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BusinessResponse>
rescue OpenapiClient::ApiError => e
  puts "Error when calling BusinessesApi->businesses_business_id_patch_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **patch_business_request** | [**PatchBusinessRequest**](PatchBusinessRequest.md) |  |  |

### Return type

[**BusinessResponse**](BusinessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

