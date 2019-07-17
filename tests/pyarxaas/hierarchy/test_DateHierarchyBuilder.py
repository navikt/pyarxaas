import unittest

from pyarxaas.hierarchy import DateHierarchyBuilder


class DateHierarchyBuildTest(unittest.TestCase):

    def test_init(self):
        DateHierarchyBuilder(
            "yyyy-MM-dd HH:mm:SSS",
            DateHierarchyBuilder.Granularity.SECOND_MINUTE_HOUR_DAY_MONTH_YEAR,
            DateHierarchyBuilder.Granularity.MINUTE_HOUR_DAY_MONTH_YEAR)

    def test__request_payload(self):
        expected = {
            "builder" : {
                "type" : "dateBased",
                "dateFormat" : "yyyy-MM-dd HH:mm",
                "granularities" : [ "SECOND_MINUTE_HOUR_DAY_MONTH_YEAR", "MINUTE_HOUR_DAY_MONTH_YEAR", "HOUR_DAY_MONTH_YEAR", "DAY_MONTH_YEAR" ]
            }
        }
        db = DateHierarchyBuilder(
            "yyyy-MM-dd HH:mm",
            DateHierarchyBuilder.Granularity.SECOND_MINUTE_HOUR_DAY_MONTH_YEAR,
            DateHierarchyBuilder.Granularity.MINUTE_HOUR_DAY_MONTH_YEAR,
            DateHierarchyBuilder.Granularity.HOUR_DAY_MONTH_YEAR,
            DateHierarchyBuilder.Granularity.DAY_MONTH_YEAR)
        self.assertEqual(expected, db._request_payload())