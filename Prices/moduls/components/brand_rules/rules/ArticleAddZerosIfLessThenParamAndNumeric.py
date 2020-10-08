from ..basicRule import BasicRule


class ArticleAddZerosIfLessThenParamAndNumericRule(BasicRule):
    """docstring for BasicRule"""
    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.param = int(param)
        self.articleCol = columns.articleCol
        self.brandCol = columns.brandCol

    def __str__(self):
        return f'For ({self.brand}) if article is numeric and has length less then {self.param} add zeros to start'

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        article_val = str(row[self.articleCol]).replace(' ', '')
        if article_val.isdigit() and len(article_val) < self.param:
            row[self.articleCol] = (int(self.param) - len(str(row[self.articleCol])))*"0 "+str(row[self.articleCol])
        return row
 