# coding: utf-8

"""
    Unifi API

    Unifi Controller API

    The version of the OpenAPI document: 8.0.26
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from unifi_client.models.user_group_response import UserGroupResponse

class TestUserGroupResponse(unittest.TestCase):
    """UserGroupResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserGroupResponse:
        """Test UserGroupResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserGroupResponse`
        """
        model = UserGroupResponse()
        if include_optional:
            return UserGroupResponse(
                data = [
                    unifi_client.models.user_group.UserGroup(
                        _id = '', 
                        attr_hidden = True, 
                        attr_hidden_id = '', 
                        attr_no_delete = True, 
                        attr_no_edit = True, 
                        name = '', 
                        qos_rate_max_down = 56, 
                        qos_rate_max_up = 56, 
                        site_id = '', )
                    ],
                meta = unifi_client.models.meta.Meta(
                    msg = '', 
                    rc = '', )
            )
        else:
            return UserGroupResponse(
        )
        """

    def testUserGroupResponse(self):
        """Test UserGroupResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
