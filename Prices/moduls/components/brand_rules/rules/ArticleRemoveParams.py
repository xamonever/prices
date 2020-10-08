from ..basicRule import BasicRule


class ArticleRemoveParamsRule(BasicRule):
    """docstring for BasicRule"""

    rus_pattern = r'[а-яА-Я]+'

    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.params = param.lower().split(',')
        self.articleCol = columns.articleCol
        self.brandCol = columns.brandCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        for param in self.params:
            row[self.articleCol] = str(row[self.articleCol]).lower().replace(param, '', 1)
        return row