# \TransactionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**TransactionsGet**](TransactionsApi.md#TransactionsGet) | **Get** /transactions | Get all Transactions for a Business
[**TransactionsPost**](TransactionsApi.md#TransactionsPost) | **Post** /transactions | Creates a Transaction for an Business
[**TransactionsStatsGet**](TransactionsApi.md#TransactionsStatsGet) | **Get** /transactions/stats | Get stats for all Transactions
[**TransactionsTransactionIdDelete**](TransactionsApi.md#TransactionsTransactionIdDelete) | **Delete** /transactions/:transactionId | Delete Transaction for an Business
[**TransactionsTransactionIdGet**](TransactionsApi.md#TransactionsTransactionIdGet) | **Get** /transactions/:transactionId | Get a Transaction for a Business
[**TransactionsTransactionIdPatch**](TransactionsApi.md#TransactionsTransactionIdPatch) | **Patch** /transactions/:transactionId | Update a Transaction for a Business



## TransactionsGet

> AllTransactionsResponse TransactionsGet(ctx).Execute()

Get all Transactions for a Business



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
    resp, r, err := apiClient.TransactionsApi.TransactionsGet(context.Background()).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TransactionsApi.TransactionsGet``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `TransactionsGet`: AllTransactionsResponse
    fmt.Fprintf(os.Stdout, "Response from `TransactionsApi.TransactionsGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiTransactionsGetRequest struct via the builder pattern


### Return type

[**AllTransactionsResponse**](AllTransactionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TransactionsPost

> TransactionResponse TransactionsPost(ctx).PostTransactionRequest(postTransactionRequest).Execute()

Creates a Transaction for an Business



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
    postTransactionRequest := *openapiclient.NewPostTransactionRequest("AccountId_example", float32(123)) // PostTransactionRequest | 

    configuration := openapiclient.NewConfiguration()
    apiClient := openapiclient.NewAPIClient(configuration)
    resp, r, err := apiClient.TransactionsApi.TransactionsPost(context.Background()).PostTransactionRequest(postTransactionRequest).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TransactionsApi.TransactionsPost``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `TransactionsPost`: TransactionResponse
    fmt.Fprintf(os.Stdout, "Response from `TransactionsApi.TransactionsPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTransactionsPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **postTransactionRequest** | [**PostTransactionRequest**](PostTransactionRequest.md) |  | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TransactionsStatsGet

> TransactionStatsResponse TransactionsStatsGet(ctx).Execute()

Get stats for all Transactions



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
    resp, r, err := apiClient.TransactionsApi.TransactionsStatsGet(context.Background()).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TransactionsApi.TransactionsStatsGet``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `TransactionsStatsGet`: TransactionStatsResponse
    fmt.Fprintf(os.Stdout, "Response from `TransactionsApi.TransactionsStatsGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiTransactionsStatsGetRequest struct via the builder pattern


### Return type

[**TransactionStatsResponse**](TransactionStatsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TransactionsTransactionIdDelete

> map[string]interface{} TransactionsTransactionIdDelete(ctx).Execute()

Delete Transaction for an Business



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
    resp, r, err := apiClient.TransactionsApi.TransactionsTransactionIdDelete(context.Background()).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TransactionsApi.TransactionsTransactionIdDelete``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `TransactionsTransactionIdDelete`: map[string]interface{}
    fmt.Fprintf(os.Stdout, "Response from `TransactionsApi.TransactionsTransactionIdDelete`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiTransactionsTransactionIdDeleteRequest struct via the builder pattern


### Return type

**map[string]interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TransactionsTransactionIdGet

> TransactionResponse TransactionsTransactionIdGet(ctx).Execute()

Get a Transaction for a Business



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
    resp, r, err := apiClient.TransactionsApi.TransactionsTransactionIdGet(context.Background()).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TransactionsApi.TransactionsTransactionIdGet``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `TransactionsTransactionIdGet`: TransactionResponse
    fmt.Fprintf(os.Stdout, "Response from `TransactionsApi.TransactionsTransactionIdGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiTransactionsTransactionIdGetRequest struct via the builder pattern


### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TransactionsTransactionIdPatch

> TransactionResponse TransactionsTransactionIdPatch(ctx).PatchTransactionRequest(patchTransactionRequest).Execute()

Update a Transaction for a Business



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
    patchTransactionRequest := *openapiclient.NewPatchTransactionRequest() // PatchTransactionRequest | 

    configuration := openapiclient.NewConfiguration()
    apiClient := openapiclient.NewAPIClient(configuration)
    resp, r, err := apiClient.TransactionsApi.TransactionsTransactionIdPatch(context.Background()).PatchTransactionRequest(patchTransactionRequest).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `TransactionsApi.TransactionsTransactionIdPatch``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `TransactionsTransactionIdPatch`: TransactionResponse
    fmt.Fprintf(os.Stdout, "Response from `TransactionsApi.TransactionsTransactionIdPatch`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiTransactionsTransactionIdPatchRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patchTransactionRequest** | [**PatchTransactionRequest**](PatchTransactionRequest.md) |  | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

