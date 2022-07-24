# PatchBusinessSettingsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CurrencyLabel** | Pointer to **string** |  | [optional] 
**CurrencyLabelSuffixed** | Pointer to **bool** |  | [optional] 
**AccountsOverdraftable** | Pointer to **bool** |  | [optional] 
**BillingType** | Pointer to [**BillingType**](BillingType.md) |  | [optional] 
**PaymentProviders** | Pointer to **[]string** |  | [optional] 
**StripeSandboxPublishableKey** | Pointer to **string** |  | [optional] 
**StripeSandboxSecretKey** | Pointer to **string** |  | [optional] 
**StripePublishableKey** | Pointer to **string** |  | [optional] 
**StripeSecretKey** | Pointer to **string** |  | [optional] 
**PaypalClientId** | Pointer to **string** |  | [optional] 
**PaypalClientSecret** | Pointer to **string** |  | [optional] 

## Methods

### NewPatchBusinessSettingsRequest

`func NewPatchBusinessSettingsRequest() *PatchBusinessSettingsRequest`

NewPatchBusinessSettingsRequest instantiates a new PatchBusinessSettingsRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPatchBusinessSettingsRequestWithDefaults

`func NewPatchBusinessSettingsRequestWithDefaults() *PatchBusinessSettingsRequest`

NewPatchBusinessSettingsRequestWithDefaults instantiates a new PatchBusinessSettingsRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCurrencyLabel

`func (o *PatchBusinessSettingsRequest) GetCurrencyLabel() string`

GetCurrencyLabel returns the CurrencyLabel field if non-nil, zero value otherwise.

### GetCurrencyLabelOk

`func (o *PatchBusinessSettingsRequest) GetCurrencyLabelOk() (*string, bool)`

GetCurrencyLabelOk returns a tuple with the CurrencyLabel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrencyLabel

`func (o *PatchBusinessSettingsRequest) SetCurrencyLabel(v string)`

SetCurrencyLabel sets CurrencyLabel field to given value.

### HasCurrencyLabel

`func (o *PatchBusinessSettingsRequest) HasCurrencyLabel() bool`

HasCurrencyLabel returns a boolean if a field has been set.

### GetCurrencyLabelSuffixed

`func (o *PatchBusinessSettingsRequest) GetCurrencyLabelSuffixed() bool`

GetCurrencyLabelSuffixed returns the CurrencyLabelSuffixed field if non-nil, zero value otherwise.

### GetCurrencyLabelSuffixedOk

`func (o *PatchBusinessSettingsRequest) GetCurrencyLabelSuffixedOk() (*bool, bool)`

GetCurrencyLabelSuffixedOk returns a tuple with the CurrencyLabelSuffixed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCurrencyLabelSuffixed

`func (o *PatchBusinessSettingsRequest) SetCurrencyLabelSuffixed(v bool)`

SetCurrencyLabelSuffixed sets CurrencyLabelSuffixed field to given value.

### HasCurrencyLabelSuffixed

`func (o *PatchBusinessSettingsRequest) HasCurrencyLabelSuffixed() bool`

HasCurrencyLabelSuffixed returns a boolean if a field has been set.

### GetAccountsOverdraftable

`func (o *PatchBusinessSettingsRequest) GetAccountsOverdraftable() bool`

GetAccountsOverdraftable returns the AccountsOverdraftable field if non-nil, zero value otherwise.

### GetAccountsOverdraftableOk

`func (o *PatchBusinessSettingsRequest) GetAccountsOverdraftableOk() (*bool, bool)`

GetAccountsOverdraftableOk returns a tuple with the AccountsOverdraftable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountsOverdraftable

`func (o *PatchBusinessSettingsRequest) SetAccountsOverdraftable(v bool)`

SetAccountsOverdraftable sets AccountsOverdraftable field to given value.

### HasAccountsOverdraftable

`func (o *PatchBusinessSettingsRequest) HasAccountsOverdraftable() bool`

HasAccountsOverdraftable returns a boolean if a field has been set.

### GetBillingType

`func (o *PatchBusinessSettingsRequest) GetBillingType() BillingType`

GetBillingType returns the BillingType field if non-nil, zero value otherwise.

### GetBillingTypeOk

`func (o *PatchBusinessSettingsRequest) GetBillingTypeOk() (*BillingType, bool)`

GetBillingTypeOk returns a tuple with the BillingType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBillingType

`func (o *PatchBusinessSettingsRequest) SetBillingType(v BillingType)`

SetBillingType sets BillingType field to given value.

### HasBillingType

`func (o *PatchBusinessSettingsRequest) HasBillingType() bool`

HasBillingType returns a boolean if a field has been set.

### GetPaymentProviders

`func (o *PatchBusinessSettingsRequest) GetPaymentProviders() []string`

GetPaymentProviders returns the PaymentProviders field if non-nil, zero value otherwise.

### GetPaymentProvidersOk

`func (o *PatchBusinessSettingsRequest) GetPaymentProvidersOk() (*[]string, bool)`

GetPaymentProvidersOk returns a tuple with the PaymentProviders field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPaymentProviders

`func (o *PatchBusinessSettingsRequest) SetPaymentProviders(v []string)`

