from ..basicRule import BasicRule
from .....exceptions import BadLineExeption


class DeleteIfParamInColumnRule(BasicRule):
    """delete_if_in_column"""


    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.params = param.lower().split(',')
        self.brandCol = columns.brandCol
        self.needle_column = self.get_col_if_str(columns, self.params[0])

    def __repr__(self):
        return self.__str__
    
    def __str__(self):
        return f'For ({self.brand}) delete row if ({self.params[1:]}) in column {self.needle_column}(+1 if in excel file)'

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row        
        for val in self.params[1:]:
            text = str(row[self.needle_column])[:70] if len(str(row[self.needle_column])) > 70 else str(row[self.needle_column])
            if val.strip() in text:
                raise BadLineExeption('ignoring bad val in column %d. Position: %s ' % (self.needle_column, row))
        return row
