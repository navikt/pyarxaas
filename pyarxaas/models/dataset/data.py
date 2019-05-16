import pandas


class Data:
    """
    Represents a collection of dataset rows
    """

    def __init__(self, headers, rows):
        self._headers = headers
        self._rows = rows

    @property
    def payload(self):
        return [self._headers] + self._rows

    @property
    def dataframe(self):
        return pandas.DataFrame(self._rows, columns=self._headers)

    def describe(self, indent):
        print("data:")
        print(self._describe_data_headers(indent))
        print("rows:")
        print(self._describe_data_rows(indent))

    def _describe_data_headers(self, indent):
        string = " "*indent + "headers:\n"
        string += " " * indent*2 + str(self._headers)
        return string

    def _describe_data_rows(self, indent):
        indent = indent*2
        max_rows_to_print = 5
        rows_to_print = min(max_rows_to_print, (len(self._rows)))
        max_columns_to_print = 8
        string = ""
        for row in self._rows[0: rows_to_print]:
            if len(row) > max_columns_to_print:
                columns_to_print_mid = max_columns_to_print // 2
                print_row = row[:columns_to_print_mid]
                print_row.append("...")
                print_row += row[-columns_to_print_mid:]
                row = print_row
            string += " "*indent +\
                      str(row) +\
                      "\n"
        if len(self._rows) > max_rows_to_print:
            string += " "*indent + str("...")
        return string

    def __hash__(self):
        d_hash = hash("")
        for header in self._headers:
            d_hash = hash(d_hash + hash(header))
        for row in self._rows:
            for cell in row:
                d_hash = hash(d_hash + hash(cell))
        return d_hash
