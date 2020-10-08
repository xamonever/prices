from ..basicRule import BasicRule


class PriceMultiplyByParamRule(BasicRule):
    """multiply_price_by_param"""


    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.param = float(param)
        self.brandCol = columns.brandCol
        self.priceCol = columns.priceCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        try:
            price = float(row[self.priceCol]) if row[self.priceCol] else 0.0
            row[self.priceCol] = price * self.param
            return row
        except ValueError:
            return row