from ..basicRule import BasicRule


class ArticleStartsWithParamRule(BasicRule):
    """docstring for BasicRule"""
    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.param = param.lower()
        self.articleCol = columns.articleCol
        self.brandCol = columns.brandCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        if not str(row[self.articleCol]).lower().startswith(self.param):
            row[self.articleCol] = self.param + str(row[self.articleCol])
        return row
