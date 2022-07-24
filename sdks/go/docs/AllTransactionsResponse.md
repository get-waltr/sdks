# AllTransactionsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Transactions** | [**[]TransactionResponse**](TransactionResponse.md) |  | 

## Methods

### NewAllTransactionsResponse

`func NewAllTransactionsResponse(transactions []TransactionResponse, ) *AllTransactionsResponse`

NewAllTransactionsResponse instantiates a new AllTransactionsResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAllTransactionsResponseWithDefaults

`func NewAllTransactionsResponseWithDefaults() *AllTransactionsResponse`

NewAllTransactionsResponseWithDefaults instantiates a new AllTransactionsResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTransactions

`func (o *AllTransactionsResponse) GetTransactions() []TransactionResponse`

GetTransactions returns the Transactions field if non-nil, zero value otherwise.

### GetTransactionsOk

`func (o *AllTransactionsResponse) GetTransactionsOk() (*[]TransactionResponse, bool)`

GetTransactionsOk returns a tuple with the Transactions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTransactions

`func (o *AllTransactionsResponse) SetTransactions(v []TransactionResponse)`

SetTransactions sets Transactions field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


