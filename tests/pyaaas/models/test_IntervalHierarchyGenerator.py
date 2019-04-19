import unittest

from models.hierarchy.interval_hierarchy_builder import IntervalHierarchyGenerator


class IntervalHierarchyGeneratorTest(unittest.TestCase):

    def test_init(self):
        IntervalHierarchyGenerator()

    def test_add_level(self):
        ib = IntervalHierarchyGenerator()
        ib.level(0).add_group(2, "test_label")
        ib.level(1).add_group(4)

    def test_add_levels_not_availible_raises_exception(self):
        with self.assertRaises(AttributeError):
            ib = IntervalHierarchyGenerator()
            ib.level(1).add_group(2)

        with self.assertRaises(AttributeError):
            ib = IntervalHierarchyGenerator()
            ib.level(0).add_group(2)
            ib.level(2).add_group(1)

    def test__request_payload(self):
        expected = {
            "column" : [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ],
            "builder" : {
                "type" : "intervalBased",
                "levels" : [ {
                    "level" : 0,
                    "groups" : [ {
                        "grouping" : 2,
                        "label" : "test_label"
                    } ]
                } ]
            }
        }

        ib = IntervalHierarchyGenerator()
        ib.level(0).add_group(2, "test_label")
        ib.prepare([ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ])
        payload = ib._request_payload()
        self.assertEqual(expected, payload)

