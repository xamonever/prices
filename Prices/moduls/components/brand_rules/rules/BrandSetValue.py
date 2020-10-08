from ..basicRule import BasicRule


class BrandSetValueRule(BasicRule):
    """set_brand_value"""


    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.param = param.lower()
        self.brandCol = columns.brandCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        row[self.brandCol] = self.param
        return row
