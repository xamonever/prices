from ..basicRule import BasicRule


class UnicMonroeCommenReplacementRule(BasicRule):
    """unic_monroe_comment_replacement"""

    monroe_list = ["(к-т 2 шт)", "(к-т 2шт)", "(2шт)", "(комплект из 2 шт левый и правый)", "упаковка 2 шт, ", "(к-кт 2 шт.)", "к-т 2шт.л/пр.", "(минимум 2шт)", 
        "упак. 2шт.", "заказывать 2шт./", "к-т 2шт.л пр.", "заказывать 2шт.", "к-т 2шт .", "к-т 2шт.", "в коробке 2шт., ", "2шт.", "2шт", "в наличии", "2 шт"]

    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.brandCol = columns.brandCol
        self.commentCol = columns.commentCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        for needle_str in self.monroe_list:
            row[self.commentCol] = str(row[self.commentCol]).lower().replace(needle_str, '')
        return row
