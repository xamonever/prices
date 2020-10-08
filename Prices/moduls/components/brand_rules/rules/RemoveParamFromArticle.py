from ..basicRule import BasicRule


class RemoveParamFromArticleRule(BasicRule):
    """docstring for RemoveParamFromArticleRule"""
    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.param = param.lower()
        self.articleCol = columns.articleCol
        self.brandCol = columns.brandCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        row[self.articleCol] = str(row[self.articleCol]).lower().replace(self.param, '', 1)
        return row
