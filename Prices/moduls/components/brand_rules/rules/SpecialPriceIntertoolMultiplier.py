from ..basicRule import BasicRule


class SpecialPriceIntertoolMultiplierRule(BasicRule):
    """intertool_price_multiplier"""


    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.brandCol = columns.brandCol
        self.priceCol = columns.priceCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand != 'все бренды': return row
        if row[5] != '' and str(row[7]).isdigit():
        	row[self.priceCol] = float(row[5])*float(row[7])
        return row
        