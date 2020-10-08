import tkinter as tk 


class SupplierBrandsInfo(object):
    """docstring for SupplierList"""

    def __init__(self, parent_frame, db_brand_price):
        self.__brand_text_frame = tk.Text(parent_frame)
        self.db_brand_price = db_brand_price
        self.place()
        

    def get_brands(self, price_name, combine=False):
        if not combine: self.__brand_text_frame.delete('1.0', tk.END)
        inf_dict = self.db_brand_price.get_brands_info_by_supplier_name('.'.join(price_name.split('.')[1:]).strip())
        self.__brand_text_frame.tag_config('brand', background="yellow")
        for brand in inf_dict:
            for k, v in brand.items():
                self.__brand_text_frame.insert(tk.INSERT, '%s: %s \n' % (k, v), 'brand' if k == 'brand' else None)
            self.__brand_text_frame.insert(tk.INSERT, '\n'+40*'-'+'\n')
        self.__brand_text_frame.lift()


    def place(self):
        self.__brand_text_frame.place(relheight=1, relwidth=1)


    def frame(self):
        return self.__brand_text_frame
