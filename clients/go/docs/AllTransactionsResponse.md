# AllTransactionsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Transactions** | [**AllTransactionsResponseTransactions**](AllTransactionsResponseTransactions.md) |  | 
**Total** | **float32** |  | 

## Methods

### NewAllTransactionsResponse

`func NewAllTransactionsResponse(transactions AllTransactionsResponseTransactions, total float32, ) *AllTransactionsResponse`

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

`func (o *AllTransactionsResponse) GetTransactions() AllTransactionsResponseTransactions`

GetTransactions returns the Transactions field if non-nil, zero value otherwise.

### GetTransactionsOk

`func (o *AllTransactionsResponse) GetTransactionsOk() (*AllTransactionsResponseTransactions, bool)`

GetTransactionsOk returns a tuple with the Transactions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTransactions

`func (o *AllTransactionsResponse) SetTransactions(v AllTransactionsResponseTransactions)`

SetTransactions sets Transactions field to given value.


### GetTotal

`func (o *AllTransactionsResponse) GetTotal() float32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *AllTransactionsResponse) GetTotalOk() (*float32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *AllTransactionsResponse) SetTotal(v float32)`

SetTotal sets Total field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


