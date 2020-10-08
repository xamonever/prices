from ..basicRule import BasicRule


class PriceMultiplyIfParam1InCol2ByParam3Rule(BasicRule):
    """multiply_price_if_param1_in_col2_by_param3"""


    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.param1, needleCol, self.param3 = param.lower().split(',')
        self.brandCol = columns.brandCol
        self.priceCol = columns.priceCol
        self.needleCol = self.get_col_if_str(columns, needleCol)
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        if self.param1 in str(row[self.needleCol]).lower():
            row[self.priceCol] = float(row[self.priceCol]) * float(self.param3)
        return row
            