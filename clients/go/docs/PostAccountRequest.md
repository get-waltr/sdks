# PostAccountRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | **string** | This is your own internal account ID. We will index it based upon your business ID. | 
**Name** | Pointer to **string** |  | [optional] 

## Methods

### NewPostAccountRequest

`func NewPostAccountRequest(accountId string, ) *PostAccountRequest`

NewPostAccountRequest instantiates a new PostAccountRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPostAccountRequestWithDefaults

`func NewPostAccountRequestWithDefaults() *PostAccountRequest`

NewPostAccountRequestWithDefaults instantiates a new PostAccountRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAccountId

`func (o *PostAccountRequest) GetAccountId() string`

GetAccountId returns the AccountId field if non-nil, zero value otherwise.

### GetAccountIdOk

`func (o *PostAccountRequest) GetAccountIdOk() (*string, bool)`

GetAccountIdOk returns a tuple with the AccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccountId

`func (o *PostAccountRequest) SetAccountId(v string)`

SetAccountId sets AccountId field to given value.


### GetName

`func (o *PostAccountRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *PostAccountRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *PostAccountRequest) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *PostAccountRequest) HasName() bool`

HasName returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


