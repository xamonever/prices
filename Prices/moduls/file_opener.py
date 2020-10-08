from . import XLSLoader, XLSXLoader, CSVLoader, DBFLoader

class FileOpener():

	fp = {'xls': XLSLoader, 'xlsx': XLSXLoader, 'csv': CSVLoader, 'txt': CSVLoader, 'dbf': DBFLoader}

	def __init__(self, ):
		pass

	@classmethod
	def get_fp_format(cls, file_format):
		return cls.fp.get(file_format.lower(), XLSLoader)

	@classmethod
	def get_fp(cls, file, instruction):
		fp = cls.get_fp_format(file.split('.')[-1])
		return fp(instruction)
