/*


No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

API version: 0.0.0
*/

// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

package openapi

import (
	"encoding/json"
)

// TransactionStatsResponse struct for TransactionStatsResponse
type TransactionStatsResponse struct {
	Total float32 `json:"total"`
	Daily []TransactionStatsResponseDailyInner `json:"daily"`
	Monthly []TransactionStatsResponseDailyInner `json:"monthly"`
}

// NewTransactionStatsResponse instantiates a new TransactionStatsResponse object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewTransactionStatsResponse(total float32, daily []TransactionStatsResponseDailyInner, monthly []TransactionStatsResponseDailyInner) *TransactionStatsResponse {
	this := TransactionStatsResponse{}
	this.Total = total
	this.Daily = daily
	this.Monthly = monthly
	return &this
}

// NewTransactionStatsResponseWithDefaults instantiates a new TransactionStatsResponse object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewTransactionStatsResponseWithDefaults() *TransactionStatsResponse {
	this := TransactionStatsResponse{}
	return &this
}

// GetTotal returns the Total field value
func (o *TransactionStatsResponse) GetTotal() float32 {
	if o == nil {
		var ret float32
		return ret
	}

	return o.Total
}

// GetTotalOk returns a tuple with the Total field value
// and a boolean to check if the value has been set.
func (o *TransactionStatsResponse) GetTotalOk() (*float32, bool) {
	if o == nil {
		return nil, false
	}
	return &o.Total, true
}

// SetTotal sets field value
func (o *TransactionStatsResponse) SetTotal(v float32) {
	o.Total = v
}

// GetDaily returns the Daily field value
func (o *TransactionStatsResponse) GetDaily() []TransactionStatsResponseDailyInner {
	if o == nil {
		var ret []TransactionStatsResponseDailyInner
		return ret
	}

	return o.Daily
}

// GetDailyOk returns a tuple with the Daily field value
// and a boolean to check if the value has been set.
func (o *TransactionStatsResponse) GetDailyOk() ([]TransactionStatsResponseDailyInner, bool) {
	if o == nil {
		return nil, false
	}
	return o.Daily, true
}

// SetDaily sets field value
func (o *TransactionStatsResponse) SetDaily(v []TransactionStatsResponseDailyInner) {
	o.Daily = v
}

// GetMonthly returns the Monthly field value
func (o *TransactionStatsResponse) GetMonthly() []TransactionStatsResponseDailyInner {
	if o == nil {
		var ret []TransactionStatsResponseDailyInner
		return ret
	}

	return o.Monthly
}

// GetMonthlyOk returns a tuple with the Monthly field value
// and a boolean to check if the value has been set.
func (o *TransactionStatsResponse) GetMonthlyOk() ([]TransactionStatsResponseDailyInner, bool) {
	if o == nil {
		return nil, false
	}
	return o.Monthly, true
}

// SetMonthly sets field value
func (o *TransactionStatsResponse) SetMonthly(v []TransactionStatsResponseDailyInner) {
	o.Monthly = v
}

func (o TransactionStatsResponse) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if true {
		toSerialize["total"] = o.Total
	}
	if true {
		toSerialize["daily"] = o.Daily
	}
	if true {
		toSerialize["monthly"] = o.Monthly
	}
	return json.Marshal(toSerialize)
}

type NullableTransactionStatsResponse struct {
	value *TransactionStatsResponse
	isSet bool
}

func (v NullableTransactionStatsResponse) Get() *TransactionStatsResponse {
	return v.value
}

func (v *NullableTransactionStatsResponse) Set(val *TransactionStatsResponse) {
	v.value = val
	v.isSet = true
}

func (v NullableTransactionStatsResponse) IsSet() bool {
	return v.isSet
}

func (v *NullableTransactionStatsResponse) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableTransactionStatsResponse(val *TransactionStatsResponse) *NullableTransactionStatsResponse {
	return &NullableTransactionStatsResponse{value: val, isSet: true}
}

func (v NullableTransactionStatsResponse) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableTransactionStatsResponse) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}

