import unittest

from pyaaas.hierarchy import RedactionHierarchyBuilder


class RedactionHierarchyBuildTest(unittest.TestCase):

    def test_init(self):
        RedactionHierarchyBuilder(
            " ",
            "*",
            RedactionHierarchyBuilder.Order.RIGHT_TO_LEFT,
            RedactionHierarchyBuilder.Order.LEFT_TO_RIGHT)

    def test__request_payload(self):
        expected = {
                    'builder': {'type': 'redactionBased',
                                'paddingCharacter': ' ',
                                'redactionCharacter': '*',
                                'paddingOrder': 'RIGHT_TO_LEFT',
                                'redactionOrder': 'LEFT_TO_RIGHT'}
                    }
        redaction_builder = RedactionHierarchyBuilder(
            " ",
            "*",
            RedactionHierarchyBuilder.Order.RIGHT_TO_LEFT,
            RedactionHierarchyBuilder.Order.LEFT_TO_RIGHT)
        request_payload = redaction_builder._request_payload()
        self.assertEqual(expected, request_payload)

    def test_redaction_builder_with_zero_params(self):
        expected = {
                    'builder': {'type': 'redactionBased',
                                'paddingCharacter': ' ',
                                'redactionCharacter': '*',
                                'paddingOrder': 'RIGHT_TO_LEFT',
                                'redactionOrder': 'RIGHT_TO_LEFT'}
                    }

        redaction_builder = RedactionHierarchyBuilder()

        request_payload = redaction_builder._request_payload()
        self.assertEqual(expected, request_payload)

    def test_padding_characters_can_only_be_single_char(self):
        with self.assertRaises(AttributeError):
            RedactionHierarchyBuilder(padding_char="ab")

        with self.assertRaises(AttributeError):
            RedactionHierarchyBuilder(redaction_char="ab")

