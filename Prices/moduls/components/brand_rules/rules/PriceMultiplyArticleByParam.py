from ..basicRule import BasicRule


class PriceMultiplyArticleByParamRule(BasicRule):
    """multiply_article_price_by_param"""


    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.params = param.lower().split(',')
        self.brandCol = columns.brandCol
        self.priceCol = columns.priceCol
        self.articleCol = columns.articleCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        for pare in self.params:
            article, param = pare.split('__')
            if article == str(row[self.articleCol]).lower():
                row[self.priceCol] = float(row[self.priceCol]) * float(param)
                break
        return row