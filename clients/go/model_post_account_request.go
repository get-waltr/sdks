/*


No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

API version: 0.0.0
*/

// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

package openapi

import (
	"encoding/json"
)

// PostAccountRequest struct for PostAccountRequest
type PostAccountRequest struct {
	// This is your own internal account ID. We will index it based upon your business ID.
	AccountId string `json:"accountId"`
	AccountName *string `json:"accountName,omitempty"`
}

// NewPostAccountRequest instantiates a new PostAccountRequest object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewPostAccountRequest(accountId string) *PostAccountRequest {
	this := PostAccountRequest{}
	this.AccountId = accountId
	return &this
}

// NewPostAccountRequestWithDefaults instantiates a new PostAccountRequest object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewPostAccountRequestWithDefaults() *PostAccountRequest {
	this := PostAccountRequest{}
	return &this
}

// GetAccountId returns the AccountId field value
func (o *PostAccountRequest) GetAccountId() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.AccountId
}

// GetAccountIdOk returns a tuple with the AccountId field value
// and a boolean to check if the value has been set.
func (o *PostAccountRequest) GetAccountIdOk() (*string, bool) {
	if o == nil {
		return nil, false
	}
	return &o.AccountId, true
}

// SetAccountId sets field value
func (o *PostAccountRequest) SetAccountId(v string) {
	o.AccountId = v
}

// GetAccountName returns the AccountName field value if set, zero value otherwise.
func (o *PostAccountRequest) GetAccountName() string {
	if o == nil || o.AccountName == nil {
		var ret string
		return ret
	}
	return *o.AccountName
}

// GetAccountNameOk returns a tuple with the AccountName field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *PostAccountRequest) GetAccountNameOk() (*string, bool) {
	if o == nil || o.AccountName == nil {
		return nil, false
	}
	return o.AccountName, true
}

// HasAccountName returns a boolean if a field has been set.
func (o *PostAccountRequest) HasAccountName() bool {
	if o != nil && o.AccountName != nil {
		return true
	}

	return false
}

// SetAccountName gets a reference to the given string and assigns it to the AccountName field.
func (o *PostAccountRequest) SetAccountName(v string) {
	o.AccountName = &v
}

func (o PostAccountRequest) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if true {
		toSerialize["accountId"] = o.AccountId
	}
	if o.AccountName != nil {
		toSerialize["accountName"] = o.AccountName
	}
	return json.Marshal(toSerialize)
}

type NullablePostAccountRequest struct {
	value *PostAccountRequest
	isSet bool
}

func (v NullablePostAccountRequest) Get() *PostAccountRequest {
	return v.value
}

func (v *NullablePostAccountRequest) Set(val *PostAccountRequest) {
	v.value = val
	v.isSet = true
}

func (v NullablePostAccountRequest) IsSet() bool {
	return v.isSet
}

func (v *NullablePostAccountRequest) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullablePostAccountRequest(val *PostAccountRequest) *NullablePostAccountRequest {
	return &NullablePostAccountRequest{value: val, isSet: true}
}

func (v NullablePostAccountRequest) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullablePostAccountRequest) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}


