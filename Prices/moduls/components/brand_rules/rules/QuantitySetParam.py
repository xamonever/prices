from ..basicRule import BasicRule


class QuantitySetParamRule(BasicRule):
    """set_quantity_to_param"""


    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.param = int(param)
        self.brandCol = columns.brandCol
        self.storageColList = columns.storageColList

    def __repr__(self):
        return self.__str__
    
    def __str__(self):
        return f'For ({self.brand}) set quantity {self.param}'

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        for storage_kol in self.storageColList:
            row[storage_kol] = self.param
        return row