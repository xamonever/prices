import tkinter as tk

class BrandList(object):
    """docstring for SupplierList"""

    def __init__(self, parent_frame, db_price):
        self.db_price = db_price
        self.__brand_list_frame = tk.Listbox(parent_frame)
        self.add_scroll(self.__brand_list_frame)
        self.place()
        self.update_list()


    def add_scroll(self, frame):
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=frame.yview)
        scrollbar.pack(side="right", fill="y")
        frame.config(yscrollcommand=scrollbar.set)


    def place(self):
        self.__brand_list_frame.place(relheight=1, relwidth=1)


    def frame(self):
        return self.__brand_list_frame


    def update_list(self, el=None):
        if el is None:
            for item in self.db_price.get_prices_name():
                self.__brand_list_frame.insert(tk.END, item['sup'])
        else:
            self.__brand_list_frame.delete(el)
            self.__brand_list_frame.insert(el, self.db_price.get_instruction_by_id(el)['sup'])