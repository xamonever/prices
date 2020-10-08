import tkinter as tk 


class SupplierBrandsEditor(object):
    """docstring for SupplierList"""

    def __init__(self, parent_frame, db_brand_price):
        self.db_brand_price = db_brand_price
        self.__brand_inputs_frame = tk.Frame(parent_frame, bg='green', bd=2)
        self.frames = self.fill_frame()
        self.place()


    def new_brand_handler(self, supp_name):
        for frame in self.frames.keys():
            self.frames[frame].children['!entry'].delete(0, tk.END)
        try:
            last = int(self.db_brand_price.get_last_id()['id'])
        except TypeError:
            last = 1
        self.frames['id'].children['!entry'].insert(tk.INSERT, last+1)
        self.frames['sup'].children['!entry'].insert(tk.INSERT, supp_name)
        self.__brand_inputs_frame.lift()
        

    def save(self, data):
        self.db_brand_price.add(data)
        

    def delete(self, brand_id):
        self.db_brand_price.delete_by_id(brand_id)


    def info_to_frames(self, inf):
        for frame in self.frames.keys():
            self.frames[frame].children['!entry'].delete(0, tk.END)
            self.frames[frame].children['!entry'].insert(tk.INSERT, inf[frame])
        self.__inputs_frame.lift()


    def fill_frame(self):
        frames = dict()
        h = 0
        keys = self.db_brand_price.columns
        for key in keys:
            frames[key] = tk.Frame(self.__brand_inputs_frame, bg='green', bd=2)
            frames[key].place(rely=h/len(keys), relwidth=1, relheight=0.05)            
            tk.Label(frames[key], text=key).place(relx=0.05, relwidth=0.3, relheight=0.9)            
            entr_el = tk.Entry(frames[key], bd=4)
            entr_el.place(relx=0.4, relwidth=0.59, relheight=1)
            h = h + 1
        return frames


    def place(self):
        self.__brand_inputs_frame.place(relheight=1, relwidth=1)


    def frame(self):
        return self.__brand_inputs_frame
