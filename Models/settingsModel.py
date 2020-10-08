import sqlite3
from Configs.staticConfig import StaticConfig 


class SettingsModel():
    
    def __init__(self, db_name=None, new_db=None):
        """ 
        @new_db = PriceLoader.get_DB_csv()
        """

        self.db_name = StaticConfig.db_name() if not db_name else db_name

        if new_db:
            self.refresh_db(new_db)

    def manual_exe(self):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        execute_line = "alter table settings ADD column additional_helper varchar default ''"
        cursor.execute(execute_line)
        connection.commit()
        connection.close()


    def update(self, data):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        execute_line = """INSERT or REPLACE INTO settings(
                                    id, 
                                    sup, 
                                    processing, 
                                    name_template, 
                                    save_formate, 
                                    columns_template, 
                                    header_row, 
                                    table_borders, 
                                    headers_template, 
                                    save_name, 
                                    additional_files,
                                    archive, 
                                    for_import, 
                                    delete_list,
                                    encoding,
                                    mainsheet,
                                    add_brand,
                                    additional_helper) VALUES(%s)""" % ','.join(['?' for _ in data.values()])
        params = ([*data.values()])
        cursor.execute(execute_line, params)

        connection.commit()
        connection.close()


    def get_prices_name(self):
        return self.fetch_db('SELECT id, sup FROM settings', fetch='all')


    def get_info_by_id(self, id_):
        return self.fetch_db(r'SELECT * FROM settings WHERE id = "%d"' % id_)


    def get_info_by_name(self, name):
        return self.fetch_db(r'SELECT * FROM settings WHERE sup = "%s"' % name)


    def get_all_instructions(self):
        return self.fetch_db('SELECT * FROM settings', fetch='all')

    
    def get_templates(self):
        return self.fetch_db('SELECT id, name_template FROM settings WHERE processing = 1', fetch='all')


    def get_instruction_by_id(self, p_id=0):
        return self.fetch_db('SELECT * FROM settings WHERE id = %d' % p_id)


    def get_last_instruction_id(self):
        return self.fetch_db('SELECT max(id) as id_ FROM settings')


    def fetch_db(self, q, fetch='one'):
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(q)
        if fetch == 'one':
            res = dict(cursor.fetchone())
        elif fetch == 'all':
            res = [dict(row) for row in cursor.fetchall()]
        else:
            res = 'error'
        connection.close()
        return res


    def delete_instruction_by_id(self, p_id=0):
        return self.edit_db('DELETE FROM settings WHERE id = %d' % p_id)


    def edit_db(self, q):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(q)
        connection.commit()
        connection.close()

        
    def refresh_db(self, new_db):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()

        cursor.execute(" DROP TABLE IF EXISTS settings")
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS settings (
                    id INTEGER NOT NULL PRIMARY KEY,
                    sup VARCHAR,
                    processing VARCHAR,
                    name_template VARCHAR,
                    save_formate VARCHAR,
                    columns_template VARCHAR,
                    header_row VARCHAR,
                    table_borders VARCHAR,
                    headers_template VARCHAR,
                    save_name VARCHAR,
                    additional_files VARCHAR,
                    archive VARCHAR,
                    for_import VARCHAR,
                    delete_list VARCHAR,
                    encoding VARCHAR,
                    mainsheet VARCHAR,
                    add_brand VARCHAR,
                    additional_helper VARCHAR
                )
            ''')
        
        for item in new_db:
            try:
                cursor.execute("""INSERT INTO settings(
                                    id, 
                                    sup, 
                                    processing, 
                                    name_template, 
                                    save_formate, 
                                    columns_template, 
                                    header_row, 
                                    table_borders, 
                                    headers_template, 
                                    save_name, 
                                    additional_files,
                                    archive, 
                                    for_import, 
                                    delete_list,
                                    encoding,
                                    mainsheet,
                                    add_brand,
                                    additional_helper) VALUES(%s)""" % ','.join(['?' for _ in item.values()]), ([*item.values()]))
            except:
                pass
        connection.commit()
        connection.close()
