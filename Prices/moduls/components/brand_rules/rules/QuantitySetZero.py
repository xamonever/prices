from ..basicRule import BasicRule


class QuantitySetZeroRule(BasicRule):
    """docstring for BasicRule"""


    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.brandCol = columns.brandCol
        self.storageColList = columns.storageColList
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        for storage_kol in self.storageColList:
            row[storage_kol] = 0
        return row