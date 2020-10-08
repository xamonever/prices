

class RowTransformator():
    """docstring for XLSXLoader"""

    columns = None
    column_order = None

    def __init__(self, ):
        pass
        

    def insert_brand(self, row, ):
        return [*row[:self.columns.brandCol], self.additional_brand, *row[self.columns.brandCol:]] if self.additional_brand else row


    def to_order(self, row):
        ordered_row = []
        for i in self.column_order:
            try:
                if i is not None:
                    ordered_row.append(row[i-min(self.column_order)])
                else:
                    ordered_row.append('')
            except IndexError:
                ordered_row.append('')
        return ordered_row



    def to_decode(self, row):
        return [d.replace('=', '', 1) if isinstance(d, str) else d for d in row]
