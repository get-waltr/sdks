# ErrorResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TransactionId** | **string** |  | 
**AccountId** | **string** |  | 
**BusinessId** | **string** |  | 
**Amount** | **float32** |  | 
**Note** | Pointer to **string** |  | [optional] 
**PaymentProvider** | Pointer to **string** |  | [optional] 
**PaymentId** | Pointer to **string** |  | [optional] 
**CreatedAt** | **float32** |  | 
**ModifiedAt** | **float32** |  | 

## Methods

### NewErrorResponse

`func NewErrorResponse(transactionId string, accountId string, businessId string, amount float32, createdAt float32, modifiedAt float32, ) *ErrorResponse`

NewErrorResponse instantiates a new ErrorResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewErrorResponseWithDefaults

`func NewErrorResponseWithDefaults() *ErrorResponse`

NewErrorResponseWithDefaults instantiates a new ErrorResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTransactionId

`func (o *ErrorResponse) GetTransactionId() string`

GetTransactionId returns the TransactionId field if non-nil, zero value otherwise.

### GetTransactionIdOk

`func (o *ErrorResponse) GetTransactionIdOk() (*string, bool)`

GetTransactionIdOk returns a tuple with the TransactionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTransactionId

`func (o *ErrorResponse) SetTransactionId(v string)`

SetTransactionId sets TransactionId field to given value.


### GetAccountId

`func (o *ErrorResponse) GetAccountId() string`

GetAccountId returns the AccountId field if non-nil, zero value otherwise.

### GetAccountIdOk

`func (o *ErrorResponse) GetAccountIdOk() (*string, bool)`

GetAccountIdOk returns a tuple with the AccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountId

`func (o *ErrorResponse) SetAccountId(v string)`

SetAccountId sets AccountId field to given value.


### GetBusinessId

`func (o *ErrorResponse) GetBusinessId() string`

GetBusinessId returns the BusinessId field if non-nil, zero value otherwise.

### GetBusinessIdOk

`func (o *ErrorResponse) GetBusinessIdOk() (*string, bool)`

GetBusinessIdOk returns a tuple with the BusinessId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBusinessId

`func (o *ErrorResponse) SetBusinessId(v string)`

SetBusinessId sets BusinessId field to given value.


### GetAmount

`func (o *ErrorResponse) GetAmount() float32`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *ErrorResponse) GetAmountOk() (*float32, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *ErrorResponse) SetAmount(v float32)`

SetAmount sets Amount field to given value.


### GetNote

`func (o *ErrorResponse) GetNote() string`

GetNote returns the Note field if non-nil, zero value otherwise.

### GetNoteOk

`func (o *ErrorResponse) GetNoteOk() (*string, bool)`

GetNoteOk returns a tuple with the Note field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNote

`func (o *ErrorResponse) SetNote(v string)`

SetNote sets Note field to given value.

### HasNote

`func (o *ErrorResponse) HasNote() bool`

HasNote returns a boolean if a field has been set.

### GetPaymentProvider

`func (o *ErrorResponse) GetPaymentProvider() string`

GetPaymentProvider returns the PaymentProvider field if non-nil, zero value otherwise.

### GetPaymentProviderOk

`func (o *ErrorResponse) GetPaymentProviderOk() (*string, bool)`

GetPaymentProviderOk returns a tuple with the PaymentProvider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPaymentProvider

`func (o *ErrorResponse) SetPaymentProvider(v string)`

SetPaymentProvider sets PaymentProvider field to given value.

### HasPaymentProvider

`func (o *ErrorResponse) HasPaymentProvider() bool`

HasPaymentProvider returns a boolean if a field has been set.

### GetPaymentId

`func (o *ErrorResponse) GetPaymentId() string`

GetPaymentId returns the PaymentId field if non-nil, zero value otherwise.

### GetPaymentIdOk

`func (o *ErrorResponse) GetPaymentIdOk() (*string, bool)`

GetPaymentIdOk returns a tuple with the PaymentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPaymentId

`func (o *ErrorResponse) SetPaymentId(v string)`

SetPaymentId sets PaymentId field to given value.

### HasPaymentId

`func (o *ErrorResponse) HasPaymentId() bool`

HasPaymentId returns a boolean if a field has been set.

### GetCreatedAt

`func (o *ErrorResponse) GetCreatedAt() float32`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ErrorResponse) GetCreatedAtOk() (*float32, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ErrorResponse) SetCreatedAt(v float32)`

SetCreatedAt sets CreatedAt field to given value.


### GetModifiedAt

`func (o *ErrorResponse) GetModifiedAt() float32`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *ErrorResponse) GetModifiedAtOk() (*float32, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *ErrorResponse) SetModifiedAt(v float32)`

SetModifiedAt sets ModifiedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


