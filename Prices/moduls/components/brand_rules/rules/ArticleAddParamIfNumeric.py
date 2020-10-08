from ..basicRule import BasicRule


class ArticleAddParamIfNumericRule(BasicRule):
    """docstring for BasicRule"""
    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        if ',' in param.lower():
            self.param, self.length = param.split(',')
        else:
            self.param = param
            self.length = None
        self.articleCol = columns.articleCol
        self.brandCol = columns.brandCol
    
    def __str__(self):
        return f'For {self.brand} adds {self.param} to article if article is numeric. If length was defined then article would be cut by it({self.length}).'

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        s_art = str(row[self.articleCol]).replace(' ', '')
        try:
            if self.length:
                x = int(s_art[:-int(self.length)])
            else:
                x = int(s_art)
        except ValueError:
            return row
        row[self.articleCol] = self.param + s_art
        return row
