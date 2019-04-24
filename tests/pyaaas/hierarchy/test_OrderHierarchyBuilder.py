import unittest

from pyaaas.hierarchy import OrderHierarchyBuilder


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

    def test_adding_same_group_twice_is_not_possible(self):
        ob = OrderHierarchyBuilder()
        ob.level(0).add_group(2, "lower-body-clothes")
        ob.level(0).add_group(2, "upper-body-clothes")
        ob.level(0).add_group(2, "lower-body-clothes")
        self.assertEqual(2, len(ob.level(0)._groups))
