# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class TransactionResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'transaction_id': 'str',
        'account_id': 'str',
        'business_id': 'str',
        'amount': 'float',
        'note': 'str',
        'payment_provider': 'str',
        'payment_id': 'str',
        'created_at': 'float',
        'modified_at': 'float'
    }

    attribute_map = {
        'transaction_id': 'transactionId',
        'account_id': 'accountId',
        'business_id': 'businessId',
        'amount': 'amount',
        'note': 'note',
        'payment_provider': 'paymentProvider',
        'payment_id': 'paymentId',
        'created_at': 'createdAt',
        'modified_at': 'modifiedAt'
    }

    def __init__(self, transaction_id=None, account_id=None, business_id=None, amount=None, note=None, payment_provider=None, payment_id=None, created_at=None, modified_at=None, local_vars_configuration=None):  # noqa: E501
        """TransactionResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._transaction_id = None
        self._account_id = None
        self._business_id = None
        self._amount = None
        self._note = None
        self._payment_provider = None
        self._payment_id = None
        self._created_at = None
        self._modified_at = None
        self.discriminator = None

        self.transaction_id = transaction_id
        self.account_id = account_id
        self.business_id = business_id
        self.amount = amount
        if note is not None:
            self.note = note
        if payment_provider is not None:
            self.payment_provider = payment_provider
        if payment_id is not None:
            self.payment_id = payment_id
        self.created_at = created_at
        self.modified_at = modified_at

    @property
    def transaction_id(self):
        """Gets the transaction_id of this TransactionResponse.  # noqa: E501


        :return: The transaction_id of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this TransactionResponse.


        :param transaction_id: The transaction_id of this TransactionResponse.  # noqa: E501
        :type transaction_id: str
        """
        if self.local_vars_configuration.client_side_validation and transaction_id is None:  # noqa: E501
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")  # noqa: E501

        self._transaction_id = transaction_id

    @property
    def account_id(self):
        """Gets the account_id of this TransactionResponse.  # noqa: E501


        :return: The account_id of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this TransactionResponse.


        :param account_id: The account_id of this TransactionResponse.  # noqa: E501
        :type account_id: str
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def business_id(self):
        """Gets the business_id of this TransactionResponse.  # noqa: E501


        :return: The business_id of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        """Sets the business_id of this TransactionResponse.


        :param business_id: The business_id of this TransactionResponse.  # noqa: E501
        :type business_id: str
        """
        if self.local_vars_configuration.client_side_validation and business_id is None:  # noqa: E501
            raise ValueError("Invalid value for `business_id`, must not be `None`")  # noqa: E501

        self._business_id = business_id

    @property
    def amount(self):
        """Gets the amount of this TransactionResponse.  # noqa: E501


        :return: The amount of this TransactionResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TransactionResponse.


        :param amount: The amount of this TransactionResponse.  # noqa: E501
        :type amount: float
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def note(self):
        """Gets the note of this TransactionResponse.  # noqa: E501


        :return: The note of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this TransactionResponse.


        :param note: The note of this TransactionResponse.  # noqa: E501
        :type note: str
        """

        self._note = note

    @property
    def payment_provider(self):
        """Gets the payment_provider of this TransactionResponse.  # noqa: E501


        :return: The payment_provider of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_provider

    @payment_provider.setter
    def payment_provider(self, payment_provider):
        """Sets the payment_provider of this TransactionResponse.


        :param payment_provider: The payment_provider of this TransactionResponse.  # noqa: E501
        :type payment_provider: str
        """
        allowed_values = ["stripe"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and payment_provider not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `payment_provider` ({0}), must be one of {1}"  # noqa: E501
                .format(payment_provider, allowed_values)
            )

        self._payment_provider = payment_provider

    @property
    def payment_id(self):
        """Gets the payment_id of this TransactionResponse.  # noqa: E501


        :return: The payment_id of this TransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this TransactionResponse.


        :param payment_id: The payment_id of this TransactionResponse.  # noqa: E501
        :type payment_id: str
        """

        self._payment_id = payment_id

    @property
    def created_at(self):
        """Gets the created_at of this TransactionResponse.  # noqa: E501


        :return: The created_at of this TransactionResponse.  # noqa: E501
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TransactionResponse.


        :param created_at: The created_at of this TransactionResponse.  # noqa: E501
        :type created_at: float
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this TransactionResponse.  # noqa: E501


        :return: The modified_at of this TransactionResponse.  # noqa: E501
        :rtype: float
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this TransactionResponse.


        :param modified_at: The modified_at of this TransactionResponse.  # noqa: E501
        :type modified_at: float
        """
        if self.local_vars_configuration.client_side_validation and modified_at is None:  # noqa: E501
            raise ValueError("Invalid value for `modified_at`, must not be `None`")  # noqa: E501

        self._modified_at = modified_at

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TransactionResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionResponse):
            return True

        return self.to_dict() != other.to_dict()
