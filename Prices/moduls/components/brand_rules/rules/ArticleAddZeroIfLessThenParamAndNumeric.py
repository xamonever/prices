from ..basicRule import BasicRule


class ArticleAddZeroIfLessThenParamAndNumericRule(BasicRule):
    """if_article_not_str_add_zero_if_len_less_then_param"""
    
    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.param = [int(p) for p in param.split(',')]
        self.articleCol = columns.articleCol
        self.brandCol = columns.brandCol
    
    def __str__(self):
        return f'For {self.brand} adds zero if article length less then {self.param[0]} and greater then second parameter (if it was defined)'

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        article_val =  str(row[self.articleCol]).replace(' ', '')
        param_max = self.param[0]
        param_min = self.param[1] if len(self.param) > 1 else 1
        if article_val.isdigit() and len(article_val) < param_max and len(article_val) > param_min:
            row[self.articleCol] = "0 "+article_val
        return row
