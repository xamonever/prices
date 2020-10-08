import tkinter as tk


class SupplierInfo(object):
    """docstring for SupplierList"""

    def __init__(self, parent_frame):
        self.__text_frame = tk.Text(parent_frame)
        self.place()


    def insert(self, inf_dict, combine=False):
        if not combine: self.__text_frame.delete('1.0', tk.END)
        self.__text_frame.insert(tk.INSERT, '\n\n'.join(['%s:%s' % (k, v) for k, v in inf_dict.items()]))
        self.__text_frame.lift()


    def place(self):
        self.__text_frame.place(relheight=1, relwidth=1)


    def frame(self):
        return self.__text_frame
