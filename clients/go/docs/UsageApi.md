# \UsageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AccountsAccountIdUsageGet**](UsageApi.md#AccountsAccountIdUsageGet) | **Get** /accounts/:accountId/usage | Get an Account&#39;s current Usage Billing Rate Adjustments
[**AccountsAccountIdUsagePost**](UsageApi.md#AccountsAccountIdUsagePost) | **Post** /accounts/:accountId/usage | Set an Account&#39;s Usage Billing Rate



## AccountsAccountIdUsageGet

> AccountUsageBillingAdjustmentsResponse AccountsAccountIdUsageGet(ctx).Execute()

Get an Account's current Usage Billing Rate Adjustments



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
    resp, r, err := apiClient.UsageApi.AccountsAccountIdUsageGet(context.Background()).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `UsageApi.AccountsAccountIdUsageGet``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `AccountsAccountIdUsageGet`: AccountUsageBillingAdjustmentsResponse
    fmt.Fprintf(os.Stdout, "Response from `UsageApi.AccountsAccountIdUsageGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiAccountsAccountIdUsageGetRequest struct via the builder pattern


### Return type

[**AccountUsageBillingAdjustmentsResponse**](AccountUsageBillingAdjustmentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## AccountsAccountIdUsagePost

> map[string]interface{} AccountsAccountIdUsagePost(ctx).PostAccountUsageBillingRateAdjustmentRequest(postAccountUsageBillingRateAdjustmentRequest).Execute()

Set an Account's Usage Billing Rate



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
    postAccountUsageBillingRateAdjustmentRequest := *openapiclient.NewPostAccountUsageBillingRateAdjustmentRequest(float32(123)) // PostAccountUsageBillingRateAdjustmentRequest | 

    configuration := openapiclient.NewConfiguration()
    apiClient := openapiclient.NewAPIClient(configuration)
    resp, r, err := apiClient.UsageApi.AccountsAccountIdUsagePost(context.Background()).PostAccountUsageBillingRateAdjustmentRequest(postAccountUsageBillingRateAdjustmentRequest).Execute()
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `UsageApi.AccountsAccountIdUsagePost``: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
    // response from `AccountsAccountIdUsagePost`: map[string]interface{}
    fmt.Fprintf(os.Stdout, "Response from `UsageApi.AccountsAccountIdUsagePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiAccountsAccountIdUsagePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **postAccountUsageBillingRateAdjustmentRequest** | [**PostAccountUsageBillingRateAdjustmentRequest**](PostAccountUsageBillingRateAdjustmentRequest.md) |  | 

### Return type

**map[string]interface{}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

