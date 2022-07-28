# AccountResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BusinessId** | **string** |  | 
**AccountId** | **string** |  | 
**AccountName** | Pointer to **string** |  | [optional] 
**CreatedAt** | **float32** |  | 
**ModifiedAt** | **float32** |  | 
**Balance** | **float32** |  | 
**UsageBillingRate** | **float32** |  | 
**RemainingHoursOnBalance** | Pointer to **float32** |  | [optional] 

## Methods

### NewAccountResponse

`func NewAccountResponse(businessId string, accountId string, createdAt float32, modifiedAt float32, balance float32, usageBillingRate float32, ) *AccountResponse`

NewAccountResponse instantiates a new AccountResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAccountResponseWithDefaults

`func NewAccountResponseWithDefaults() *AccountResponse`

NewAccountResponseWithDefaults instantiates a new AccountResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBusinessId

`func (o *AccountResponse) GetBusinessId() string`

GetBusinessId returns the BusinessId field if non-nil, zero value otherwise.

### GetBusinessIdOk

`func (o *AccountResponse) GetBusinessIdOk() (*string, bool)`

GetBusinessIdOk returns a tuple with the BusinessId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBusinessId

`func (o *AccountResponse) SetBusinessId(v string)`

SetBusinessId sets BusinessId field to given value.


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


### GetAccountName

`func (o *AccountResponse) GetAccountName() string`

GetAccountName returns the AccountName field if non-nil, zero value otherwise.

### GetAccountNameOk

`func (o *AccountResponse) GetAccountNameOk() (*string, bool)`

GetAccountNameOk returns a tuple with the AccountName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountName

`func (o *AccountResponse) SetAccountName(v string)`

SetAccountName sets AccountName field to given value.

### HasAccountName

`func (o *AccountResponse) HasAccountName() bool`

HasAccountName returns a boolean if a field has been set.

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


### GetBalance

`func (o *AccountResponse) GetBalance() float32`

GetBalance returns the Balance field if non-nil, zero value otherwise.

### GetBalanceOk

`func (o *AccountResponse) GetBalanceOk() (*float32, bool)`

GetBalanceOk returns a tuple with the Balance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBalance

`func (o *AccountResponse) SetBalance(v float32)`

SetBalance sets Balance field to given value.


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


### GetRemainingHoursOnBalance

`func (o *AccountResponse) GetRemainingHoursOnBalance() float32`

GetRemainingHoursOnBalance returns the RemainingHoursOnBalance field if non-nil, zero value otherwise.

### GetRemainingHoursOnBalanceOk

`func (o *AccountResponse) GetRemainingHoursOnBalanceOk() (*float32, bool)`

GetRemainingHoursOnBalanceOk returns a tuple with the RemainingHoursOnBalance field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemainingHoursOnBalance

`func (o *AccountResponse) SetRemainingHoursOnBalance(v float32)`

SetRemainingHoursOnBalance sets RemainingHoursOnBalance field to given value.

### HasRemainingHoursOnBalance

`func (o *AccountResponse) HasRemainingHoursOnBalance() bool`

HasRemainingHoursOnBalance returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


