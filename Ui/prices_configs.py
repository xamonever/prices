import tkinter as tk, time

from Models import *
from .frames import *

class UI(object):
    """docstring for UI"""
    HEIGHT = 700
    WIDTH = 1400

    text_frame = None
    supplier_editor = None


    def __init__(self, db_name=None):
        self.root = tk.Tk()
        tk.Canvas(self.root, height=self.HEIGHT, width=self.WIDTH).pack()
        self.db_price = SettingsModel(db_name=db_name)
        db_brand_price = BrandRulesModel(db_name=db_name)

        self.main_frame = tk.Frame(self.root, bg='blue', bd=5)
        self.main_frame.place( relx=0.01, rely=0.1, relheight=0.8, relwidth=0.4)

        self.info_frame = tk.Frame(self.root, bg='red', bd=5)
        self.info_frame.place( relx=0.58, rely=0.1, relheight=0.8, relwidth=0.4)

        self.supplier_editor = SupplierEditor(self.info_frame, self.db_price)
        self.supplier_brand_editor = SupplierBrandsEditor(self.info_frame, db_brand_price)
        self.brand_text_frame = SupplierBrandsInfo(self.info_frame, db_brand_price)
        

    def start_session(self):
        list_frame_c = SupplierList(self.main_frame, self.db_price)
        list_frame = list_frame_c.frame()

        shit_input = tk.Entry(self.root) 
        shit_input.place( relx=0.42, rely=0.05, relwidth=0.15)     

        tk.Button(self.root, text="Добавить прайс", command=lambda: self.add_price(), bg='green', fg='yellow').place( relx=0.42, rely=0.15, relwidth=0.15)
        tk.Button(self.root, text="Удалить прайс", command=lambda: self.delete_price(list_frame), bg='red', fg='yellow').place( relx=0.42, rely=0.2, relwidth=0.15)

        tk.Button(self.root, text="Добавить правило к прайсу", command=lambda: self.add_brand(list_frame), bg='green', fg='yellow').place( relx=0.42, rely=0.3, relwidth=0.15)
        tk.Button(self.root, text="Удалить правило прайса", command=lambda: self.delete_brand_by_id_from_entry(shit_input), bg='red', fg='yellow').place( relx=0.42, rely=0.35, relwidth=0.15)

        tk.Button(self.root, text="Параметры прайса", command=lambda: self.show_editor(list_frame), bg='green', fg='yellow').place( relx=0.42, rely=0.5, relwidth=0.15)
        
        tk.Button(self.root, text="Подробнее", command=lambda: self.more(list_frame), bg='yellow', fg='red').place( relx=0.42, rely=0.6, relwidth=0.15)
        tk.Button(self.root, text="Правила прайса", command=lambda: self.show_brand_editor(list_frame), bg='green', fg='yellow').place( relx=0.42, rely=0.55, relwidth=0.15)
        tk.Button(self.root, text="Выход", command=self.root.destroy).place( relx=0.42, rely=0.8, relwidth=0.15)
        
        self.s = tk.Button(self.root, text="Сохранить", command=lambda: self.save(list_frame_c), bg='green', fg='yellow')
        self.s.place( relx=0.72, rely=0.92, relwidth=0.15)
        self.sb = tk.Button(self.root, text="Сохранить бренд к прайсу", command=lambda: self.save_brand(list_frame_c), bg='green', fg='yellow')
        self.sb.place( relx=0.72, rely=0.92, relwidth=0.15)
        
        return self.run_session()


    def add_price(self):
        inf = self.db_price.get_last_instruction_id()
        price_id = int(inf['id_'])+1 
        self.supplier_editor.creating_price(price_id)
        self.s.lift()


    def add_brand(self, frame):
        select = frame.curselection()[0]
        supp = '.'.join(frame.get(select).split('.')[1:]).strip()
        self.supplier_brand_editor.new_brand_handler(supp)
        self.sb.lift()


    def save_brand(self, frame):
        data = {}
        for k, v in self.supplier_brand_editor.frame().children.items():
            data[v.children['!label'].cget("text")] = v.children['!entry'].get() 
        self.supplier_brand_editor.save(data)
        self.sb.lift()


    def show_brand_editor(self, frame):
        select = frame.curselection()[0]
        price_name = frame.get(select)
        self.brand_text_frame.get_brands(price_name)
        self.sb.lift()


    def delete_brand_by_id_from_entry(self, shit_input):
        brand_id = shit_input.get()
        if brand_id.isdigit():
            self.supplier_brand_editor.delete(int(brand_id))
        shit_input.delete(0, tk.END)


    def delete_price(self, frame):
        select = frame.curselection()[0]
        inf = self.db_price.get_info_by_id(int(frame.get(select).split('.')[0]))

        self.db_price.delete_instruction_by_id(inf['id'])
        # frame.update_list()
        self.s.lift()


    def show_editor(self, frame):
        select = frame.curselection()[0]
        inf = self.db_price.get_info_by_id(int(frame.get(select).split('.')[0]))
        self.supplier_editor.info_to_frames(inf)
        self.s.lift()


    def save(self, frame):
        data = {}
        for k, v in self.supplier_editor.frame().children.items():
            data[v.children['!label'].cget("text")] = v.children['!entry'].get()
        self.db_price.update(data)
        frame.update_list(int(data['id']))
        self.s.lift()


    def more(self, frame):
        select = frame.curselection()[0]
        inf = self.db_price.get_info_by_id(int(frame.get(select).split('.')[0]))
        if self.text_frame is None:
            self.text_frame = SupplierInfo(self.info_frame)
        self.text_frame.insert(inf)
        self.s.lift()


    def run_session(self):
        self.root.mainloop()
