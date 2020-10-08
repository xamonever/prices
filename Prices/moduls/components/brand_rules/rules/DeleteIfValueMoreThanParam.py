from ..basicRule import BasicRule
from .....exceptions import BadLineExeption


class DeleteIfValueMoreThanParamRule(BasicRule):
    """delete_if_value_more_than_param"""

    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.brandCol = columns.brandCol
        self.needleCol, self.param = param.split(',')
        self.param = float(self.param)
        self.needleCol = self.get_col_if_str(columns, self.needleCol)
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand != 'все бренды': return row
        try:
            if float(str(row[self.needleCol]).strip().replace(',', '.')) > self.param:
                raise BadLineExeption('ignoring big price. Position: %s ' % row)
        except ValueError:
            print(row)
            raise ValueError
        return row