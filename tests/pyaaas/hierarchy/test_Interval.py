import unittest

from pyaaas.hierarchy.interval_builder.interval import Interval


class IntervalTest(unittest.TestCase):

    def test_init(self):
        self.assertIsNotNone(Interval(0, 10))

    def test_equality(self):
        i1 = Interval(0, 10, "child")
        i2 = Interval(0, 10, "child")
        self.assertEqual(i1, i2)

    def test_hash(self):
        i1 = Interval(0, 10, "child")
        i2 = Interval(0, 10, "child")
        test_set = {i1, i2}
        self.assertEqual(1, len(test_set))

