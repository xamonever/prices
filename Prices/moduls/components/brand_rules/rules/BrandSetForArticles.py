from ..basicRule import BasicRule


class BrandSetForArticlesRule(BasicRule):
    """set_brand_to_article"""


    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.params = param.lower().split(',')
        self.brandCol = columns.brandCol
        self.articleCol = columns.articleCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        for pare in self.params:
            article, brand = pare.split('__')
            if str(row[self.articleCol]).lower() == article:
                row[self.brandCol] = brand
                break
        return row
