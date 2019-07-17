from enum import Enum
from typing import Mapping


class DateHierarchyBuilder:
    """ Understands building hierarchies for date values"""

    class Granularity(Enum):
        SECOND_MINUTE_HOUR_DAY_MONTH_YEAR = "smhdmy"
        MINUTE_HOUR_DAY_MONTH_YEAR = "mhdmy"
        HOUR_DAY_MONTH_YEAR = "hdmy"
        DAY_MONTH_YEAR = "dmy"
        WEEK_MONTH_YEAR = "wmy"
        WEEK_YEAR = "wy"
        MONTH_YEAR = "my"
        WEEKDAY = "wd"
        WEEK = "w"
        QUARTER = "q"
        YEAR = "y"
        DECADE = "d"
        CENTURY = "c"
        MILLENIUM = "m"

    def __init__(self, date_format, *granularities):
        self._date_format = date_format
        self._granularities = granularities

    def _request_payload(self) -> Mapping:
        return {
            "builder": {
                "type": "dateBased",
                "dateFormat": self._date_format,
                "granularities": [granularity.name for granularity  in self._granularities]
            }
        }

