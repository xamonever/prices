from ..basicRule import BasicRule


class SpecialArticleElitSupKHRule(BasicRule):
    """docstring for BasicRule"""


    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.param = int(param)
        self.brandCol = columns.brandCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        if row[self.param].lower().startswith('kh') and not row[self.param].lower().startswith('khd') and not row[self.param].lower().startswith('khr'):
            row[self.brandCol] = 'KLOKKERHOLM'
        return row
