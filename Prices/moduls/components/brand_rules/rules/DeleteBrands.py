from ..basicRule import BasicRule
from .....exceptions import BadLineExeption


class DeleteBrandsRule(BasicRule):
    """delete_brands"""


    def __init__(self, brand, param, columns):
        self.brands = [ _.strip() for _ in brand.lower().split(',')]
        self.brands += [ _.strip() for _ in param.lower().split(',')]
        self.brandCol = columns.brandCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower().strip() in self.brands: 
            raise BadLineExeption('ignoring brand. Position: %s ' % row)
        return row
