import re
from collections import defaultdict


class Headers():

    price_pattern = r'[0-9 ,.]+'
    header_brand = 'Бренд'
    to_start = False

    def __init__(self, obj):
        self.headers_template = obj.headers_template
        self.header_rows = obj.header_rows
        self.additional_brand = obj.additional_brand
        self.column_order = obj.column_order
        self.columns = obj.columns
        self.f_format =  obj.currentFO.f_format
        self.FO =  obj.currentFO


    def to_value(self, row):
        ordered_row = []
        for i in self.column_order:
            try:
                ordered_row.append(row[i-min(self.column_order)] if row[i-min(self.column_order)] is not None else '')
            except IndexError:
                ordered_row.append('')
        return [*ordered_row[:self.columns.brandCol], self.header_brand, *ordered_row[self.columns.brandCol:]] if self.additional_brand else ordered_row


    def print_res(self, template_headers, res):
        for _id in range(len(template_headers)):
            if not res[_id]:
                print(f'Warning: Column {_id} must be like ({template_headers[_id]})')


    def check_headers(self, template_headers, row, res):
        for _id in range(len(template_headers)):
            try:
                if template_headers[_id][0] == '~':
                    row[_id] = template_headers[_id][1:]
                    res[_id] = True
                    continue

                if template_headers[_id].strip().lower() == str(row[_id]).strip().lower():
                    res[_id] = True
            except IndexError:
                pass


    def check_headers_by_items(self, template_headers, row):
        return str(row[self.columns.articleCol]).strip().replace('\n', '') == template_headers[1].strip().replace('\n', '') and \
                str(row[self.columns.brandCol]).strip().replace('\n', '') == template_headers[0].strip().replace('\n', '') and \
                re.match(self.price_pattern, str(row[self.columns.priceCol]))


    def output_headers(self, I_ws, data_list, content):
        check_type, *template_headers = self.headers_template if self.headers_template[-1] else self.headers_template[:-1]
        self.to_start = False if check_type == '1' else True
        return self._output_headers_template(I_ws, data_list, content, template_headers) if check_type == '1' else self._output_headers_item(I_ws, content, template_headers)


    def _output_headers_template(self, I_ws, data_list, content, template_headers):
        res = [False for _ in range(len(template_headers))]

        for _id, _row in enumerate(content):
            if _id < self.header_rows[0]-1:continue
            row = self.FO.get_row_vals(I_ws, _row, self.column_order)
            c_row = self.to_value(row)

            self.check_headers(template_headers, c_row, res)
            data_list.append(c_row)

        self.print_res(template_headers, res) 
        return not min(res)


    def _output_headers_item(self, I_ws, content, template_headers):
        res =  False

        for _id, _row in enumerate(content):
            if _id < self.header_rows[0]-1:continue
            row = self.FO.get_row_vals(I_ws, _row, self.column_order)
            c_row = self.to_value(row)

            res = self.check_headers_by_items(template_headers, c_row)
            if res: break

        return not res