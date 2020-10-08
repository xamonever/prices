import re
from ..basicRule import BasicRule


class ArticleIfRusGetFromAnotherColumnRule(BasicRule):
    """if_rus_pattent_in_article_set_article_from_another_column"""

    rus_pattern = r'^.*[а-яА-Я]+'

    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.param = int(param)
        self.articleCol = columns.articleCol
        self.brandCol = columns.brandCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        if re.match(self.rus_pattern, str(row[self.articleCol])):
            row[self.articleCol] = str(row[self.param])
        return row