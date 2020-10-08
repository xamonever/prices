import csv

from ..abstruct.abs_price import AbstractPrice
# from .components import *



class CSVLoader(AbstractPrice):
    """docstring for CSVLoader"""

    delims = {
        'tab': '\t',
        'coma': ',',
    }

    def __init__(self, instruction, ):
        self.f_format = 'csv'
        self.csv_delimiter = ';' if instruction['for_import'].strip() not in self.delims else self.delims[instruction['for_import'].strip()]
        self.encoding = instruction['encoding']


    @staticmethod
    def get_content(I_ws, content_start, column_order):
        return I_ws[content_start:]


    @staticmethod
    def get_headers(I_ws, content_start, column_order):
        return I_ws[:content_start]


    @staticmethod
    def get_row_vals(I_ws, row, column_order):
        return  row[min(column_order)-1:max(column_order)+1]


    @staticmethod
    def init_attr_by_int_list(obj, attr, instr, delim=','):
        setattr(obj, attr, [int(i)-1 for i in instr.split(delim)])


    def get_input_data(self, file_name):
        return  (None, self.open_wb(file_name))


    def open_wb(self, file_name):
        with open(file_name, encoding=self.encoding, errors = 'ignore') as csvf:
            reader = [line for line in csv.reader(csvf, delimiter=self.csv_delimiter)]
        return reader

    def close_wb(self, book):
        pass

   