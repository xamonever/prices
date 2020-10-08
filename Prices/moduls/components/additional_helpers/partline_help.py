


class PartlineHelp():

    def __init__(self, columns):
        self.storageColList = columns.storageColList
        self.articleCol = columns.articleCol
        self.brandCol = columns.brandCol


    def execute(self, data_list):
        temp = {}
        to_delete = list()
        res_list = list()
                
        for idr, row in enumerate(data_list):
            if idr in to_delete:
                continue

            art = row[self.articleCol]
            brand = row[self.brandCol]
            
            if brand not in temp:
                temp[brand] = {art: idr}

            elif art not in temp[brand]:
                temp[brand][art] = idr
                
            else:
                for storageCol in self.storageColList:
                    if row[storageCol]: 
                        try:
                            data_list[temp[brand][art]][storageCol] += row[storageCol]
                        except:
                            pass
                to_delete.append(idr)
        
        for idx, row in enumerate(data_list):
            if idx not in to_delete: 
                res_list.append(row)
        print(len(data_list))
        print(len(to_delete))
        print(len(res_list))
        return res_list
