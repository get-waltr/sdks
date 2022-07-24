# TransactionStatsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Total** | **float32** |  | 
**Daily** | [**[]TransactionStatsResponseDailyInner**](TransactionStatsResponseDailyInner.md) |  | 
**Monthly** | [**[]TransactionStatsResponseDailyInner**](TransactionStatsResponseDailyInner.md) |  | 

## Methods

### NewTransactionStatsResponse

`func NewTransactionStatsResponse(total float32, daily []TransactionStatsResponseDailyInner, monthly []TransactionStatsResponseDailyInner, ) *TransactionStatsResponse`

NewTransactionStatsResponse instantiates a new TransactionStatsResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTransactionStatsResponseWithDefaults

`func NewTransactionStatsResponseWithDefaults() *TransactionStatsResponse`

NewTransactionStatsResponseWithDefaults instantiates a new TransactionStatsResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTotal

`func (o *TransactionStatsResponse) GetTotal() float32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *TransactionStatsResponse) GetTotalOk() (*float32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *TransactionStatsResponse) SetTotal(v float32)`

SetTotal sets Total field to given value.


### GetDaily

`func (o *TransactionStatsResponse) GetDaily() []TransactionStatsResponseDailyInner`

GetDaily returns the Daily field if non-nil, zero value otherwise.

### GetDailyOk

`func (o *TransactionStatsResponse) GetDailyOk() (*[]TransactionStatsResponseDailyInner, bool)`

GetDailyOk returns a tuple with the Daily field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDaily

`func (o *TransactionStatsResponse) SetDaily(v []TransactionStatsResponseDailyInner)`

SetDaily sets Daily field to given value.


### GetMonthly

`func (o *TransactionStatsResponse) GetMonthly() []TransactionStatsResponseDailyInner`

GetMonthly returns the Monthly field if non-nil, zero value otherwise.

### GetMonthlyOk

`func (o *TransactionStatsResponse) GetMonthlyOk() (*[]TransactionStatsResponseDailyInner, bool)`

GetMonthlyOk returns a tuple with the Monthly field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMonthly

`func (o *TransactionStatsResponse) SetMonthly(v []TransactionStatsResponseDailyInner)`

SetMonthly sets Monthly field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


