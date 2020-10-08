

class BasicRule(object):
    """docstring for BasicRule"""
    def __init__(self, brand='', param='', columns=None):
        self.brand = brand.lower()
        if columns:
            self.brandCol = columns.brandCol        
    
    
    def execute(self, row):
        return row


    def get_col_if_str(self, columns, param):
        if not param.isdigit():
            return int(getattr(columns, param.replace('col', 'Col')))
        return int(param)-1
