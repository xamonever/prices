from ..basicRule import BasicRule


class ArticleGetFromColumn1SplitByParam2TakePart3Rule(BasicRule):
    """set_article_from_split_column1_value_by_param2_and_take_part3"""

    rus_pattern = r'[а-яА-Я]+'

    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        column, self.delim, self.part = param.lower().split(',')
        self.column = self.get_col_if_str(columns, column)
        self.articleCol = columns.articleCol
        self.brandCol = columns.brandCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        row[self.articleCol] = row[self.column].lower().split(self.delim)[int(self.part)]
        return row