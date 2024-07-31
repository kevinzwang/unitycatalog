# coding: utf-8

"""
    Unity Catalog API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unitycatalog.models.dependency_list import DependencyList

class TestDependencyList(unittest.TestCase):
    """DependencyList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DependencyList:
        """Test DependencyList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DependencyList`
        """
        model = DependencyList()
        if include_optional:
            return DependencyList(
                dependencies = [
                    unitycatalog.models.dependency.Dependency(
                        table = unitycatalog.models.table_dependency.TableDependency(
                            table_full_name = '', ), 
                        function = unitycatalog.models.function_dependency.FunctionDependency(
                            function_full_name = '', ), )
                    ]
            )
        else:
            return DependencyList(
        )
        """

    def testDependencyList(self):
        """Test DependencyList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
