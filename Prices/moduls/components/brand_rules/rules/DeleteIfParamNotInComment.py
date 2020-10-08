from ..basicRule import BasicRule
from .....exceptions import BadLineExeption


class DeleteIfParamNotInCommentRule(BasicRule):
    """delete_if_not_in_comment"""


    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.params = param.lower().split(',')
        self.brandCol = columns.brandCol
        self.commentCol = columns.commentCol
    
    def __str__(self):
        return f'For {self.brand} deletes row if {self.params} not in comment'

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        for param in self.params:
            comment = str(row[self.commentCol]).lower()
            if param not in comment:
                raise BadLineExeption('ignoring sth in comment. Position: %s ' % row)
        return row