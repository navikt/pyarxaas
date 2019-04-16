import unittest

from pyaaas.models.hierarchy.reduction_hierarchy_builder import RedactionHierarchyBuilder


class RedactionHierarchyBuildTest(unittest.TestCase):

    def test_init(self):
        RedactionHierarchyBuilder(
            " ",
            "*",
            RedactionHierarchyBuilder.Order.RIGHT_TO_LEFT,
            RedactionHierarchyBuilder.Order.LEFT_TO_RIGHT)

    def test_prepare(self):
        redaction_builder = RedactionHierarchyBuilder(
            " ",
            "*",
            RedactionHierarchyBuilder.Order.RIGHT_TO_LEFT,
            RedactionHierarchyBuilder.Order.LEFT_TO_RIGHT)
        redaction_builder.prepare(["1123", "1321", "1234", "1532"])

    def test__request_payload(self):
        expected = {'column': ['1123', '1321', '1234', '1532'],
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
        redaction_builder.prepare(["1123", "1321", "1234", "1532"])
        request_payload = redaction_builder._request_payload()
        self.assertEqual(expected, request_payload)

    def test_redaction_builder_with_zero_params(self):
        expected = {'column': ['1123', '1321', '1234', '1532'],
                    'builder': {'type': 'redactionBased',
                                'paddingCharacter': ' ',
                                'redactionCharacter': '*',
                                'paddingOrder': 'RIGHT_TO_LEFT',
                                'redactionOrder': 'RIGHT_TO_LEFT'}
                    }

        redaction_builder = RedactionHierarchyBuilder()
        redaction_builder.prepare(["1123", "1321", "1234", "1532"])

        request_payload = redaction_builder._request_payload()
        self.assertEqual(expected, request_payload)
