from ..basicRule import BasicRule
from .....exceptions import BadLineExeption


class DeleteIfValueEqualParamRule(BasicRule):
    """delete_if_value_equal_param"""

    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.brandCol = columns.brandCol
        self.needleCol, self.param = param.split(',')
        self.needleCol = self.get_col_if_str(columns, self.needleCol)
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand != 'все бренды': return row
        if row[self.needleCol] and str(row[self.needleCol]).strip() == self.param:
            raise BadLineExeption('ignoring big price. Position: %s ' % row)
        return row
