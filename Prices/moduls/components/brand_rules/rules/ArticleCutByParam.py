from ..basicRule import BasicRule


class ArticleCutByParamRule(BasicRule):
    """docstring for BasicRule"""


    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.param = param.lower()
        self.articleCol = columns.articleCol
        self.brandCol = columns.brandCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        row[self.articleCol] = str(row[self.articleCol]).split(self.param)[0]
        return row
