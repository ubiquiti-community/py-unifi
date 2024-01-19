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

from openapi_client.models.device_radio_table import DeviceRadioTable

class TestDeviceRadioTable(unittest.TestCase):
    """DeviceRadioTable unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceRadioTable:
        """Test DeviceRadioTable
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceRadioTable`
        """
        model = DeviceRadioTable()
        if include_optional:
            return DeviceRadioTable(
                antenna_gain = 56,
                antenna_id = 56,
                backup_channel = '',
                channel = '',
                channel_optimization_enabled = True,
                hard_noise_floor_enabled = True,
                ht = 56,
                loadbalance_enabled = True,
                maxsta = 56,
                min_rssi = 56,
                min_rssi_enabled = True,
                name = '',
                radio = '',
                radio_identifiers = [
                    openapi_client.models.device_radio_i_dentifiers.DeviceRadioIDentifiers(
                        device_id = '', 
                        radio_name = '', )
                    ],
                sens_level = 56,
                sens_level_enabled = True,
                tx_power = '',
                tx_power_mode = '',
                vwire_enabled = True
            )
        else:
            return DeviceRadioTable(
        )
        """

    def testDeviceRadioTable(self):
        """Test DeviceRadioTable"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()