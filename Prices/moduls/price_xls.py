import xlrd, os

from ..abstruct.abs_price import AbstractPrice
# from .components import *



class XLSLoader(AbstractPrice):
    """docstring for XLSLoader"""

    def __init__(self, instruction, ):
        self.f_format = 'xls'
        self.mainsheet = int(instruction['mainsheet']) if instruction['mainsheet'] else 0
        self.encoding = instruction['encoding']

    
    @staticmethod
    def get_headers(I_ws, content_start, column_order):
        return range(content_start)

    
    @staticmethod
    def get_content(I_ws, content_start, column_order):
        return range(content_start, I_ws.nrows)


    @staticmethod
    def get_row_vals(I_ws, row, column_order):
        return  I_ws.row_values(row)[min(column_order)-1:max(column_order)+1]


    @staticmethod
    def init_attr_by_int_list(obj, attr, instr, delim=','):
        setattr(obj, attr, [int(i)-1 for i in instr.split(delim)])


    def get_input_data(self, file_name):
        input_wb = self.open_wb(file_name)
        I_ws = input_wb.sheet_by_index(self.mainsheet)
        return  (input_wb, I_ws)
        

    def open_wb(self, file_name):
        try:
            wb = xlrd.open_workbook(
                file_name, 
                formatting_info=True, 
                on_demand=True,
                encoding_override=self.encoding)
        except NotImplementedError:            
            wb = xlrd.open_workbook(
                file_name, 
                formatting_info=False, 
                encoding_override=self.encoding)
        return wb

        
    def close_wb(self, book):
        # self.log_file.close()
        book.release_resources()
        del book
