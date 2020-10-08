from ..basicRule import BasicRule


class StoragePartitionByNameRule(BasicRule):
    """storage_partition_by_names
    
    source_storage_col, source_storage_names_col, remove_names_col, *(storage_name__storage_col)
    
    """

    storages_cols = dict()

    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        source_storage_col, source_storage_names_col, remove_names_col, *params = param.lower().split(',')
        self.source_storage_col = int(source_storage_col) - 1
        self.source_storage_names_col = int(source_storage_names_col) - 1
        self.remove_names_col = int(remove_names_col)
        for param in params:
            if not param: continue
            storage_name, storage_col = param.split('__') 
            self.storages_cols[storage_name.lower().strip()] = int(storage_col) - 1
    

    def execute(self, row):
        cur_storage_name = row[self.source_storage_names_col].lower() if row[self.source_storage_names_col] is not None else '' 
        if cur_storage_name in self.storages_cols and self.storages_cols[cur_storage_name] != self.source_storage_col:
            row[self.storages_cols[cur_storage_name]] = row[self.source_storage_col]
            row[self.source_storage_col] = 0
        if self.remove_names_col == 1:
            row = row[:self.source_storage_names_col]+row[self.source_storage_names_col+1:]
        return row
