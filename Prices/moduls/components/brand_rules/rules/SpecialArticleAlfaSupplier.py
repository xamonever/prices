from ..basicRule import BasicRule
from .....exceptions import BadLineExeption


class SpecialArticleAlfaSupplierRule(BasicRule):
    """alfa_article_shit"""


    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.param = param.lower()
        self.brandCol = columns.brandCol
        self.articleCol = columns.articleCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        if not str(row[self.articleCol]).startswith("00"):
            row[self.articleCol] = "0 "*int(self.param)+str(row[self.articleCol]).replace(',',' ')
        return row
