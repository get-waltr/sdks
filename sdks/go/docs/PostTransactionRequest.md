# PostTransactionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | **string** |  | 
**Amount** | **float32** |  | 
**Note** | Pointer to **string** |  | [optional] 
**PaymentProvider** | Pointer to [**PaymentProvider**](PaymentProvider.md) |  | [optional] 
**PaymentId** | Pointer to **string** |  | [optional] 

## Methods

### NewPostTransactionRequest

`func NewPostTransactionRequest(accountId string, amount float32, ) *PostTransactionRequest`

NewPostTransactionRequest instantiates a new PostTransactionRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPostTransactionRequestWithDefaults

`func NewPostTransactionRequestWithDefaults() *PostTransactionRequest`

NewPostTransactionRequestWithDefaults instantiates a new PostTransactionRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAccountId

`func (o *PostTransactionRequest) GetAccountId() string`

GetAccountId returns the AccountId field if non-nil, zero value otherwise.

### GetAccountIdOk

`func (o *PostTransactionRequest) GetAccountIdOk() (*string, bool)`

GetAccountIdOk returns a tuple with the AccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountId

`func (o *PostTransactionRequest) SetAccountId(v string)`

SetAccountId sets AccountId field to given value.


### GetAmount

`func (o *PostTransactionRequest) GetAmount() float32`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *PostTransactionRequest) GetAmountOk() (*float32, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *PostTransactionRequest) SetAmount(v float32)`

SetAmount sets Amount field to given value.


### GetNote

`func (o *PostTransactionRequest) GetNote() string`

GetNote returns the Note field if non-nil, zero value otherwise.

### GetNoteOk

`func (o *PostTransactionRequest) GetNoteOk() (*string, bool)`

GetNoteOk returns a tuple with the Note field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNote

`func (o *PostTransactionRequest) SetNote(v string)`

SetNote sets Note field to given value.

### HasNote

`func (o *PostTransactionRequest) HasNote() bool`

HasNote returns a boolean if a field has been set.

### GetPaymentProvider

`func (o *PostTransactionRequest) GetPaymentProvider() PaymentProvider`

GetPaymentProvider returns the PaymentProvider field if non-nil, zero value otherwise.

### GetPaymentProviderOk

`func (o *PostTransactionRequest) GetPaymentProviderOk() (*PaymentProvider, bool)`

GetPaymentProviderOk returns a tuple with the PaymentProvider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPaymentProvider

`func (o *PostTransactionRequest) SetPaymentProvider(v PaymentProvider)`

SetPaymentProvider sets PaymentProvider field to given value.

### HasPaymentProvider

`func (o *PostTransactionRequest) HasPaymentProvider() bool`

HasPaymentProvider returns a boolean if a field has been set.

### GetPaymentId

`func (o *PostTransactionRequest) GetPaymentId() string`

GetPaymentId returns the PaymentId field if non-nil, zero value otherwise.

### GetPaymentIdOk

`func (o *PostTransactionRequest) GetPaymentIdOk() (*string, bool)`

GetPaymentIdOk returns a tuple with the PaymentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPaymentId

`func (o *PostTransactionRequest) SetPaymentId(v string)`

SetPaymentId sets PaymentId field to given value.

### HasPaymentId

`func (o *PostTransactionRequest) HasPaymentId() bool`

HasPaymentId returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


