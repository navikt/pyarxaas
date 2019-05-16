import unittest

from pyarxaas.hierarchy import IntervalHierarchyBuilder


class IntervalHierarchyBuilderTest(unittest.TestCase):

    def test_init(self):
        IntervalHierarchyBuilder()

    def test_add_level(self):
        ib = IntervalHierarchyBuilder()
        ib.level(0).add_group(2, "test_label")
        ib.level(1).add_group(4)

    def test_add_levels_not_availible_raises_exception(self):
        with self.assertRaises(AttributeError):
            ib = IntervalHierarchyBuilder()
            ib.level(1).add_group(2)

        with self.assertRaises(AttributeError):
            ib = IntervalHierarchyBuilder()
            ib.level(0).add_group(2)
            ib.level(2).add_group(1)

    def test__request_payload(self):
        expected = {
            "builder" : {
                "type" : "intervalBased",
                "dataType": "LONG",
                "intervals": [],
                "levels" : [ {
                    "level" : 0,
                    "groups" : [ {
                        "grouping" : 2,
                        "label" : "test_label"
                    } ]
                } ]
            }
        }

        ib = IntervalHierarchyBuilder()
        ib.level(0).add_group(2, "test_label")
        payload = ib._request_payload()
        self.assertEqual(expected, payload)

    def test_intervals_are_unique(self):
        ib = IntervalHierarchyBuilder()
        ib.add_interval(0, 10)
        ib.add_interval(0, 10)
        self.assertEqual(1, len(ib.intervals))

    def test_intervals_order(self):
        ib = IntervalHierarchyBuilder()
        ib.add_interval(0, 10)
        ib.add_interval(10, 20)
        ib.add_interval(20, 30)
        self.assertEqual(10, ib.intervals[0]._to)
        self.assertEqual(20, ib.intervals[1]._to)
        self.assertEqual(30, ib.intervals[2]._to)

    def test_group_building(self):
        ib = IntervalHierarchyBuilder()
        ib.level(0)\
            .add_group(2)\
            .add_group(2)
        ib.level(1)\
            .add_group(2)
        self.assertEqual(2, len(ib.levels[0]._groups))
        self.assertEqual(1, len(ib.levels[1]._groups))

    def test_decimal_interval(self):
        expected = {'builder':
                        {'type': 'intervalBased',
                         'dataType': 'DOUBLE',
                         'intervals':
                             [{'from': 0.0, 'to': 10, 'label': None},
                              {'from': 10, 'to': 20, 'label': None},
                              {'from': 20, 'to': 30, 'label': None}],
                         'levels': []}}

        ib = IntervalHierarchyBuilder()
        ib.add_interval(0.0, 10)
        ib.add_interval(10, 20)
        ib.add_interval(20, 30)
        payload = ib._request_payload()
        self.assertEqual(expected, payload)

    def test_integer_interval(self):
        expected = {'builder':
                        {'type': 'intervalBased',
                         'dataType': 'LONG',
                         'intervals':
                             [{'from': 0.0, 'to': 10, 'label': None},
                              {'from': 10, 'to': 20, 'label': None},
                              {'from': 20, 'to': 30, 'label': None}],
                         'levels': []}}

        ib = IntervalHierarchyBuilder()
        ib.add_interval(0, 10)
        ib.add_interval(10, 20)
        ib.add_interval(20, 30)
        payload = ib._request_payload()
        self.assertEqual(expected, payload)



