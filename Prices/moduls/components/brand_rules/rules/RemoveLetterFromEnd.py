from ..basicRule import BasicRule


class RemoveLetterFromEndRule(BasicRule):
    """remove_letter_at_end"""


    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.params = param.lower().split(',')
        self.brandCol = columns.brandCol
        self.articleCol = columns.articleCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        for letter in self.params:
            if str(row[self.articleCol]).lower().endswith(letter):
                row[self.articleCol] = row[self.articleCol][:-1]
                break
        return row
