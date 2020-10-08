from ..basicRule import BasicRule


class VesnaZerosToCodeRule(BasicRule):
    """vesna_zeros_to_code"""


    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.param = int(param)
        self.codeCol = columns.codeCol
        self.brandCol = columns.brandCol


    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand != 'все бренды': return row
        code_val = str(row[self.codeCol])
        if code_val.isdigit() and len(code_val) < self.param:
            row[self.codeCol] = (int(self.param) - len(row[self.codeCol]))*"0 "+str(row[self.codeCol])
        return row
