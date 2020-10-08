
class BadLineExeption(Exception):
    """docstring for BadLine"""
    def __init__(self, dErrArguments):
        Exception.__init__(self,"Exception was raised because {0}".format(dErrArguments))


class NoFileExeption(Exception):
    """docstring for  NoFile"""
    def __init__(self, dErrArguments):
        Exception.__init__(self,"Exception was raised because no file found with template \"{0}\"".format(dErrArguments))
   