from Models import *

from .abstruct import AbstractFactory
from .moduls import AllLoader
from .exceptions import NoFileExeption


class PriceLoader(AbstractFactory):
    """docstring for PriceLoader"""

    def __init__(self, db_name=None, db_refresh=False, **config):
        self.__file_path = config['file_path']
        self.__config_encoding = config['base_encoding']
        if db_refresh:
            self.__db_loader = SettingsModel(db_name=db_name, new_db=self.get_DB_csv()) 
        else:
            self.__db_loader = SettingsModel(db_name=db_name)
        self.__db_brand_model = BrandRulesModel(db_name=db_name)


    def create_format_loader(self, fileName):
        instruction = self.get_price_instruction(fileName)
        if instruction['processing'] != '1':
            raise NoFileExeption
        brand_instruction_list = self.get_brand_instruction(instruction['sup'])
        print(15*'---', '\n', fileName, '<-- ', instruction['id'], instruction['sup'])
        return AllLoader(fileName, instruction, brand_instruction_list)


    def get_format_price_loader(self, fileName):
        return self.__loader_dict[self.get_fileFormat(fileName)]


    def parse_(self, row):
        return {
            'id':               int(row[0]),
            'sup':              row[1],
            'processing':       row[2],
            'name_template':    row[3],
            'save_formate':     row[4],
            'columns_template': row[5],
            'header_row':       row[6],
            'table_borders':    row[7],
            'headers_template': row[8],
            'save_name':        row[9],
            'additional_files': row[10], # additional files
            'archive':          row[11],
            'for_import':       row[12],
            'delete_list':      row[13],
            'encoding':         row[14],
            'mainsheet':        row[15],
            'add_brand':        row[16],
            'additional_helper':row[17],
        }


    @staticmethod
    def get_fileFormat(fileName):
        return fileName.split('.')[-1]


    def get_DB_csv(self, delim=';'):
        import csv

        db = []
        headerRow = True
        with open(self.__file_path) as cf:
            for row in csv.reader(cf, delimiter=delim):
                if headerRow:
                    headerRow = False
                    continue
                db.append(self.parse_(row))
        return db


    def get_price_instruction(self, fileName):
        for item in self.__db_loader.get_templates():
            if item['name_template'].lower() in fileName.lower():
                return self.__db_loader.get_instruction_by_id(item['id'])
        raise NoFileExeption(fileName)


    def get_brand_instruction(self, priceName):
        brands = self.__db_brand_model.get_funcs_by_price_name(priceName)
        # for brand in brands:
        #     print(brand)
        return brands
