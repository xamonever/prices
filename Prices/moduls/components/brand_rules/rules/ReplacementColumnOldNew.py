from ..basicRule import BasicRule


class ReplacementColumnOldNewRule(BasicRule):
    """replacement"""


    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        needle_column, *self.params = param.lower().split(',')
        self.needle_column = self.get_col_if_str(columns, needle_column)
        self.brandCol = columns.brandCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        needle_str, sub_str = self.params
        if needle_str != '':
            row[self.needle_column] = str(row[self.needle_column]).lower().replace(needle_str, sub_str)
        else:
            row[self.needle_column] = sub_str
        return row