SetPaymentProviders sets PaymentProviders field to given value.

### HasPaymentProviders

`func (o *PatchBusinessSettingsRequest) HasPaymentProviders() bool`

HasPaymentProviders returns a boolean if a field has been set.

### GetStripeSandboxPublishableKey

`func (o *PatchBusinessSettingsRequest) GetStripeSandboxPublishableKey() string`

GetStripeSandboxPublishableKey returns the StripeSandboxPublishableKey field if non-nil, zero value otherwise.

### GetStripeSandboxPublishableKeyOk

`func (o *PatchBusinessSettingsRequest) GetStripeSandboxPublishableKeyOk() (*string, bool)`

GetStripeSandboxPublishableKeyOk returns a tuple with the StripeSandboxPublishableKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStripeSandboxPublishableKey

`func (o *PatchBusinessSettingsRequest) SetStripeSandboxPublishableKey(v string)`

SetStripeSandboxPublishableKey sets StripeSandboxPublishableKey field to given value.

### HasStripeSandboxPublishableKey

`func (o *PatchBusinessSettingsRequest) HasStripeSandboxPublishableKey() bool`

HasStripeSandboxPublishableKey returns a boolean if a field has been set.

### GetStripeSandboxSecretKey

`func (o *PatchBusinessSettingsRequest) GetStripeSandboxSecretKey() string`

GetStripeSandboxSecretKey returns the StripeSandboxSecretKey field if non-nil, zero value otherwise.

### GetStripeSandboxSecretKeyOk

`func (o *PatchBusinessSettingsRequest) GetStripeSandboxSecretKeyOk() (*string, bool)`

GetStripeSandboxSecretKeyOk returns a tuple with the StripeSandboxSecretKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStripeSandboxSecretKey

`func (o *PatchBusinessSettingsRequest) SetStripeSandboxSecretKey(v string)`

SetStripeSandboxSecretKey sets StripeSandboxSecretKey field to given value.

### HasStripeSandboxSecretKey

`func (o *PatchBusinessSettingsRequest) HasStripeSandboxSecretKey() bool`

HasStripeSandboxSecretKey returns a boolean if a field has been set.

### GetStripePublishableKey

`func (o *PatchBusinessSettingsRequest) GetStripePublishableKey() string`

GetStripePublishableKey returns the StripePublishableKey field if non-nil, zero value otherwise.

### GetStripePublishableKeyOk

`func (o *PatchBusinessSettingsRequest) GetStripePublishableKeyOk() (*string, bool)`

GetStripePublishableKeyOk returns a tuple with the StripePublishableKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStripePublishableKey

`func (o *PatchBusinessSettingsRequest) SetStripePublishableKey(v string)`

SetStripePublishableKey sets StripePublishableKey field to given value.

### HasStripePublishableKey

`func (o *PatchBusinessSettingsRequest) HasStripePublishableKey() bool`

HasStripePublishableKey returns a boolean if a field has been set.

### GetStripeSecretKey

`func (o *PatchBusinessSettingsRequest) GetStripeSecretKey() string`

GetStripeSecretKey returns the StripeSecretKey field if non-nil, zero value otherwise.

### GetStripeSecretKeyOk

`func (o *PatchBusinessSettingsRequest) GetStripeSecretKeyOk() (*string, bool)`

GetStripeSecretKeyOk returns a tuple with the StripeSecretKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStripeSecretKey

`func (o *PatchBusinessSettingsRequest) SetStripeSecretKey(v string)`

SetStripeSecretKey sets StripeSecretKey field to given value.

### HasStripeSecretKey

`func (o *PatchBusinessSettingsRequest) HasStripeSecretKey() bool`

HasStripeSecretKey returns a boolean if a field has been set.

### GetPaypalClientId

`func (o *PatchBusinessSettingsRequest) GetPaypalClientId() string`

GetPaypalClientId returns the PaypalClientId field if non-nil, zero value otherwise.

### GetPaypalClientIdOk

`func (o *PatchBusinessSettingsRequest) GetPaypalClientIdOk() (*string, bool)`

GetPaypalClientIdOk returns a tuple with the PaypalClientId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPaypalClientId

`func (o *PatchBusinessSettingsRequest) SetPaypalClientId(v string)`

SetPaypalClientId sets PaypalClientId field to given value.

### HasPaypalClientId

`func (o *PatchBusinessSettingsRequest) HasPaypalClientId() bool`

HasPaypalClientId returns a boolean if a field has been set.

### GetPaypalClientSecret

`func (o *PatchBusinessSettingsRequest) GetPaypalClientSecret() string`

GetPaypalClientSecret returns the PaypalClientSecret field if non-nil, zero value otherwise.

### GetPaypalClientSecretOk

`func (o *PatchBusinessSettingsRequest) GetPaypalClientSecretOk() (*string, bool)`

GetPaypalClientSecretOk returns a tuple with the PaypalClientSecret field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPaypalClientSecret

`func (o *PatchBusinessSettingsRequest) SetPaypalClientSecret(v string)`

SetPaypalClientSecret sets PaypalClientSecret field to given value.

### HasPaypalClientSecret

`func (o *PatchBusinessSettingsRequest) HasPaypalClientSecret() bool`

HasPaypalClientSecret returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


