from ..basicRule import BasicRule


class ArticleIfLenLessParam1StartsWithParam2Rule(BasicRule):
    """docstring for BasicRule"""

    rus_pattern = r'[а-яА-Я]+'

    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.params = param.lower().split(',')
        self.articleCol = columns.articleCol
        self.brandCol = columns.brandCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        param1, param2 = self.params
        if len(str(row[self.articleCol])) < int(param1) and not str(row[self.articleCol]).lower().startswith(param2):
            row[self.articleCol] = param2 + str(row[self.articleCol])
        return row