# openapi_client.UsageApi

All URIs are relative to *http://localhost:3333*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_account_id_usage_get**](UsageApi.md#accounts_account_id_usage_get) | **GET** /accounts/:accountId/usage | Get an Account&#39;s current Usage Billing Rate Adjustments
[**accounts_account_id_usage_post**](UsageApi.md#accounts_account_id_usage_post) | **POST** /accounts/:accountId/usage | Set an Account&#39;s Usage Billing Rate


# **accounts_account_id_usage_get**
> AccountUsageBillingAdjustmentsResponse accounts_account_id_usage_get()

Get an Account's current Usage Billing Rate Adjustments

Get an Account's current Usage Billing Rate Adjustments

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UsageApi(api_client)
    
    try:
        # Get an Account's current Usage Billing Rate Adjustments
        api_response = api_instance.accounts_account_id_usage_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsageApi->accounts_account_id_usage_get: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**401** | Error |  -  |
**404** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_account_id_usage_post**
> object accounts_account_id_usage_post(post_account_usage_billing_rate_adjustment_request)

Set an Account's Usage Billing Rate

Set an Account's Usage Billing Rate

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UsageApi(api_client)
    post_account_usage_billing_rate_adjustment_request = openapi_client.PostAccountUsageBillingRateAdjustmentRequest() # PostAccountUsageBillingRateAdjustmentRequest | 

    try:
        # Set an Account's Usage Billing Rate
        api_response = api_instance.accounts_account_id_usage_post(post_account_usage_billing_rate_adjustment_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsageApi->accounts_account_id_usage_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_account_usage_billing_rate_adjustment_request** | [**PostAccountUsageBillingRateAdjustmentRequest**](PostAccountUsageBillingRateAdjustmentRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf8
 - **Accept**: application/json; charset=utf8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**400** | Error |  -  |
**401** | Error |  -  |
**404** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

