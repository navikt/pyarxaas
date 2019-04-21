import unittest

from pyaaas.models.hierarchy.order_builder.order_hierarchy_builder import OrderHierarchyBuilder


class OrderHierarchyBuilderTest(unittest.TestCase):

    def test_init(self):
        OrderHierarchyBuilder()

    def test_add_groups(self):
        ob = OrderHierarchyBuilder()
        ob.level(0).add_group(2, "upper-body-clothes")

    def test__request_payload(self):
        expected = {'builder': {'type': 'orderBased', 'levels': [{'level': 0, 'groups': [{'grouping': 2, 'label': 'upper-body-clothes'}]}]}}
        ob = OrderHierarchyBuilder()
        ob.level(0).add_group(2, "upper-body-clothes")
        self.assertEqual(expected, ob._request_payload())