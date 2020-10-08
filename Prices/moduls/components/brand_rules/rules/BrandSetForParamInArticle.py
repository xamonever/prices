from ..basicRule import BasicRule


class BrandSetForParamInArticleRule(BasicRule):
    """set_brand_if_param_in_article_mult"""


    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.params = param.lower().split(',')
        self.brandCol = columns.brandCol
        self.articleCol = columns.articleCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        for param in self.params:
            param, brand = param.split('__')
            if param in str(row[self.articleCol]).lower():
                row[self.brandCol] = brand
                break
        return row
