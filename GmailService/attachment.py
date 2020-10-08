import base64
import os

from Models.settingsModel import SettingsModel
from .abs_messege import AbstractMessege


class Attachment(AbstractMessege):
    """docstring for Attachment"""
    __savePATH = '..\\priceProject\\Files\\today_shit'


    def __init__(self, att_inf, att_data, save=True):
        self.__id = att_inf['id']
        self.__fileName = att_inf['fileName']
        self.__size = att_data['size']
        self.refresh_fullname()
        
        model = SettingsModel()
        self.templates = model.get_templates()
        self.att_data = att_data

        # if save: self.__saved = self.download_and_save(att_data['data'])
        # else: self.unidate = self.load_data(att_data['data']) 


    def __str__(self):
        return '%s in directory %s' % (self.__fileName, self.__savePATH) 


    def check_and_save(self):
        for template_name in [temp['name_template'] for temp in self.templates]:
            if template_name.lower() in self.__fileName.lower():
                return self.download_and_save(self.att_data['data'])
                


    def get_id(self, msg: AbstractMessege):
        return {'id': self.__id, 'msg_id': msg.get_id()}


    def get_fileName(self):
        return self.__fileName


    def refresh_fullname(self):
        self.__fullFileName = os.path.join(self.__savePATH, self.__fileName)


    def load_data(self, data):
        return base64.urlsafe_b64decode(data.encode('UTF-8'))


    def save(self, filedata):
        with open(self.__fullFileName, 'wb') as f:
            f.write(filedata)
        return True

    
    def download_and_save(self, data):
        return self.save(self.load_data(data))
