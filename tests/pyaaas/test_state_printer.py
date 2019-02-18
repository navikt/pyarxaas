import unittest
import builtins

import pandas

from pyaaas import state_printer


def mock_print(*args):
    pass


builtins.print = mock_print # mock print function


class StatePrinterTest(unittest.TestCase):

    def setUp(self):
        self.test_df = pandas.DataFrame()
        self.test_name_dataframe_mapping ={"zipcode": pandas.DataFrame()}

    def test_print_mapping__run(self):
        state_printer.print_mapping(self.test_name_dataframe_mapping)

    def test_jupyter_print_mapping(self):
        state_printer.jupyter_print_mapping(self.test_name_dataframe_mapping)


