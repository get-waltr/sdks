# \BusinessesApi

All URIs are relative to *http://localhost:3333*

Method | HTTP request | Description
------------- | ------------- | -------------
[**BusinessesBusinessIdGet**](BusinessesApi.md#BusinessesBusinessIdGet) | **Get** /businesses/:businessId | Get Business Details
[**BusinessesBusinessIdPatch**](BusinessesApi.md#BusinessesBusinessIdPatch) | **Patch** /businesses/:businessId | Update Business Details
[**BusinessesBusinessIdSettingsGet**](BusinessesApi.md#BusinessesBusinessIdSettingsGet) | **Get** /businesses/:businessId/settings | Get Settings for a business



## BusinessesBusinessIdGet

> BusinessResponse BusinessesBusinessIdGet(ctx).Execute()

Get Business Details



### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {

    configuration := openapiclient.NewConfiguration()
    apiClient := openapiclient.NewAPIClient(configuration)
    resp, r, err := apiClient.BusinessesApi.BusinessesBusinessIdGet(context.Background()).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `BusinessesApi.BusinessesBusinessIdGet``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `BusinessesBusinessIdGet`: BusinessResponse
    fmt.Fprintf(os.Stdout, "Response from `BusinessesApi.BusinessesBusinessIdGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiBusinessesBusinessIdGetRequest struct via the builder pattern


### Return type

[**BusinessResponse**](BusinessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BusinessesBusinessIdPatch

> BusinessResponse BusinessesBusinessIdPatch(ctx).PatchBusinessRequest(patchBusinessRequest).Execute()

Update Business Details



### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {
    patchBusinessRequest := *openapiclient.NewPatchBusinessRequest() // PatchBusinessRequest | 

    configuration := openapiclient.NewConfiguration()
    apiClient := openapiclient.NewAPIClient(configuration)
    resp, r, err := apiClient.BusinessesApi.BusinessesBusinessIdPatch(context.Background()).PatchBusinessRequest(patchBusinessRequest).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `BusinessesApi.BusinessesBusinessIdPatch``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `BusinessesBusinessIdPatch`: BusinessResponse
    fmt.Fprintf(os.Stdout, "Response from `BusinessesApi.BusinessesBusinessIdPatch`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiBusinessesBusinessIdPatchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patchBusinessRequest** | [**PatchBusinessRequest**](PatchBusinessRequest.md) |  | 

### Return type

[**BusinessResponse**](BusinessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json; charset=utf8
- **Accept**: application/json; charset=utf8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BusinessesBusinessIdSettingsGet

> BusinessSettingsResponse BusinessesBusinessIdSettingsGet(ctx).Execute()

Get Settings for a business



### Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    openapiclient "./openapi"
)

func main() {

    configuration := openapiclient.NewConfiguration()
    apiClient := openapiclient.NewAPIClient(configuration)
    resp, r, err := apiClient.BusinessesApi.BusinessesBusinessIdSettingsGet(context.Background()).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `BusinessesApi.BusinessesBusinessIdSettingsGet``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `BusinessesBusinessIdSettingsGet`: BusinessSettingsResponse
    fmt.Fprintf(os.Stdout, "Response from `BusinessesApi.BusinessesBusinessIdSettingsGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiBusinessesBusinessIdSettingsGetRequest struct via the builder pattern


### Return type

[**BusinessSettingsResponse**](BusinessSettingsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

