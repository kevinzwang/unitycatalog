# coding: utf-8

"""
    Unity Catalog API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unitycatalog.models.list_tables_response import ListTablesResponse

class TestListTablesResponse(unittest.TestCase):
    """ListTablesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListTablesResponse:
        """Test ListTablesResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListTablesResponse`
        """
        model = ListTablesResponse()
        if include_optional:
            return ListTablesResponse(
                tables = [
                    unitycatalog.models.table_info.TableInfo(
                        name = '', 
                        catalog_name = '', 
                        schema_name = '', 
                        table_type = 'MANAGED', 
                        data_source_format = 'DELTA', 
                        columns = [
                            unitycatalog.models.column_info.ColumnInfo(
                                name = '', 
                                type_text = '', 
                                type_json = '', 
                                type_name = 'BOOLEAN', 
                                type_precision = 56, 
                                type_scale = 56, 
                                type_interval_type = '', 
                                position = 56, 
                                comment = '', 
                                nullable = True, 
                                partition_index = 56, )
                            ], 
                        storage_location = '', 
                        comment = '', 
                        properties = {
                            'key' : ''
                            }, 
                        created_at = 56, 
                        updated_at = 56, 
                        table_id = '', )
                    ],
                next_page_token = ''
            )
        else:
            return ListTablesResponse(
        )
        """

    def testListTablesResponse(self):
        """Test ListTablesResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
