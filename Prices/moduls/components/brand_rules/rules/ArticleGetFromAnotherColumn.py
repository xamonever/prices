from ..basicRule import BasicRule


class ArticleGetFromAnotherColumnRule(BasicRule):
    """set_article_from_another_column"""
    
    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.param = int(param)
        self.articleCol = columns.articleCol
        self.brandCol = columns.brandCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        row[self.articleCol] = str(row[self.param])
        return row
