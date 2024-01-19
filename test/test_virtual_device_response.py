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

from openapi_client.models.virtual_device_response import VirtualDeviceResponse

class TestVirtualDeviceResponse(unittest.TestCase):
    """VirtualDeviceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VirtualDeviceResponse:
        """Test VirtualDeviceResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VirtualDeviceResponse`
        """
        model = VirtualDeviceResponse()
        if include_optional:
            return VirtualDeviceResponse(
                data = [
                    openapi_client.models.virtual_device.VirtualDevice(
                        _id = '', 
                        attr_hidden = True, 
                        attr_hidden_id = '', 
                        attr_no_delete = True, 
                        attr_no_edit = True, 
                        height_in_meters = 1.337, 
                        locked = True, 
                        map_id = '', 
                        site_id = '', 
                        type = '', 
                        x = '', 
                        y = '', )
                    ],
                meta = openapi_client.models.meta.Meta(
                    msg = '', 
                    rc = '', )
            )
        else:
            return VirtualDeviceResponse(
        )
        """

    def testVirtualDeviceResponse(self):
        """Test VirtualDeviceResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()