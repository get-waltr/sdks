# openapi_client.AccountsApi

All URIs are relative to *http://localhost:3333*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_account_id_delete**](AccountsApi.md#accounts_account_id_delete) | **DELETE** /accounts/:accountId | Delete an Account of a Business
[**accounts_account_id_get**](AccountsApi.md#accounts_account_id_get) | **GET** /accounts/:accountId | Get an account for a Business
[**accounts_account_id_patch**](AccountsApi.md#accounts_account_id_patch) | **PATCH** /accounts/:accountId | Update Account for Business
[**accounts_account_id_transactions_get**](AccountsApi.md#accounts_account_id_transactions_get) | **GET** /accounts/:accountId/transactions | Get Transactions for an Account
[**accounts_get**](AccountsApi.md#accounts_get) | **GET** /accounts | Get all Accounts for a Business
[**accounts_post**](AccountsApi.md#accounts_post) | **POST** /accounts | Create an Account for a Business


# **accounts_account_id_delete**
> object accounts_account_id_delete()

Delete an Account of a Business

Delete an Account of a Business

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
    api_instance = openapi_client.AccountsApi(api_client)
    
    try:
        # Delete an Account of a Business
        api_response = api_instance.accounts_account_id_delete()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_account_id_delete: %s\n" % e)
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

# **accounts_account_id_get**
> AccountResponse accounts_account_id_get()

Get an account for a Business

Get an account for a Business

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
    api_instance = openapi_client.AccountsApi(api_client)
    
    try:
        # Get an account for a Business
        api_response = api_instance.accounts_account_id_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_account_id_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountResponse**](AccountResponse.md)

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

# **accounts_account_id_patch**
> AccountResponse accounts_account_id_patch(patch_account_request)

Update Account for Business

Update Account for Business

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
    api_instance = openapi_client.AccountsApi(api_client)
    patch_account_request = openapi_client.PatchAccountRequest() # PatchAccountRequest | 

    try:
        # Update Account for Business
        api_response = api_instance.accounts_account_id_patch(patch_account_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_account_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_account_request** | [**PatchAccountRequest**](PatchAccountRequest.md)|  | 

### Return type

[**AccountResponse**](AccountResponse.md)

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

# **accounts_account_id_transactions_get**
> AllTransactionsResponse accounts_account_id_transactions_get()

Get Transactions for an Account

Get Transactions for an Account

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
    api_instance = openapi_client.AccountsApi(api_client)
    
    try:
        # Get Transactions for an Account
        api_response = api_instance.accounts_account_id_transactions_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_account_id_transactions_get: %s\n" % e)
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
**404** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get**
> AllAccountsResponse accounts_get()

Get all Accounts for a Business

Get all Accounts for a Business

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
    api_instance = openapi_client.AccountsApi(api_client)
    
    try:
        # Get all Accounts for a Business
        api_response = api_instance.accounts_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AllAccountsResponse**](AllAccountsResponse.md)

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

# **accounts_post**
> AccountResponse accounts_post(post_account_request)

Create an Account for a Business

Create an Account for a Business

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
    api_instance = openapi_client.AccountsApi(api_client)
    post_account_request = openapi_client.PostAccountRequest() # PostAccountRequest | 

    try:
        # Create an Account for a Business
        api_response = api_instance.accounts_post(post_account_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->accounts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_account_request** | [**PostAccountRequest**](PostAccountRequest.md)|  | 

### Return type

[**AccountResponse**](AccountResponse.md)

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
**409** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

