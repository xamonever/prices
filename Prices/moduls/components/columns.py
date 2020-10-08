
class Columns():
    """docstring for Columns"""
    
    def __init__(self, template):
        lst = template.split(',')
        self.articleCol = int(lst[0])
        self.brandCol = int(lst[1])
        self.priceCol = int(lst[2])
        self.codeCol = int(lst[3])
        self.storageCol = lst[4]
        self.commentCol = int(lst[6])
        self.storageColList = self.zzz()


    def __str__(self):
        return ','.join([str(col) for col in (self.articleCol, self.brandCol, self.priceCol, 'x', self.storageColList, 'x', self.commentCol)])


    def art_brand_price(self):
        return (self.articleCol, self.brandCol, self.priceCol)
        

    def zzz(self):
        lst = []
        for line in self.storageCol.split('|'):
            if '_' in line:
                t = [i for i in range(*[int(k) for k in line.split('_')])]
                t.append(t[-1]+1)
                lst.extend(t)
            else:
                lst.append(int(line))
        return lst
