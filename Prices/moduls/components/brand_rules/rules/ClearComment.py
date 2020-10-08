from ..basicRule import BasicRule


class ClearCommentRule(BasicRule):
    """vesna_zeros_to_code"""


    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.brandCol = columns.brandCol
        self.commentCol = columns.commentCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        row[self.commentCol] = ''
        return row
