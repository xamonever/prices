import sqlite3
from Configs.staticConfig import StaticConfig 


class BrandRulesModel():

    columns = ['id', 'sup', 'brand', 'function', 'params', 'priority']
    
    def __init__(self, db_name=None):
        """ 
        @new_db = PriceLoader.get_DB_csv()
        """        
        self.db_name = StaticConfig.db_name() if not db_name else db_name


    def setUP(self):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(" DROP TABLE IF EXISTS brand_functions")
        execute_line = """CREATE TABLE IF NOT EXISTS brand_functions(%s INTEGER NOT NULL PRIMARY KEY, %s VARCHAR)""" % (self.columns[0], ' VARCHAR, '.join(self.columns[1:]))
        cursor.execute(execute_line)
                                    
        connection.commit()
        connection.close()


    def add(self, data):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        execute_line = """INSERT INTO brand_functions(%s) VALUES(%s)""" % (', '.join(self.columns), ','.join(['?' for _ in data.values()]))
        params = ([*data.values()])
        cursor.execute(execute_line, params)
                                    
        connection.commit()
        connection.close()


    def get_brands_info_by_supplier_name(self, name):
        return self.fetch_db(r'SELECT * FROM brand_functions WHERE sup = "%s" ORDER BY brand' % name, 'all')


    def get_last_id(self):
        return self.fetch_db('SELECT max(id) as id FROM brand_functions')


    def delete_by_id(self, b_id):
        return self.remove_db('DELETE FROM brand_functions WHERE id = %d' % b_id) if b_id else None 


    def remove_db(self, q):
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            cursor.execute(q)
            connection.commit()
        finally:
            connection.close()


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


    def get_funcs_by_price_name(self, price_name):
        return self.fetch_db('SELECT id, sup, brand, function, params, cast(priority as int) as priority FROM brand_functions WHERE sup = "%s" or sup = "Админ - Пустышка" ORDER BY priority ASC' % price_name.strip(), 'all')


    def get_all(self):
        return self.fetch_db('SELECT * FROM brand_functions', 'all')
