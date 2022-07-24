# AccountResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | **string** |  | 
**Name** | Pointer to **string** |  | [optional] 
**CreatedAt** | **float32** |  | 
**ModifiedAt** | **float32** |  | 
**UsageBillingRate** | **float32** |  | 

## Methods

### NewAccountResponse

`func NewAccountResponse(accountId string, createdAt float32, modifiedAt float32, usageBillingRate float32, ) *AccountResponse`

NewAccountResponse instantiates a new AccountResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAccountResponseWithDefaults

`func NewAccountResponseWithDefaults() *AccountResponse`

NewAccountResponseWithDefaults instantiates a new AccountResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAccountId

`func (o *AccountResponse) GetAccountId() string`

GetAccountId returns the AccountId field if non-nil, zero value otherwise.

### GetAccountIdOk

`func (o *AccountResponse) GetAccountIdOk() (*string, bool)`

GetAccountIdOk returns a tuple with the AccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountId

`func (o *AccountResponse) SetAccountId(v string)`

SetAccountId sets AccountId field to given value.


### GetName

`func (o *AccountResponse) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *AccountResponse) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *AccountResponse) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *AccountResponse) HasName() bool`

HasName returns a boolean if a field has been set.

### GetCreatedAt

`func (o *AccountResponse) GetCreatedAt() float32`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *AccountResponse) GetCreatedAtOk() (*float32, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *AccountResponse) SetCreatedAt(v float32)`

SetCreatedAt sets CreatedAt field to given value.


### GetModifiedAt

`func (o *AccountResponse) GetModifiedAt() float32`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *AccountResponse) GetModifiedAtOk() (*float32, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *AccountResponse) SetModifiedAt(v float32)`

SetModifiedAt sets ModifiedAt field to given value.


### GetUsageBillingRate

`func (o *AccountResponse) GetUsageBillingRate() float32`

GetUsageBillingRate returns the UsageBillingRate field if non-nil, zero value otherwise.

### GetUsageBillingRateOk

`func (o *AccountResponse) GetUsageBillingRateOk() (*float32, bool)`

GetUsageBillingRateOk returns a tuple with the UsageBillingRate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsageBillingRate

`func (o *AccountResponse) SetUsageBillingRate(v float32)`

SetUsageBillingRate sets UsageBillingRate field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


