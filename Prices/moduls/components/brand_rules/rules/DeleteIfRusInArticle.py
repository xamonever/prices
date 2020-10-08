import re
from ..basicRule import BasicRule
from .....exceptions import BadLineExeption


class DeleteIfRusInArticleRule(BasicRule):
    """delete_if_rus_pattent"""

    rus_pattern = r'[а-яА-Я]+'

    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.brandCol = columns.brandCol
        self.articleCol = columns.articleCol
    
    def __str__(self):
        return f'Delete row if rus symbols in article'

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        if re.search(self.rus_pattern, str(row[self.articleCol])):
            raise BadLineExeption('ignoring rus article. Position: %s ' % row)
        return row
