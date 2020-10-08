from ..basicRule import BasicRule
from .....exceptions import BadLineExeption


class SpecialArticleMannRule(BasicRule):
    """docstring for BasicRule"""


    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.params = param.lower().split(',')
        self.brandCol = columns.brandCol
        self.articleCol = columns.articleCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        if row[self.articleCol].isdigit() and int(row[self.articleCol]) > 1000000: 
            raise BadLineExeption('not Mann article. Position: %s ' % row)
        return row
