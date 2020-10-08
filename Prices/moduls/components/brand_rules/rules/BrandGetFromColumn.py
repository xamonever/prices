from ..basicRule import BasicRule


class BrandGetFromColumnRule(BasicRule):
    """set_brand_from_another_column"""


    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.param = int(param)
        self.brandCol = columns.brandCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        row[self.brandCol] = row[self.param]
        return row
