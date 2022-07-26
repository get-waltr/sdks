# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.account_response import AccountResponse  # noqa: E501
from openapi_client.rest import ApiException

class TestAccountResponse(unittest.TestCase):
    """AccountResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AccountResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.account_response.AccountResponse()  # noqa: E501
        if include_optional :
            return AccountResponse(
                business_id = '', 
                account_id = '', 
                account_name = '', 
                created_at = 1.337, 
                modified_at = 1.337, 
                balance = 1.337, 
                usage_billing_rate = 1.337, 
                remaining_hours_on_balance = 1.337
            )
        else :
            return AccountResponse(
                business_id = '',
                account_id = '',
                created_at = 1.337,
                modified_at = 1.337,
                balance = 1.337,
                usage_billing_rate = 1.337,
        )

    def testAccountResponse(self):
        """Test AccountResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
