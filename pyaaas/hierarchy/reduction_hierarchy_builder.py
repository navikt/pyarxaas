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
        self._assert_padding_is_valid(redaction_char, padding_char)
        self._padding_char = padding_char
        self._reduction_char = redaction_char
        self._padding_order = padding_order
        self._redaction_order = redaction_order

    def _request_payload(self)-> Mapping:
        return {
            "builder": {
                "type": "redactionBased",
                "paddingCharacter": self._padding_char,
                "redactionCharacter": self._reduction_char,
                "paddingOrder": self._padding_order.value,
                "redactionOrder": self._redaction_order.value
            }
        }

    def _assert_padding_is_valid(self, *characters):
        for char in characters:
            if len(char) > 1:
                raise AttributeError(f"characters can only be a single character: len({char}) > 1")
