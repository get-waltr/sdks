# PatchBusinessRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BusinessName** | Pointer to **string** | I am curious to see if this works with markdown like this link: [to google](https://www.google.com) | [optional] 

## Methods

### NewPatchBusinessRequest

`func NewPatchBusinessRequest() *PatchBusinessRequest`

NewPatchBusinessRequest instantiates a new PatchBusinessRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPatchBusinessRequestWithDefaults

`func NewPatchBusinessRequestWithDefaults() *PatchBusinessRequest`

NewPatchBusinessRequestWithDefaults instantiates a new PatchBusinessRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBusinessName

`func (o *PatchBusinessRequest) GetBusinessName() string`

GetBusinessName returns the BusinessName field if non-nil, zero value otherwise.

### GetBusinessNameOk

`func (o *PatchBusinessRequest) GetBusinessNameOk() (*string, bool)`

GetBusinessNameOk returns a tuple with the BusinessName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBusinessName

`func (o *PatchBusinessRequest) SetBusinessName(v string)`

SetBusinessName sets BusinessName field to given value.

### HasBusinessName

`func (o *PatchBusinessRequest) HasBusinessName() bool`

HasBusinessName returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


