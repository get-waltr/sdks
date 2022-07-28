# AllTransactionsResponseTransactions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Items** | [**[]TransactionResponse**](TransactionResponse.md) |  | 
**Count** | **float32** |  | 
**ScannedCount** | **float32** |  | 
**LastEvaluatedKey** | **map[string]string** |  | 

## Methods

### NewAllTransactionsResponseTransactions

`func NewAllTransactionsResponseTransactions(items []TransactionResponse, count float32, scannedCount float32, lastEvaluatedKey map[string]string, ) *AllTransactionsResponseTransactions`

NewAllTransactionsResponseTransactions instantiates a new AllTransactionsResponseTransactions object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAllTransactionsResponseTransactionsWithDefaults

`func NewAllTransactionsResponseTransactionsWithDefaults() *AllTransactionsResponseTransactions`

NewAllTransactionsResponseTransactionsWithDefaults instantiates a new AllTransactionsResponseTransactions object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetItems

`func (o *AllTransactionsResponseTransactions) GetItems() []TransactionResponse`

GetItems returns the Items field if non-nil, zero value otherwise.

### GetItemsOk

`func (o *AllTransactionsResponseTransactions) GetItemsOk() (*[]TransactionResponse, bool)`

GetItemsOk returns a tuple with the Items field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItems

`func (o *AllTransactionsResponseTransactions) SetItems(v []TransactionResponse)`

SetItems sets Items field to given value.


### GetCount

`func (o *AllTransactionsResponseTransactions) GetCount() float32`

GetCount returns the Count field if non-nil, zero value otherwise.

### GetCountOk

`func (o *AllTransactionsResponseTransactions) GetCountOk() (*float32, bool)`

GetCountOk returns a tuple with the Count field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCount

`func (o *AllTransactionsResponseTransactions) SetCount(v float32)`

SetCount sets Count field to given value.


### GetScannedCount

`func (o *AllTransactionsResponseTransactions) GetScannedCount() float32`

GetScannedCount returns the ScannedCount field if non-nil, zero value otherwise.

### GetScannedCountOk

`func (o *AllTransactionsResponseTransactions) GetScannedCountOk() (*float32, bool)`

GetScannedCountOk returns a tuple with the ScannedCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScannedCount

`func (o *AllTransactionsResponseTransactions) SetScannedCount(v float32)`

SetScannedCount sets ScannedCount field to given value.


### GetLastEvaluatedKey

`func (o *AllTransactionsResponseTransactions) GetLastEvaluatedKey() map[string]string`

GetLastEvaluatedKey returns the LastEvaluatedKey field if non-nil, zero value otherwise.

### GetLastEvaluatedKeyOk

`func (o *AllTransactionsResponseTransactions) GetLastEvaluatedKeyOk() (*map[string]string, bool)`

GetLastEvaluatedKeyOk returns a tuple with the LastEvaluatedKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastEvaluatedKey

`func (o *AllTransactionsResponseTransactions) SetLastEvaluatedKey(v map[string]string)`

SetLastEvaluatedKey sets LastEvaluatedKey field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


