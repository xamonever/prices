import re
from ..basicRule import BasicRule
from .....exceptions import BadLineExeption


class SpecialArticleRavenolSupplierRule(BasicRule):
    """ravenol_article_rule"""

    pattern = r'(\d+)[ ]?л'

    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.param = param.lower()
        self.brandCol = columns.brandCol
        self.articleCol = columns.articleCol
        self.commentCol = columns.commentCol
    

    def execute(self, row):
        res = re.search(self.pattern, row[self.commentCol])
        last_part = str(res.groups()[0]).strip() if res else ''
        row[self.articleCol] = str(row[self.articleCol]).strip() + '-' + last_part
        return row