# coding: utf-8

"""
    Unity Catalog API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unitycatalog.models.create_schema import CreateSchema

class TestCreateSchema(unittest.TestCase):
    """CreateSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSchema:
        """Test CreateSchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSchema`
        """
        model = CreateSchema()
        if include_optional:
            return CreateSchema(
                name = '',
                catalog_name = '',
                comment = '',
                properties = {
                    'key' : ''
                    }
            )
        else:
            return CreateSchema(
                name = '',
                catalog_name = '',
        )
        """

    def testCreateSchema(self):
        """Test CreateSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
