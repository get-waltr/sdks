# NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
# https://openapi-generator.tech
# Do not edit the class manually.

defmodule .Model.BusinessSettingsResponse do
  @moduledoc """
  
  """

  @derive [Poison.Encoder]
  defstruct [
    :businessId,
    :currencyLabel,
    :currencyLabelSuffixed,
    :accountsOverdraftable
  ]

  @type t :: %__MODULE__{
    :businessId => String.t,
    :currencyLabel => String.t,
    :currencyLabelSuffixed => boolean(),
    :accountsOverdraftable => boolean()
  }
end

defimpl Poison.Decoder, for: .Model.BusinessSettingsResponse do
  def decode(value, _options) do
    value
  end
end
