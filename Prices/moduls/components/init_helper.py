import os

class InitHelper():
    """docstring for XLSXLoader"""
    open_path = None

    def __init__(self, ):
        pass


    def to_file_tuple_list(self, inf, open_path):
        res = []
        if not inf: return ''
        for file in inf.split('|'):
            add_file_name_part, startrow, order = file.split(';')
            add_file_name = self.get_add_file_name(add_file_name_part, open_path)
            column_order = self.set_column_order(order)
            res.append((add_file_name, column_order, startrow,))
        return res


    def get_add_file_name(self, add_file_name_part, open_path):
        for file in os.listdir(open_path):
            if add_file_name_part.lower() in file.lower():
                return file 


    def set_ignored(self, delete_list):
        if delete_list:
            self.ignored = [(pair.split(',')) for pair in delete_list.split(';')]
        else:
            self.ignored = None


    def set_column_order(self, order):
        column_order = None
        if '_' in order:
            column_order = [i for i in range(*[int(k) for k in order.split('_')])]
            column_order.append(int(order.split('_')[-1]))
        elif ',' in order:
            column_order = [int(i) for i in order.split(',')]
        return column_order
