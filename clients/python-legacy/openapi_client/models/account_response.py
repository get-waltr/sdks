# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.42
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


class AccountResponse(object):
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
        'account_id': 'str',
        'name': 'str',
        'created_at': 'float',
        'modified_at': 'float',
        'usage_billing_rate': 'float'
    }

    attribute_map = {
        'account_id': 'accountId',
        'name': 'name',
        'created_at': 'createdAt',
        'modified_at': 'modifiedAt',
        'usage_billing_rate': 'usageBillingRate'
    }

    def __init__(self, account_id=None, name=None, created_at=None, modified_at=None, usage_billing_rate=None, local_vars_configuration=None):  # noqa: E501
        """AccountResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._name = None
        self._created_at = None
        self._modified_at = None
        self._usage_billing_rate = None
        self.discriminator = None

        self.account_id = account_id
        if name is not None:
            self.name = name
        self.created_at = created_at
        self.modified_at = modified_at
        self.usage_billing_rate = usage_billing_rate

    @property
    def account_id(self):
        """Gets the account_id of this AccountResponse.  # noqa: E501


        :return: The account_id of this AccountResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountResponse.


        :param account_id: The account_id of this AccountResponse.  # noqa: E501
        :type account_id: str
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this AccountResponse.  # noqa: E501


        :return: The name of this AccountResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountResponse.


        :param name: The name of this AccountResponse.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this AccountResponse.  # noqa: E501


        :return: The created_at of this AccountResponse.  # noqa: E501
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AccountResponse.


        :param created_at: The created_at of this AccountResponse.  # noqa: E501
        :type created_at: float
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this AccountResponse.  # noqa: E501


        :return: The modified_at of this AccountResponse.  # noqa: E501
        :rtype: float
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this AccountResponse.


        :param modified_at: The modified_at of this AccountResponse.  # noqa: E501
        :type modified_at: float
        """
        if self.local_vars_configuration.client_side_validation and modified_at is None:  # noqa: E501
            raise ValueError("Invalid value for `modified_at`, must not be `None`")  # noqa: E501

        self._modified_at = modified_at

    @property
    def usage_billing_rate(self):
        """Gets the usage_billing_rate of this AccountResponse.  # noqa: E501


        :return: The usage_billing_rate of this AccountResponse.  # noqa: E501
        :rtype: float
        """
        return self._usage_billing_rate

    @usage_billing_rate.setter
    def usage_billing_rate(self, usage_billing_rate):
        """Sets the usage_billing_rate of this AccountResponse.


        :param usage_billing_rate: The usage_billing_rate of this AccountResponse.  # noqa: E501
        :type usage_billing_rate: float
        """
        if self.local_vars_configuration.client_side_validation and usage_billing_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `usage_billing_rate`, must not be `None`")  # noqa: E501

        self._usage_billing_rate = usage_billing_rate

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
        if not isinstance(other, AccountResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountResponse):
            return True

        return self.to_dict() != other.to_dict()