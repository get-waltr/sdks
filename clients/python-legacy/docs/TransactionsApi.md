# openapi_client.TransactionsApi

All URIs are relative to *http://localhost:3333*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transactions_get**](TransactionsApi.md#transactions_get) | **GET** /transactions | Get all Transactions for a Business
[**transactions_post**](TransactionsApi.md#transactions_post) | **POST** /transactions | Creates a Transaction for an Business
[**transactions_transaction_id_delete**](TransactionsApi.md#transactions_transaction_id_delete) | **DELETE** /transactions/:transactionId | Delete Transaction for an Business
[**transactions_transaction_id_get**](TransactionsApi.md#transactions_transaction_id_get) | **GET** /transactions/:transactionId | Get a Transaction for a Business
[**transactions_transaction_id_patch**](TransactionsApi.md#transactions_transaction_id_patch) | **PATCH** /transactions/:transactionId | Update a Transaction for a Business


# **transactions_get**
> AllTransactionsResponse transactions_get()

Get all Transactions for a Business

Get all Transactions for a Business

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
    api_instance = openapi_client.TransactionsApi(api_client)
    
    try:
        # Get all Transactions for a Business
        api_response = api_instance.transactions_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionsApi->transactions_get: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**401** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_post**
> TransactionResponse transactions_post(post_transaction_request)

Creates a Transaction for an Business

Creates a Transaction for an Business

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
    api_instance = openapi_client.TransactionsApi(api_client)
    post_transaction_request = openapi_client.PostTransactionRequest() # PostTransactionRequest | 

    try:
        # Creates a Transaction for an Business
        api_response = api_instance.transactions_post(post_transaction_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionsApi->transactions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_transaction_request** | [**PostTransactionRequest**](PostTransactionRequest.md)|  | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_transaction_id_delete**
> object transactions_transaction_id_delete()

Delete Transaction for an Business

Delete Transaction for an Business

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
    api_instance = openapi_client.TransactionsApi(api_client)
    
    try:
        # Delete Transaction for an Business
        api_response = api_instance.transactions_transaction_id_delete()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionsApi->transactions_transaction_id_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

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

# **transactions_transaction_id_get**
> TransactionResponse transactions_transaction_id_get()

Get a Transaction for a Business

Get a Transaction for a Business

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
    api_instance = openapi_client.TransactionsApi(api_client)
    
    try:
        # Get a Transaction for a Business
        api_response = api_instance.transactions_transaction_id_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionsApi->transactions_transaction_id_get: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**401** | Error |  -  |
**404** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_transaction_id_patch**
> TransactionResponse transactions_transaction_id_patch(patch_transaction_request)

Update a Transaction for a Business

Update a Transaction for a Business

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
    api_instance = openapi_client.TransactionsApi(api_client)
    patch_transaction_request = openapi_client.PatchTransactionRequest() # PatchTransactionRequest | 

    try:
        # Update a Transaction for a Business
        api_response = api_instance.transactions_transaction_id_patch(patch_transaction_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionsApi->transactions_transaction_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_transaction_request** | [**PatchTransactionRequest**](PatchTransactionRequest.md)|  | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

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

