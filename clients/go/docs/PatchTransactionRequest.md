# PatchTransactionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | Pointer to **string** |  | [optional] 
**Amount** | Pointer to **float32** |  | [optional] 
**Note** | Pointer to **string** |  | [optional] 
**PaymentProvider** | Pointer to [**PaymentProvider**](PaymentProvider.md) |  | [optional] 
**PaymentId** | Pointer to **string** |  | [optional] 

## Methods

### NewPatchTransactionRequest

`func NewPatchTransactionRequest() *PatchTransactionRequest`

NewPatchTransactionRequest instantiates a new PatchTransactionRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPatchTransactionRequestWithDefaults

`func NewPatchTransactionRequestWithDefaults() *PatchTransactionRequest`

NewPatchTransactionRequestWithDefaults instantiates a new PatchTransactionRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAccountId

`func (o *PatchTransactionRequest) GetAccountId() string`

GetAccountId returns the AccountId field if non-nil, zero value otherwise.

### GetAccountIdOk

`func (o *PatchTransactionRequest) GetAccountIdOk() (*string, bool)`

GetAccountIdOk returns a tuple with the AccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountId

`func (o *PatchTransactionRequest) SetAccountId(v string)`

SetAccountId sets AccountId field to given value.

### HasAccountId

`func (o *PatchTransactionRequest) HasAccountId() bool`

HasAccountId returns a boolean if a field has been set.

### GetAmount

`func (o *PatchTransactionRequest) GetAmount() float32`

GetAmount returns the Amount field if non-nil, zero value otherwise.

### GetAmountOk

`func (o *PatchTransactionRequest) GetAmountOk() (*float32, bool)`

GetAmountOk returns a tuple with the Amount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAmount

`func (o *PatchTransactionRequest) SetAmount(v float32)`

SetAmount sets Amount field to given value.

### HasAmount

`func (o *PatchTransactionRequest) HasAmount() bool`

HasAmount returns a boolean if a field has been set.

### GetNote

`func (o *PatchTransactionRequest) GetNote() string`

GetNote returns the Note field if non-nil, zero value otherwise.

### GetNoteOk

`func (o *PatchTransactionRequest) GetNoteOk() (*string, bool)`

GetNoteOk returns a tuple with the Note field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNote

`func (o *PatchTransactionRequest) SetNote(v string)`

SetNote sets Note field to given value.

### HasNote

`func (o *PatchTransactionRequest) HasNote() bool`

HasNote returns a boolean if a field has been set.

### GetPaymentProvider

`func (o *PatchTransactionRequest) GetPaymentProvider() PaymentProvider`

GetPaymentProvider returns the PaymentProvider field if non-nil, zero value otherwise.

### GetPaymentProviderOk

`func (o *PatchTransactionRequest) GetPaymentProviderOk() (*PaymentProvider, bool)`

GetPaymentProviderOk returns a tuple with the PaymentProvider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPaymentProvider

`func (o *PatchTransactionRequest) SetPaymentProvider(v PaymentProvider)`

SetPaymentProvider sets PaymentProvider field to given value.

### HasPaymentProvider

`func (o *PatchTransactionRequest) HasPaymentProvider() bool`

HasPaymentProvider returns a boolean if a field has been set.

### GetPaymentId

`func (o *PatchTransactionRequest) GetPaymentId() string`

GetPaymentId returns the PaymentId field if non-nil, zero value otherwise.

### GetPaymentIdOk

`func (o *PatchTransactionRequest) GetPaymentIdOk() (*string, bool)`

GetPaymentIdOk returns a tuple with the PaymentId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPaymentId

`func (o *PatchTransactionRequest) SetPaymentId(v string)`

SetPaymentId sets PaymentId field to given value.

### HasPaymentId

`func (o *PatchTransactionRequest) HasPaymentId() bool`

HasPaymentId returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


