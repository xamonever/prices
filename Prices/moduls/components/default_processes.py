import re
from ...exceptions import BadLineExeption

class DefaultProcess():

    availability_replacement_dict = {'pos':["Есть", "на складе", "в наличии", "Y"], 'neg':["нет", "N", "Под заказ: доставка от 2 дней", "нет в наличии"]}

    article_pattern = r'[/\|+-="\']'
    available_pattern = r'[><+ ]'
    non_pritable_chars = r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]'

    def __init__(self, obj):
        self.columns = obj.columns
        self.custom_availability = obj.custom_availability
        self.ignored = obj.ignored


    @staticmethod
    def clean_price(price):
        if isinstance(price, str):
            try:
                price = float(price.replace(',', '.').replace(' ', ''))
            except:
                price = 0.00
        return price if price is not None else 0.00


    def safe_vals(self, row):
        row = [re.sub(self.non_pritable_chars, '', cell) if isinstance(cell, str) else cell for cell in row]
        return row

    def check_ignored(self, row):
        if self.ignored:
            for article, brand in self.ignored:
                if str(row[self.columns.articleCol]).lower() == article.lower() and str(row[self.columns.brandCol]).lower() == brand.lower():
                    raise BadLineExeption('Ignored item. Position: %s ' % row)


    def check_zero_price(self, row):
        if not self.clean_price(row[self.columns.priceCol]) > 0.0:
            raise BadLineExeption('zero price. Position: %s ' % row)


    def check_empty_main_cols(self, row):
        for col in self.columns.art_brand_price():
            if not str(row[col]).strip():
                raise BadLineExeption('empty value. Position: %s ' % row)

    
    def set_clean_comment(self, row):
        pattern = r'[\n\\=\";\']'
        row[self.columns.commentCol] = re.sub(pattern, '', str(row[self.columns.commentCol]))
        return row


    def set_clean_availability(self, row):
        for storage in self.columns.storageColList:
            for key in self.availability_replacement_dict.keys():
                repl = self.custom_availability if key == 'pos' else "0"
                for words in self.availability_replacement_dict[key]:
                    if isinstance(row[storage], str) and words.lower() in row[storage].lower():
                        row[storage] = str(repl)
                        break

            if isinstance(row[storage], str):
                row[storage] = re.sub(self.available_pattern, '', str(row[storage])).replace(',', '.')
            try:
                row[storage] = int(float(row[storage])) 
            except (TypeError, ValueError):
                row[storage] = 0
            # elif isinstance(row[storage], float):
            #     row[storage] = int(row[storage])
            # elif row[storage] is None:
            #     row[storage] = 0
        return row


    def set_price_format(self, row, csv_=False):
        row[self.columns.priceCol] = round(self.clean_price(row[self.columns.priceCol]), 2)
        if csv_: row[self.columns.priceCol] = str(row[self.columns.priceCol]).replace('.', ',')
        return row


    def set_clean_article(self, row):
        if isinstance(row[self.columns.articleCol], str):
            row[self.columns.articleCol] = re.sub(self.article_pattern, '', str(row[self.columns.articleCol]))
        return row