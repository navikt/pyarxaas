from collections.abc import Mapping
from enum import Enum


class RedactionHierarchyBuilder:
    """
    Understands building redaction based hierarchies
    """

    class Order(Enum):
        LEFT_TO_RIGHT = "LEFT_TO_RIGHT"
        RIGHT_TO_LEFT = "RIGHT_TO_LEFT"

    def __init__(self, padding_char:str = " ",
                 redaction_char: str = "*",
                 padding_order: Order = Order.RIGHT_TO_LEFT,
                 redaction_order: Order = Order.RIGHT_TO_LEFT):
        self._padding_char = padding_char
        self._reduction_char = redaction_char
        self._padding_order = padding_order
        self._redaction_order = redaction_order
        self._column = None

    def prepare(self, column):
        self._column = column

    def _request_payload(self)-> Mapping:
        return {
            "column": self._column,
            "builder": {
                "type": "redactionBased",
                "paddingCharacter": self._padding_char,
                "redactionCharacter": self._reduction_char,
                "paddingOrder": self._padding_order.value,
                "redactionOrder": self._redaction_order.value
            }
        }
