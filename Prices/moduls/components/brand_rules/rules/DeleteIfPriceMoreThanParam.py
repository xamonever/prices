from ..basicRule import BasicRule
from .....exceptions import BadLineExeption


class DeleteIfPriceMoreThanParamRule(BasicRule):
    """docstring for BasicRule"""

    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.param = float(param)
        self.brandCol = columns.brandCol
        self.priceCol = columns.priceCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand != 'все бренды': return row
        if not str(row[self.priceCol]).strip() or float(str(row[self.priceCol]).strip().replace(',', '.')) > self.param:
            raise BadLineExeption('ignoring big price. Position: %s ' % row)
        return row
