# BusinessSettingsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BusinessId** | **string** |  | 
**CurrencyLabel** | **string** |  | 
**CurrencyLabelSuffixed** | **bool** |  | 
**AccountsOverdraftable** | **bool** |  | 

## Methods

### NewBusinessSettingsResponse

`func NewBusinessSettingsResponse(businessId string, currencyLabel string, currencyLabelSuffixed bool, accountsOverdraftable bool, ) *BusinessSettingsResponse`

NewBusinessSettingsResponse instantiates a new BusinessSettingsResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBusinessSettingsResponseWithDefaults

`func NewBusinessSettingsResponseWithDefaults() *BusinessSettingsResponse`

NewBusinessSettingsResponseWithDefaults instantiates a new BusinessSettingsResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBusinessId

`func (o *BusinessSettingsResponse) GetBusinessId() string`

GetBusinessId returns the BusinessId field if non-nil, zero value otherwise.

### GetBusinessIdOk

`func (o *BusinessSettingsResponse) GetBusinessIdOk() (*string, bool)`

GetBusinessIdOk returns a tuple with the BusinessId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBusinessId

`func (o *BusinessSettingsResponse) SetBusinessId(v string)`

SetBusinessId sets BusinessId field to given value.


### GetCurrencyLabel

`func (o *BusinessSettingsResponse) GetCurrencyLabel() string`

GetCurrencyLabel returns the CurrencyLabel field if non-nil, zero value otherwise.

### GetCurrencyLabelOk

`func (o *BusinessSettingsResponse) GetCurrencyLabelOk() (*string, bool)`

GetCurrencyLabelOk returns a tuple with the CurrencyLabel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrencyLabel

`func (o *BusinessSettingsResponse) SetCurrencyLabel(v string)`

SetCurrencyLabel sets CurrencyLabel field to given value.


### GetCurrencyLabelSuffixed

`func (o *BusinessSettingsResponse) GetCurrencyLabelSuffixed() bool`

GetCurrencyLabelSuffixed returns the CurrencyLabelSuffixed field if non-nil, zero value otherwise.

### GetCurrencyLabelSuffixedOk

`func (o *BusinessSettingsResponse) GetCurrencyLabelSuffixedOk() (*bool, bool)`

GetCurrencyLabelSuffixedOk returns a tuple with the CurrencyLabelSuffixed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrencyLabelSuffixed

`func (o *BusinessSettingsResponse) SetCurrencyLabelSuffixed(v bool)`

SetCurrencyLabelSuffixed sets CurrencyLabelSuffixed field to given value.


### GetAccountsOverdraftable

`func (o *BusinessSettingsResponse) GetAccountsOverdraftable() bool`

GetAccountsOverdraftable returns the AccountsOverdraftable field if non-nil, zero value otherwise.

### GetAccountsOverdraftableOk

`func (o *BusinessSettingsResponse) GetAccountsOverdraftableOk() (*bool, bool)`

GetAccountsOverdraftableOk returns a tuple with the AccountsOverdraftable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountsOverdraftable

`func (o *BusinessSettingsResponse) SetAccountsOverdraftable(v bool)`

SetAccountsOverdraftable sets AccountsOverdraftable field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


