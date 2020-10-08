from ..basicRule import BasicRule
from .....exceptions import BadLineExeption


class DeleteIfParamInCommentRule(BasicRule):
    """delete_if_in_comment"""


    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.params = param.lower().split(',')
        self.brandCol = columns.brandCol
        self.commentCol = columns.commentCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        for param in self.params:
            comment = str(row[self.commentCol]).lower()[:70] if len(str(row[self.commentCol])) > 70 else str(row[self.commentCol]).lower()
            if param in comment:
                raise BadLineExeption('ignoring sth in comment. Position: %s ' % row)
        return row