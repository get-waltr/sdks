/*


No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

API version: 0.0.0
*/

// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

package openapi

import (
	"encoding/json"
)

// BusinessSettingsResponse struct for BusinessSettingsResponse
type BusinessSettingsResponse struct {
	BusinessId string `json:"businessId"`
	CurrencyLabel string `json:"currencyLabel"`
	CurrencyLabelSuffixed bool `json:"currencyLabelSuffixed"`
	AccountsOverdraftable bool `json:"accountsOverdraftable"`
}

// NewBusinessSettingsResponse instantiates a new BusinessSettingsResponse object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewBusinessSettingsResponse(businessId string, currencyLabel string, currencyLabelSuffixed bool, accountsOverdraftable bool) *BusinessSettingsResponse {
	this := BusinessSettingsResponse{}
	this.BusinessId = businessId
	this.CurrencyLabel = currencyLabel
	this.CurrencyLabelSuffixed = currencyLabelSuffixed
	this.AccountsOverdraftable = accountsOverdraftable
	return &this
}

// NewBusinessSettingsResponseWithDefaults instantiates a new BusinessSettingsResponse object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewBusinessSettingsResponseWithDefaults() *BusinessSettingsResponse {
	this := BusinessSettingsResponse{}
	return &this
}

// GetBusinessId returns the BusinessId field value
func (o *BusinessSettingsResponse) GetBusinessId() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.BusinessId
}

// GetBusinessIdOk returns a tuple with the BusinessId field value
// and a boolean to check if the value has been set.
func (o *BusinessSettingsResponse) GetBusinessIdOk() (*string, bool) {
	if o == nil {
		return nil, false
	}
	return &o.BusinessId, true
}

// SetBusinessId sets field value
func (o *BusinessSettingsResponse) SetBusinessId(v string) {
	o.BusinessId = v
}

// GetCurrencyLabel returns the CurrencyLabel field value
func (o *BusinessSettingsResponse) GetCurrencyLabel() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.CurrencyLabel
}

// GetCurrencyLabelOk returns a tuple with the CurrencyLabel field value
// and a boolean to check if the value has been set.
func (o *BusinessSettingsResponse) GetCurrencyLabelOk() (*string, bool) {
	if o == nil {
		return nil, false
	}
	return &o.CurrencyLabel, true
}

// SetCurrencyLabel sets field value
func (o *BusinessSettingsResponse) SetCurrencyLabel(v string) {
	o.CurrencyLabel = v
}

// GetCurrencyLabelSuffixed returns the CurrencyLabelSuffixed field value
func (o *BusinessSettingsResponse) GetCurrencyLabelSuffixed() bool {
	if o == nil {
		var ret bool
		return ret
	}

	return o.CurrencyLabelSuffixed
}

// GetCurrencyLabelSuffixedOk returns a tuple with the CurrencyLabelSuffixed field value
// and a boolean to check if the value has been set.
func (o *BusinessSettingsResponse) GetCurrencyLabelSuffixedOk() (*bool, bool) {
	if o == nil {
		return nil, false
	}
	return &o.CurrencyLabelSuffixed, true
}

// SetCurrencyLabelSuffixed sets field value
func (o *BusinessSettingsResponse) SetCurrencyLabelSuffixed(v bool) {
	o.CurrencyLabelSuffixed = v
}

// GetAccountsOverdraftable returns the AccountsOverdraftable field value
func (o *BusinessSettingsResponse) GetAccountsOverdraftable() bool {
	if o == nil {
		var ret bool
		return ret
	}

	return o.AccountsOverdraftable
}

// GetAccountsOverdraftableOk returns a tuple with the AccountsOverdraftable field value
// and a boolean to check if the value has been set.
func (o *BusinessSettingsResponse) GetAccountsOverdraftableOk() (*bool, bool) {
	if o == nil {
		return nil, false
	}
	return &o.AccountsOverdraftable, true
}

// SetAccountsOverdraftable sets field value
func (o *BusinessSettingsResponse) SetAccountsOverdraftable(v bool) {
	o.AccountsOverdraftable = v
}

func (o BusinessSettingsResponse) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if true {
		toSerialize["businessId"] = o.BusinessId
	}
	if true {
		toSerialize["currencyLabel"] = o.CurrencyLabel
	}
	if true {
		toSerialize["currencyLabelSuffixed"] = o.CurrencyLabelSuffixed
	}
	if true {
		toSerialize["accountsOverdraftable"] = o.AccountsOverdraftable
	}
	return json.Marshal(toSerialize)
}

type NullableBusinessSettingsResponse struct {
	value *BusinessSettingsResponse
	isSet bool
}

func (v NullableBusinessSettingsResponse) Get() *BusinessSettingsResponse {
	return v.value
}

func (v *NullableBusinessSettingsResponse) Set(val *BusinessSettingsResponse) {
	v.value = val
	v.isSet = true
}

func (v NullableBusinessSettingsResponse) IsSet() bool {
	return v.isSet
}

func (v *NullableBusinessSettingsResponse) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableBusinessSettingsResponse(val *BusinessSettingsResponse) *NullableBusinessSettingsResponse {
	return &NullableBusinessSettingsResponse{value: val, isSet: true}
}

func (v NullableBusinessSettingsResponse) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableBusinessSettingsResponse) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}


