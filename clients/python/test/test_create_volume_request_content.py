# coding: utf-8

"""
    Unity Catalog API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unitycatalog.models.create_volume_request_content import CreateVolumeRequestContent

class TestCreateVolumeRequestContent(unittest.TestCase):
    """CreateVolumeRequestContent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateVolumeRequestContent:
        """Test CreateVolumeRequestContent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateVolumeRequestContent`
        """
        model = CreateVolumeRequestContent()
        if include_optional:
            return CreateVolumeRequestContent(
                catalog_name = '',
                schema_name = '',
                name = '',
                volume_type = 'MANAGED',
                comment = '0',
                storage_location = ''
            )
        else:
            return CreateVolumeRequestContent(
                catalog_name = '',
                schema_name = '',
                name = '',
                volume_type = 'MANAGED',
                storage_location = '',
        )
        """

    def testCreateVolumeRequestContent(self):
        """Test CreateVolumeRequestContent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
