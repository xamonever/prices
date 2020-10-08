from ..basicRule import BasicRule


class BrandSetForParamInCommentRule(BasicRule):
    """if_param1_in_comment_set_brand_to_param2"""

    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.params = param.lower().split(',')
        self.brandCol = columns.brandCol
        self.commentCol = columns.commentCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        param1, param2 = self.params
        if param1 in str(row[self.commentCol]).lower():
            row[self.brandCol] = param2
        return row