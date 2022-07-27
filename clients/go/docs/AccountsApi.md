# \AccountsApi

All URIs are relative to *http://localhost:3333*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AccountsAccountIdDelete**](AccountsApi.md#AccountsAccountIdDelete) | **Delete** /accounts/:accountId | Delete an Account of a Business
[**AccountsAccountIdGet**](AccountsApi.md#AccountsAccountIdGet) | **Get** /accounts/:accountId | Get an account for a Business
[**AccountsAccountIdPatch**](AccountsApi.md#AccountsAccountIdPatch) | **Patch** /accounts/:accountId | Update Account for Business
[**AccountsAccountIdTransactionsGet**](AccountsApi.md#AccountsAccountIdTransactionsGet) | **Get** /accounts/:accountId/transactions | Get Transactions for an Account
[**AccountsGet**](AccountsApi.md#AccountsGet) | **Get** /accounts | Get all Accounts for a Business
[**AccountsPost**](AccountsApi.md#AccountsPost) | **Post** /accounts | Create an Account for a Business
[**AccountsStatsGet**](AccountsApi.md#AccountsStatsGet) | **Get** /accounts/stats | Get stats for all accounts



## AccountsAccountIdDelete

> map[string]interface{} AccountsAccountIdDelete(ctx).Execute()

Delete an Account of a Business



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
    resp, r, err := apiClient.AccountsApi.AccountsAccountIdDelete(context.Background()).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AccountsApi.AccountsAccountIdDelete``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `AccountsAccountIdDelete`: map[string]interface{}
    fmt.Fprintf(os.Stdout, "Response from `AccountsApi.AccountsAccountIdDelete`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiAccountsAccountIdDeleteRequest struct via the builder pattern


### Return type

**map[string]interface{}**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## AccountsAccountIdGet

> AccountResponse AccountsAccountIdGet(ctx).Execute()

Get an account for a Business



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
    resp, r, err := apiClient.AccountsApi.AccountsAccountIdGet(context.Background()).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AccountsApi.AccountsAccountIdGet``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `AccountsAccountIdGet`: AccountResponse
    fmt.Fprintf(os.Stdout, "Response from `AccountsApi.AccountsAccountIdGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiAccountsAccountIdGetRequest struct via the builder pattern


### Return type

[**AccountResponse**](AccountResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## AccountsAccountIdPatch

> AccountResponse AccountsAccountIdPatch(ctx).PatchAccountRequest(patchAccountRequest).Execute()

Update Account for Business



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
    patchAccountRequest := *openapiclient.NewPatchAccountRequest() // PatchAccountRequest | 

    configuration := openapiclient.NewConfiguration()
    apiClient := openapiclient.NewAPIClient(configuration)
    resp, r, err := apiClient.AccountsApi.AccountsAccountIdPatch(context.Background()).PatchAccountRequest(patchAccountRequest).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AccountsApi.AccountsAccountIdPatch``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `AccountsAccountIdPatch`: AccountResponse
    fmt.Fprintf(os.Stdout, "Response from `AccountsApi.AccountsAccountIdPatch`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiAccountsAccountIdPatchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patchAccountRequest** | [**PatchAccountRequest**](PatchAccountRequest.md) |  | 

### Return type

[**AccountResponse**](AccountResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## AccountsAccountIdTransactionsGet

> AllTransactionsResponse AccountsAccountIdTransactionsGet(ctx).Execute()

Get Transactions for an Account



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
    resp, r, err := apiClient.AccountsApi.AccountsAccountIdTransactionsGet(context.Background()).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AccountsApi.AccountsAccountIdTransactionsGet``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `AccountsAccountIdTransactionsGet`: AllTransactionsResponse
    fmt.Fprintf(os.Stdout, "Response from `AccountsApi.AccountsAccountIdTransactionsGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiAccountsAccountIdTransactionsGetRequest struct via the builder pattern


### Return type

[**AllTransactionsResponse**](AllTransactionsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## AccountsGet

> AllAccountsResponse AccountsGet(ctx).Execute()

Get all Accounts for a Business



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
    resp, r, err := apiClient.AccountsApi.AccountsGet(context.Background()).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AccountsApi.AccountsGet``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `AccountsGet`: AllAccountsResponse
    fmt.Fprintf(os.Stdout, "Response from `AccountsApi.AccountsGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiAccountsGetRequest struct via the builder pattern


### Return type

[**AllAccountsResponse**](AllAccountsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## AccountsPost

> AccountResponse AccountsPost(ctx).PostAccountRequest(postAccountRequest).Execute()

Create an Account for a Business



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
    postAccountRequest := *openapiclient.NewPostAccountRequest("AccountId_example") // PostAccountRequest | 

    configuration := openapiclient.NewConfiguration()
    apiClient := openapiclient.NewAPIClient(configuration)
    resp, r, err := apiClient.AccountsApi.AccountsPost(context.Background()).PostAccountRequest(postAccountRequest).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AccountsApi.AccountsPost``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `AccountsPost`: AccountResponse
    fmt.Fprintf(os.Stdout, "Response from `AccountsApi.AccountsPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiAccountsPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **postAccountRequest** | [**PostAccountRequest**](PostAccountRequest.md) |  | 

### Return type

[**AccountResponse**](AccountResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## AccountsStatsGet

> AccountStatsResponse AccountsStatsGet(ctx).Execute()

Get stats for all accounts



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
    resp, r, err := apiClient.AccountsApi.AccountsStatsGet(context.Background()).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `AccountsApi.AccountsStatsGet``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `AccountsStatsGet`: AccountStatsResponse
    fmt.Fprintf(os.Stdout, "Response from `AccountsApi.AccountsStatsGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiAccountsStatsGetRequest struct via the builder pattern


### Return type

[**AccountStatsResponse**](AccountStatsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

