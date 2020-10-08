import tkinter as tk


class SupplierEditor(object):
    """docstring for SupplierList"""

    def __init__(self, parent_frame, db_price):
        self.db_price = db_price
        self.__inputs_frame = tk.Frame(parent_frame, bg='green', bd=2)
        self.place()
        self.frames = self.fill_frame()


    def creating_price(self, price_id):
        for frame in self.frames.keys():
            self.frames[frame].children['!entry'].delete(0, tk.END)
        self.frames['id'].children['!entry'].insert(tk.INSERT, price_id)
        self.frames['processing'].children['!entry'].insert(tk.INSERT, '1')
        self.frames['header_row'].children['!entry'].insert(tk.INSERT, '1')
        self.frames['table_borders'].children['!entry'].insert(tk.INSERT, '1|1_5')
        self.frames['save_formate'].children['!entry'].insert(tk.INSERT, 'xlsx')
        self.__inputs_frame.lift()



    def info_to_frames(self, inf):
        for frame in self.frames.keys():
            self.frames[frame].children['!entry'].delete(0, tk.END)
            self.frames[frame].children['!entry'].insert(tk.INSERT, inf[frame])
        self.__inputs_frame.lift()


    def fill_frame(self):
        frames = dict()
        h = 0
        keys = self.db_price.get_instruction_by_id().keys()
        for key in keys:
            frames[key] = tk.Frame(self.__inputs_frame, bg='green', bd=2)
            frames[key].place(rely=0.05*h, relwidth=1, relheight=0.05)  
            # frames[key].place(rely=h/len(keys), relwidth=1, relheight=0.05)            
            tk.Label(frames[key], text=key).place(relx=0.05, relwidth=0.3, relheight=0.9)            
            entr_el = tk.Entry(frames[key], bd=4)
            entr_el.place(relx=0.4, relwidth=0.59, relheight=1)
            h = h + 1
        return frames


    def place(self):
        self.__inputs_frame.place(relheight=1, relwidth=1)


    def frame(self):
        return self.__inputs_frame
