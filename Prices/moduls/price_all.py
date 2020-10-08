import openpyxl, csv, os, re
from . import FileOpener
from .directory_manager import DirectoryManager
from .components import *
from ..exceptions import BadLineExeption, NoFileExeption


class AllLoader(RowTransformator, InitHelper):

    output_wb = None
    O_ws = None
    n_file = 0
    error_in_headers = False

    def __init__(self, file, instruction, brand_instruction_list, OBJ=None):
        self.FM = DirectoryManager(instruction['archive'])
        self.file = self.FM.get_file(file)
        self.mainFO = FileOpener
        self.FO_dict = {'mainsheet':instruction['mainsheet'],'for_import':instruction['for_import'],'encoding':instruction['encoding']}
        self.currentFO = self.mainFO.get_fp(self.file, self.FO_dict)

        headers, order = instruction['table_borders'].split('|')
        self.currentFO.init_attr_by_int_list(self, 'header_rows', headers)
        self.headers_template = instruction['headers_template'].split('|')
        
        self.save_formate = instruction['save_formate']
        self.save_file = '.'.join([str(instruction['id']), instruction['save_name'], instruction['save_formate']])
        
        self.encoding = instruction['encoding']
        self.columns = Columns(instruction['columns_template'])

        self.column_order = self.set_column_order(order)
        self.custom_availability = 5
        self.set_ignored(instruction['delete_list'])
          
        self.additional_files = self.to_file_tuple_list(instruction['additional_files'], self.FM.open_path)
        self.additional_brand = instruction['add_brand'].strip()
        self.additional_helpers = instruction['additional_helper'].split(',')
        
        self.hhh = Headers(self)
        self.dp = DefaultProcess(self)
        self.Rul_Ex = RulesExecutor(brand_instruction_list, self.columns)
        self.helpers = additional_helpers.BaseHelp(self.additional_helpers, self.columns)


    def run(self):
        data_list = list()
        
        self.main_ex(data_list, self.file)
        for file, order_, startrow in self.additional_files:
            print(file)
            if not file: continue
            self.column_order = order_
            self.currentFO = self.mainFO.get_fp(file, self.FO_dict)
            self.main_ex(data_list, file, startrow, addition=True)
        
        data_list = self.helpers.run(data_list)

        self.save_output(data_list)
            
        print('done')        


    def main_ex(self, data_list, file_name, startrow=None, addition=False):
        full_file_name = self.FM.path_for_purpose('open', file_name)
        try:
            input_wb, I_ws = self.currentFO.get_input_data(full_file_name)        
        except:
            raise NoFileExeption(file_name)

        content_start = self.header_rows[-1]+1 if not startrow else int(startrow)

        if not addition:
            content_headers = self.currentFO.get_headers(I_ws, content_start, self.column_order)
            self.error_in_headers = self.hhh.output_headers(I_ws, data_list, content_headers)
            if self.hhh.to_start: content_start = self.header_rows[0]

        content = self.currentFO.get_content(I_ws, content_start, self.column_order)
        for r_idx, row in enumerate(content):            
            try:
                row_vals = self.currentFO.get_row_vals(I_ws, row, self.column_order)
                ordered_row = self.to_order(row_vals)
                branded_row = self.insert_brand(ordered_row)
                decoded_row = self.to_decode(branded_row)
                cleaned_row = self.procedures(decoded_row)

                data_list.append(cleaned_row)
                if len(data_list) > 900000:
                    self.save_output(data_list, overlimit=True)
                    
            except BadLineExeption as e:
                pass
        
        print(r_idx, '->', len(data_list)+self.n_file*900000, end=' | ')
        self.currentFO.close_wb(input_wb)
        self.FM.move_file(file_name)


    def procedures(self, row):
        row = self.dp.safe_vals(row)
        self.dp.check_ignored(row)

        row = self.Rul_Ex.execute_all(row)
        self.dp.check_empty_main_cols(row)
        self.dp.check_zero_price(row)

        row = self.dp.set_price_format(row, self.save_formate=='csv')
        row = self.dp.set_clean_availability(row)
        row = self.dp.set_clean_comment(row)
        return row
    

    def save_output(self, data, close=True, overlimit=False):   
        saver = {'xlsx': self.xlsx_saver, 'csv': self.csv_saver}.get(self.save_formate, 'csv')        
        saver(data, close, overlimit, 'headers_error' if self.error_in_headers else 'save')


    def csv_saver(self, data, close, overlimit, purpose):
        O_ws = None
        output_wb = None
        if overlimit or self.n_file:
            self.n_file += 1
        save_file = self.save_file.replace('.csv', ' '+str(self.n_file)+'.csv') if self.n_file else self.save_file
        
        output_wb = open( self.FM.path_for_purpose(purpose, save_file), 'w', newline='', encoding='cp1251')
        O_ws = csv.writer(output_wb, delimiter=';')
        
        for row in data:
            try:
                O_ws.writerow(row)
            except UnicodeEncodeError:
                pass
        
        output_wb.close()
        data.clear()
    

    def xlsx_saver(self, data, close, overlimitt, purpose):
        O_ws = None
        output_wb = None

        output_wb = openpyxl.Workbook(write_only=True)
        O_ws = output_wb.create_sheet()
        
        for row in data:
            O_ws.append(row)
        
        if close: 
            output_wb.save(self.FM.path_for_purpose(purpose, self.save_file))
            output_wb.close()