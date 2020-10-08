import os
from datetime import datetime, date
from os.path import join
from rarfile import RarFile
from zipfile import ZipFile


class DirectoryManager(object):
    """docstring for DirectoryManager"""
    _project_dir = join('Files')

    _open_dir = 'today_shit'
    _move_dir = 'moved'
    _save_dir = 'complited'
    _error_dir = 'error'
    _headers_error_dir = 'headers_error'
    

    def __init__(self, archive_pass):
        self.archive_pass = archive_pass
        self._open_path = join(self._project_dir, self._open_dir)
        current_path = join(self._project_dir, str(date.today()))
        self._move_path = join(current_path, self._move_dir)
        self._save_path = join(current_path, self._save_dir)
        self._error_path = join(current_path, self._error_dir)
        self._headers_error_path = join(current_path, self._headers_error_dir)
        
        self.create_dirs([current_path, self._move_path, self._save_path, self._error_path, self._headers_error_path])


    def create_dirs(self, dir_path_list):
        for path in dir_path_list:
            if not os.path.exists(path):
                os.mkdir(path)


    def path_for_purpose(self, command, file_name):
        return join({'open': self._open_path, 'move':self._move_path, 'save':self._save_path, 'error':self._error_path, 'headers_error':self._headers_error_path}.get(command, ''), file_name)


    @property
    def open_path(self):
        return self._open_path


    @property
    def move_path(self):
        return self._move_path


    @property
    def save_path(self):
        return self._save_path


    def move_file(self, file_name, pre='', command='move'):
        destination = self.path_for_purpose(command, file_name)
        if os.path.exists(destination):
            destination = destination.replace(file_name, ' '.join([datetime.now().strftime("%H.%M"), file_name]))
        os.rename(join(self._open_path, file_name), destination)


    def get_file(self, file_name):
        f_format = file_name.split('.')[-1].lower()
        if f_format == 'rar':
            extracted_file = self.unrar(file_name)
        elif f_format == 'zip':
            extracted_file = self.unzip(file_name)
        else:
            return file_name
        self.move_file(file_name)
        return extracted_file


    def unrar(self, file_name):
        zf = RarFile(join(self.open_path, file_name), 'r')
        to_extract = zf.namelist()[0]
        zf.extract(to_extract, path=self.open_path,)
        return to_extract


    def unzip(self, file_name):
        zf = ZipFile(join(self.open_path, file_name), 'r')
        to_extract = zf.namelist()[0]
        zf.extractall(path=self.open_path, members=[to_extract], pwd=self.archive_pass.encode() if self.archive_pass else None)
        return to_extract