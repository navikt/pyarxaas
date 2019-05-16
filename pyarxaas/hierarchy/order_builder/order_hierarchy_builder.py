from pyarxaas.hierarchy.grouping_based_hierarchy import GroupingBasedHierarchy


class OrderHierarchyBuilder(GroupingBasedHierarchy):

    def __init__(self):
        super().__init__()

    def _request_payload(self):
        return {
            "builder": {
                "type": "orderBased",
                "levels": [level.payload() for level in self.levels]
            }
        }
