# AllAccountsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Accounts** | [**AllAccountsResponseAccounts**](AllAccountsResponseAccounts.md) |  | 
**Total** | **float32** |  | 

## Methods

### NewAllAccountsResponse

`func NewAllAccountsResponse(accounts AllAccountsResponseAccounts, total float32, ) *AllAccountsResponse`

NewAllAccountsResponse instantiates a new AllAccountsResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAllAccountsResponseWithDefaults

`func NewAllAccountsResponseWithDefaults() *AllAccountsResponse`

NewAllAccountsResponseWithDefaults instantiates a new AllAccountsResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAccounts

`func (o *AllAccountsResponse) GetAccounts() AllAccountsResponseAccounts`

GetAccounts returns the Accounts field if non-nil, zero value otherwise.

### GetAccountsOk

`func (o *AllAccountsResponse) GetAccountsOk() (*AllAccountsResponseAccounts, bool)`

GetAccountsOk returns a tuple with the Accounts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccounts

`func (o *AllAccountsResponse) SetAccounts(v AllAccountsResponseAccounts)`

SetAccounts sets Accounts field to given value.


### GetTotal

`func (o *AllAccountsResponse) GetTotal() float32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *AllAccountsResponse) GetTotalOk() (*float32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *AllAccountsResponse) SetTotal(v float32)`

SetTotal sets Total field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


