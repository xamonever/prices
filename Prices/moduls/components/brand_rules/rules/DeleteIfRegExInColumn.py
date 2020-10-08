import re
from ..basicRule import BasicRule
from .....exceptions import BadLineExeption


class DeleteIfRegExInColumnRule(BasicRule):
    """delete_if_RegEx_in_column"""

    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        needle_column, *RegEx = param.lower().split(',')
        self.needle_column = self.get_col_if_str(columns, needle_column)
        self.RegEx = ','.join(RegEx)
        self.brandCol = columns.brandCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        if re.match(self.RegEx, str(row[self.needle_column])):
            raise BadLineExeption('ignoring bad val in column %s. Position: %s ' % (self.needle_column, row))
        return row
