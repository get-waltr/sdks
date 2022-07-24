# AccountStatsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Total** | **float32** |  | 
**Daily** | [**[]AccountStatsResponseDailyInner**](AccountStatsResponseDailyInner.md) |  | 
**Monthly** | [**[]AccountStatsResponseDailyInner**](AccountStatsResponseDailyInner.md) |  | 

## Methods

### NewAccountStatsResponse

`func NewAccountStatsResponse(total float32, daily []AccountStatsResponseDailyInner, monthly []AccountStatsResponseDailyInner, ) *AccountStatsResponse`

NewAccountStatsResponse instantiates a new AccountStatsResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAccountStatsResponseWithDefaults

`func NewAccountStatsResponseWithDefaults() *AccountStatsResponse`

NewAccountStatsResponseWithDefaults instantiates a new AccountStatsResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTotal

`func (o *AccountStatsResponse) GetTotal() float32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *AccountStatsResponse) GetTotalOk() (*float32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *AccountStatsResponse) SetTotal(v float32)`

SetTotal sets Total field to given value.


### GetDaily

`func (o *AccountStatsResponse) GetDaily() []AccountStatsResponseDailyInner`

GetDaily returns the Daily field if non-nil, zero value otherwise.

### GetDailyOk

`func (o *AccountStatsResponse) GetDailyOk() (*[]AccountStatsResponseDailyInner, bool)`

GetDailyOk returns a tuple with the Daily field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDaily

`func (o *AccountStatsResponse) SetDaily(v []AccountStatsResponseDailyInner)`

SetDaily sets Daily field to given value.


### GetMonthly

`func (o *AccountStatsResponse) GetMonthly() []AccountStatsResponseDailyInner`

GetMonthly returns the Monthly field if non-nil, zero value otherwise.

### GetMonthlyOk

`func (o *AccountStatsResponse) GetMonthlyOk() (*[]AccountStatsResponseDailyInner, bool)`

GetMonthlyOk returns a tuple with the Monthly field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMonthly

`func (o *AccountStatsResponse) SetMonthly(v []AccountStatsResponseDailyInner)`

SetMonthly sets Monthly field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


