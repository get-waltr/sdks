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


class PatchBusinessRequest(object):
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
        'business_name': 'str'
    }

    attribute_map = {
        'business_name': 'businessName'
    }

    def __init__(self, business_name=None, local_vars_configuration=None):  # noqa: E501
        """PatchBusinessRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._business_name = None
        self.discriminator = None

        if business_name is not None:
            self.business_name = business_name

    @property
    def business_name(self):
        """Gets the business_name of this PatchBusinessRequest.  # noqa: E501

        I am curious to see if this works with markdown like this link: [to google](https://www.google.com)  # noqa: E501

        :return: The business_name of this PatchBusinessRequest.  # noqa: E501
        :rtype: str
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        """Sets the business_name of this PatchBusinessRequest.

        I am curious to see if this works with markdown like this link: [to google](https://www.google.com)  # noqa: E501

        :param business_name: The business_name of this PatchBusinessRequest.  # noqa: E501
        :type business_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                business_name is not None and len(business_name) < 1):
            raise ValueError("Invalid value for `business_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._business_name = business_name

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
        if not isinstance(other, PatchBusinessRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchBusinessRequest):
            return True

        return self.to_dict() != other.to_dict()
