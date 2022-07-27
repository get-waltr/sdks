# NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
# https://openapi-generator.tech
# Do not edit the class manually.

defmodule .Api.Transactions do
  @moduledoc """
  API calls for all endpoints tagged `Transactions`.
  """

  alias .Connection
  import .RequestBuilder


  @doc """
  Get all Transactions for a Business
  Get all Transactions for a Business

  ## Parameters

  - connection (.Connection): Connection to server
  - opts (KeywordList): [optional] Optional parameters
  ## Returns

  {:ok, .Model.AllTransactionsResponse.t} on success
  {:error, Tesla.Env.t} on failure
  """
  @spec transactions_get(Tesla.Env.client, keyword()) :: {:ok, .Model.AllTransactionsResponse.t} | {:ok, .Model.ErrorResponse.t} | {:error, Tesla.Env.t}
  def transactions_get(connection, _opts \\ []) do
    %{}
    |> method(:get)
    |> url("/transactions")
    |> Enum.into([])
    |> (&Connection.request(connection, &1)).()
    |> evaluate_response([
      { 200, %.Model.AllTransactionsResponse{}},
      { 400, %.Model.ErrorResponse{}},
      { 401, %.Model.ErrorResponse{}},
      { 500, %.Model.ErrorResponse{}}
    ])
  end

  @doc """
  Creates a Transaction for an Business
  Creates a Transaction for an Business

  ## Parameters

  - connection (.Connection): Connection to server
  - post_transaction_request (PostTransactionRequest): 
  - opts (KeywordList): [optional] Optional parameters
  ## Returns

  {:ok, .Model.TransactionResponse.t} on success
  {:error, Tesla.Env.t} on failure
  """
  @spec transactions_post(Tesla.Env.client, .Model.PostTransactionRequest.t, keyword()) :: {:ok, .Model.TransactionResponse.t} | {:ok, .Model.ErrorResponse.t} | {:error, Tesla.Env.t}
  def transactions_post(connection, post_transaction_request, _opts \\ []) do
    %{}
    |> method(:post)
    |> url("/transactions")
    |> add_param(:body, :body, post_transaction_request)
    |> Enum.into([])
    |> (&Connection.request(connection, &1)).()
    |> evaluate_response([
      { 200, %.Model.TransactionResponse{}},
      { 400, %.Model.ErrorResponse{}},
      { 401, %.Model.ErrorResponse{}},
      { 500, %.Model.ErrorResponse{}}
    ])
  end

  @doc """
  Get stats for all Transactions
  Get stats for all Transactions

  ## Parameters

  - connection (.Connection): Connection to server
  - opts (KeywordList): [optional] Optional parameters
  ## Returns

  {:ok, .Model.TransactionStatsResponse.t} on success
  {:error, Tesla.Env.t} on failure
  """
  @spec transactions_stats_get(Tesla.Env.client, keyword()) :: {:ok, .Model.TransactionStatsResponse.t} | {:ok, .Model.ErrorResponse.t} | {:error, Tesla.Env.t}
  def transactions_stats_get(connection, _opts \\ []) do
    %{}
    |> method(:get)
    |> url("/transactions/stats")
    |> Enum.into([])
    |> (&Connection.request(connection, &1)).()
    |> evaluate_response([
      { 200, %.Model.TransactionStatsResponse{}},
      { 400, %.Model.ErrorResponse{}},
      { 500, %.Model.ErrorResponse{}}
    ])
  end

  @doc """
  Delete Transaction for an Business
  Delete Transaction for an Business

  ## Parameters

  - connection (.Connection): Connection to server
  - opts (KeywordList): [optional] Optional parameters
  ## Returns

  {:ok, map()} on success
  {:error, Tesla.Env.t} on failure
  """
  @spec transactions_transaction_id_delete(Tesla.Env.client, keyword()) :: {:ok, Map.t} | {:ok, .Model.ErrorResponse.t} | {:error, Tesla.Env.t}
  def transactions_transaction_id_delete(connection, _opts \\ []) do
    %{}
    |> method(:delete)
    |> url("/transactions/:transactionId")
    |> Enum.into([])
    |> (&Connection.request(connection, &1)).()
    |> evaluate_response([
      { 200, %{}},
      { 400, %.Model.ErrorResponse{}},
      { 401, %.Model.ErrorResponse{}},
      { 403, %.Model.ErrorResponse{}},
      { 404, %.Model.ErrorResponse{}},
      { 500, %.Model.ErrorResponse{}}
    ])
  end

  @doc """
  Get a Transaction for a Business
  Get a Transaction for a Business

  ## Parameters

  - connection (.Connection): Connection to server
  - opts (KeywordList): [optional] Optional parameters
  ## Returns

  {:ok, .Model.TransactionResponse.t} on success
  {:error, Tesla.Env.t} on failure
  """
  @spec transactions_transaction_id_get(Tesla.Env.client, keyword()) :: {:ok, .Model.TransactionResponse.t} | {:ok, .Model.ErrorResponse.t} | {:error, Tesla.Env.t}
  def transactions_transaction_id_get(connection, _opts \\ []) do
    %{}
    |> method(:get)
    |> url("/transactions/:transactionId")
    |> Enum.into([])
    |> (&Connection.request(connection, &1)).()
    |> evaluate_response([
      { 200, %.Model.TransactionResponse{}},
      { 400, %.Model.ErrorResponse{}},
      { 401, %.Model.ErrorResponse{}},
      { 403, %.Model.ErrorResponse{}},
      { 404, %.Model.ErrorResponse{}},
      { 500, %.Model.ErrorResponse{}}
    ])
  end

  @doc """
  Update a Transaction for a Business
  Update a Transaction for a Business

  ## Parameters

  - connection (.Connection): Connection to server
  - patch_transaction_request (PatchTransactionRequest): 
  - opts (KeywordList): [optional] Optional parameters
  ## Returns

  {:ok, .Model.TransactionResponse.t} on success
  {:error, Tesla.Env.t} on failure
  """
  @spec transactions_transaction_id_patch(Tesla.Env.client, .Model.PatchTransactionRequest.t, keyword()) :: {:ok, .Model.TransactionResponse.t} | {:ok, .Model.ErrorResponse.t} | {:error, Tesla.Env.t}
  def transactions_transaction_id_patch(connection, patch_transaction_request, _opts \\ []) do
    %{}
    |> method(:patch)
    |> url("/transactions/:transactionId")
    |> add_param(:body, :body, patch_transaction_request)
    |> Enum.into([])
    |> (&Connection.request(connection, &1)).()
    |> evaluate_response([
      { 200, %.Model.TransactionResponse{}},
      { 400, %.Model.ErrorResponse{}},
      { 401, %.Model.ErrorResponse{}},
      { 403, %.Model.ErrorResponse{}},
      { 404, %.Model.ErrorResponse{}},
      { 500, %.Model.ErrorResponse{}}
    ])
  end
end