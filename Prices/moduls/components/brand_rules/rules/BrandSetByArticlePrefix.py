from ..basicRule import BasicRule


class BrandSetByArticlePrefixRule(BasicRule):
    """set_brand_by_start_of_article"""


    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.params = param.lower().split(',')
        self.brandCol = columns.brandCol
        self.articleCol = columns.articleCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        for param in self.params:
            prefix, brand = param.split('__')
            if str(row[self.articleCol]).lower().startswith(prefix):
                row[self.brandCol] = brand
                break
        return row
