import unittest

from pyaaas.models.hierarchy.interval_builder.interval_hierarchy_builder import IntervalHierarchyBuilder


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

