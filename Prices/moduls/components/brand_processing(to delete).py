import re
from ...exceptions import BadLineExeption
from .brand_rules.rulesExecutor import RulesExecutor


class BrandProcess():

    rus_pattern = r'[а-яА-Я]+'

    def __init__(self, obj):
        self.columns = obj.columns
        self.brand_instructions = obj.brand_instructions        
        self.Rul_Ex = RulesExecutor(self.brand_instructions, self.columns)
        print(self.Rul_Ex.rules)


    def get_f(self, f):
        return {
            # 'set_article_begin_with_param':                 self.set_article_begin_with_param,
            # 'set_article_end_with_param':                   self.set_article_end_with_param,
            # 'set_article_not_begin_with_param':             self.set_article_not_begin_with_param,                          # 1парам - префикс
            # 'set_article_from_another_column':              self.set_article_from_another_column,
            # 'if_article_not_str_add_zero_if_len_less_then_param': self.if_article_not_str_add_zero_if_len_less_then_param,
            # 'if_article_not_str_add_zeros_to_start_to_len': self.if_article_not_str_add_zeros_to_start_to_len,              # 1парам - кол-во символов
            # 'if_article_numeric_add_to_start_param':        self.if_article_numeric_add_to_start_param,                     # 1парам - префикс
            # 'if_rus_pattent_in_article_set_article_from_another_column': self.if_rus_pattent_in_article_set_article_from_another_column,
            # 'if_article_len_less_param1_set_article_start_param2': self.if_article_len_less_param1_set_article_start_param2,
            # 'set_article_from_split_column1_value_by_param2_and_take_part3': self.set_article_from_split_column1_value_by_param2_and_take_part3,
            # 'remove_param_from_article':                    self.remove_param_from_article,
            # 'remove_params_from_article':                   self.remove_params_from_article,
            # 'cut_article_value_by_param':                   self.cut_article_value_by_param,
 
            # 'set_brand_value':                              self.set_brand_value, 
            # 'set_brand_from_another_column':                self.set_brand_from_another_column,
            # 'set_brand_to_article':                         self.set_brand_to_article, 
            # 'set_brand_by_start_of_article':                self.set_brand_by_start_of_article,                             # парные параметры с разделителем "__" через запятую(префикс1__бренд1,x2__y2, ..)
            # 'set_brand_if_param_in_article_mult':           self.set_brand_if_param_in_article_mult,                        # парные параметры с разделителем "__" через запятую(парам1__бренд1,x2__y2, ..)
            # 'if_param_in_comment_set_param_as_brand':       self.if_param_in_comment_set_param_as_brand,
            # 'if_param1_in_article_set_brand_to_param2':     self.if_param1_in_article_set_brand_to_param2,                  # 1парам - значение в артикуле, 2парам - какой бренд поставить(через запятую)

            # 'multiply_price_by_param':                      self.multiply_price_by_param,
            # 'multiply_article_price_by_param':              self.multiply_article_price_by_param,

            # 'set_quantity_to_zero':                         self.set_quantity_to_zero,

            # 'delete_if_in_comment':                         self.delete_if_in_comment,
            # 'delete_if_in_column':                          self.delete_if_in_column,                                       # 1парам - номер колонки(с учетом сортировки), 2 - список запрещаемых значений через разделитель "__"
            # 'delete_if_rus_pattent':                        self.delete_if_rus_pattent,
            # 'delete_letter_at_end':                         self.delete_letter_at_end,

            # 'replacement':                                  self.replacement,

            # 'check_article_mann':                           self.check_article_mann,
            # 'alfa_article_shit':                            self.alfa_article_shit,
            # 'elit_article_kh_shit':                         self.elit_article_kh_shit,
        }.get(f, 'error')


    # def check_by_brand(self, row):
    #     row = self.Rul_Ex.execute_all(row)
    #     return row


    # def check_by_brand_old(self, row):
    #     for key in self.brand_instructions:
    #         price_brand = str(row[self.columns.brandCol])
    #         if price_brand.lower() == key.lower() or 'все бренды' == key.lower():
    #             for f, params_line in self.brand_instructions[key]:
    #                 func = self.get_f(f)
    #                 params = params_line.lower().split(',')
    #                 row = func(row, *params)
    #     return row


    # def delete_if_in_column(self, row, *params):
    #     needle_column, *vals_to_delete = params 
    #     for val in vals_to_delete:
    #         if val in str(row[int(needle_column)]):
    #             raise BadLineExeption('ignoring bad val in column %s. Position: %s ' % (needle_column, row))
        # return row


    # def replacement(self, row, param):
    #     needle_column, needle_str, sub_str = param.split('_') 
    #     row[needle_column] = str(row[needle_column]).replace(needle_str, sub_str)
        # return row


    # def set_article_from_split_column1_value_by_param2_and_take_part3(self, row, *params):
    #     column, delim, part = params
    #     row[self.columns.articleCol] = row[int(column)].lower().split(delim)[int(part)]
    #     return row


    # def if_article_len_less_param1_set_article_start_param2(self, row, *params):
    #     param1, param2 = params
    #     if len(str(row[self.columns.articleCol])) < int(param1) and not str(row[self.columns.articleCol]).lower().startswith(param2):
    #         row[self.columns.articleCol] = param2 + str(row[self.columns.articleCol])
    #     return row


    # def set_quantity_to_zero(self, row):
    #     for storage_kol in self.columns.storageColList:
    #         row[storage_kol] = "0"
        # return row


    # def if_rus_pattent_in_article_set_article_from_another_column(self, row, param):
    #     if re.search(self.rus_pattern, str(row[self.columns.articleCol])):
    #         row[self.columns.articleCol] = str(row[param])
    #     return row


    # def set_brand_to_article(self, row, *params):
    #     for pare in params:
    #         article, brand = pare.split('__')
    #         if str(row[self.columns.articleCol]).lower() == article:
    #             row[self.columns.brandCol] = brand
    #             break
    #     return row


    # def multiply_article_price_by_param(self, row, *param):
    #     for pare in params:
    #         article, param = pare.split('__')
    #         if article == str(row[self.columns.articleCol]):
    #             row[self.columns.priceCol] = float(row[self.columns.priceCol]) * float(param)
    #             break
        # return row 


    # def multiply_price_by_param(self, row, param):
    #     row[self.columns.priceCol] = float(row[self.columns.priceCol]) * float(param)
        # return row 


    # def if_article_not_str_add_zero_if_len_less_then_param(self, row, param):
    #     if not row[self.columns.articleCol].isdigit() and len(row[self.columns.articleCol]) == int(param):
    #         row[self.columns.articleCol] = "0 "+str(row[self.columns.articleCol])
        # return row


    # def if_article_not_str_add_zeros_to_start_to_len(self, row, param):
    #     if not row[self.columns.articleCol].isdigit() and len(row[self.columns.articleCol]) < int(param):
    #         row[self.columns.articleCol] = (int(param) - len(row[self.columns.articleCol]))*"0 "+str(row[self.columns.articleCol])
    #     return row


    # def if_param1_in_article_set_brand_to_param2(self, row, *params):
    #     param1, param2 = params
    #     if param1 in str(row[self.columns.articleCol]).lower():
    #         row[self.columns.brandCol] = param2
        # return row


    # def delete_if_rus_pattent(self, row):
    #     if re.search(self.rus_pattern, str(row[self.columns.articleCol])):
    #         raise BadLineExeption('ignoring brand. Position: %s ' % row)
        # return row


    # def delete_if_in_comment(self, row, *params):
    #     for param in params:
    #         if param in row[self.columns.commentCol].lower():
    #             raise BadLineExeption('ignoring brand. Position: %s ' % row)
    #     return row


    # def delete_letter_at_end(self, row, *params):
    #     for letter in params:
    #         if str(row[self.columns.articleCol]).lower().endswith(letter):
    #             row[self.columns.articleCol] = row[self.columns.articleCol][:-1]
    #             break
        # return row


    # def remove_param_from_article(self, row, param):
    #     row[self.columns.articleCol] = str(row[self.columns.articleCol]).lower().replace(param, '', 1)
    #     return row


    # def remove_params_from_article(self, row, *params):
    #     for param in params:
    #         row[self.columns.articleCol] = str(row[self.columns.articleCol]).lower().replace(param, '', 1)
    #     return row


    # def cut_article_value_by_param(self, row, param):
    #     if param in str(row[self.columns.articleCol]):
    #         row[self.columns.articleCol] = str(row[self.columns.articleCol]).split(param)[0]
    #     return row


    # def set_brand_if_param_in_article_mult(self, row, *params):
    #     for param in params:
    #         param, brand = param.split('__')
    #         if param.lower() in str(row[self.columns.articleCol]).lower():
    #             row[self.columns.brandCol] = brand
    #             break
        # return row


    # def set_brand_by_start_of_article(self, row, *params):
    #     for param in params:
    #         prefix, brand = param.split('__')
    #         if str(row[self.columns.articleCol]).lower().startswith(prefix):
    #             row[self.columns.brandCol] = brand
    #             break
        # return row


    # def if_article_numeric_add_to_start_param(self, row, param):
    #     if str(row[self.columns.articleCol]).replace("",'').isdigit():
    #         row[self.columns.articleCol] = param + str(row[self.columns.articleCol])
    #     return row


    def if_param_in_comment_set_param_as_brand(self, row, *params):
        for param in params:
            if '__' in param:
                param, val = param.split('__')
            else:
                val = param
            if param in row[self.columns.commentCol].lower():
                row[self.columns.commenbrandCol] = val
                break
        return row


    # def set_article_not_begin_with_param(self, row, param):
    #     if str(row[self.columns.articleCol]).lower().startswith(param):
    #         row[self.columns.articleCol] = str(row[self.columns.articleCol])[len(param):]
    #     return row


    # def set_article_end_with_param(self, row, param):
    #     if not str(row[self.columns.articleCol]).lower().endswith(param):
    #         row[self.columns.articleCol] = row[self.columns.articleCol] + str(param)
    #     return row


    # def set_article_begin_with_param(self, row, param):
    #     if not str(row[self.columns.articleCol]).lower().startswith(param):
    #         row[self.columns.articleCol] = param + row[self.columns.articleCol]
    #     return row


    # def check_article_mann(self, row):
    #     if row[self.columns.articleCol].isdigit() and int(row[self.columns.articleCol]) > 1000000: 
    #         raise BadLineExeption('not Mann article. Position: %s ' % row)
        # return row


    # def alfa_article_shit(self, row):
    #     if not str(row[self.columns.articleCol]).startswith("00"):
    #         row[self.columns.articleCol] = "0 0"+row[self.columns.articleCol].replace(',','') 
        # return row


    # def delete_row(self, row):
    #     raise BadLineExeption('ignoring brand. Position: %s ' % row)


    # def set_article_from_another_column(self, row, valueCol):
    #     row[self.columns.articleCol] = row[int(valueCol)]
    #     return row


    # def set_brand_from_another_column(self, row, valueCol):
    #     row[self.columns.brandCol] = row[int(valueCol)]
    #     return row


    # def set_brand_value(self, row, value):
    #     row[self.columns.brandCol] = value
    #     return row


    # def elit_article_kh_shit(self, row, param):
    #     if row[int(param)].lower().startswith('kh') and not row[int(param)].lower().startswith('khd') and not row[int(param)].lower().startswith('khr'):
    #         row[self.columns.brandCol] = 'KLOKKERHOLM'
    #     return row



if __name__ == '__main__':
    pass
    # b = BrandProcess()
    # b.check_by_brand()

    # d = {
        # 'lol': 'test,5,7,kw',
        # удаления autoLider, torsion, telega_mill, carsPoland, 911, APM, geona, autoTechnics, unic, intertool, asg

        # 'vitol':'set_brand_to_article,MPH006441 (200)__Stenson,MPH006442 (200)__Stenson,MPH006443 (200)__Stenson,2000008257534__RUGBY,2000008257527__RUGBY', kilometr

        # 'INTERTOOL':'multiply_article_price_by_param,IT-0014__10,IT-0019__10,IT-0024__10,IT-0029__10', intertool

        # 'OEM':'set_brand_from_another_column,11', autoExpert
        # 'OE': 'set_brand_from_another_column,11', autoExpert

        # 'AFTERMARKET':'set_brand_value,Chery',    xpert

        # 'LUK A.S.(INA)':'set_brand_value,Ina',    carsPoland

        # 'f1':'set_brand_value,Fone',              torsion

        # 'BSG':'set_article_begin_with_param,BSG',               drujok
        # 'Alkar':'set_article_not_begin_with_param,al',          drujok

        # 'Китай':'if_param_in_comment_set_param_as_brand,chery,geely,great wall,lifan,zaz,byd', dragonparts

        # 'ag auto parts':'if_article_numeric_add_to_start_param',      autoOil
        # 'bosal':'set_begin_with_not,bos',                             autoOil

        # 'Химия и аксессуары':'set_brand_by_start_of_article,DD__DoneDeal,SP__StepUp,DW__DoneDeal,ER__Energy Release,HG__Hi-Gear,NX__NANOX,SM__SMT2',  alfacars
        # 'Motul':'cut_article_value_by_param,/',                                                                                                       alfacars
        # 'Ajusa':'set_article_not_begin_with_param,aj',                                                                                                alfacars

        # 'knecht':'remove_param_from_article,eco',     motorZona
        # 'mahle':'remove_param_from_article,eco',      motorZona

        # 'bsg':'set_article_begin_with_param,BSG',     ProfiCars
        # 'bta':'set_article_end_with_param,BTA',       ProfiCars

        # 'bosch':'delete_letter_at_end,r,u,p,e',       italAuto
        # 'bsg':'set_article_begin_with_param,BSG',     italAuto

        # 'bosch':'remove_param_from_article,bosch',    asiaChina

        # 'bosch':'delete_letter_at_end,v',             samurai
        # 'bosal':'set_begin_with_not,bos',             samurai

        # 'knecht':'remove_param_from_article,eco',     autoFormat3

        # 'ADG':'if_param1_in_article_set_brand_to_param2,voda,ad',     autoZapas

        # 'bosch':'remove_param_from_article,WYP',                                          intercars
        # 'asmet':'remove_param_from_article,asm',                                          intercars
        # 'WATER TOSOL FLUIDS':'if_param1_in_article_set_brand_to_param2,POLUS,POLUS',      intercars
        # 'WATER TOSOL FLUIDS':'if_param1_in_article_set_brand_to_param2,ADIXOL,ADIXOL',    intercars

        # 'Ajusa':'if_article_not_str_add_zeros_to_start_to_len,8',             japan
        # 'Bosch':'if_article_not_str_add_zeros_to_start_to_len,10',            japan
        # 'Febi':'if_article_not_str_add_zeros_to_start_to_len,5',              japan
        # 'Elring':'remove_param_from_article,el',                              japan
        # 'Elring':'if_article_not_str_add_zeros_to_start_to_len,6',            japan
        # 'DW':'set_brand_by_start_of_article,HG__HiGear',                      japan
        # 'Германия':'set_brand_if_param_in_article,E-Tec__TEC',                japan
        # 'Украина':'set_brand_if_param_in_article,helpix__helpix,advge__Тайга',japan
        # 'BANDO':'remove_param_from_article,ban',                              japan

        # 'Ajusa':'if_article_not_str_add_zeros_to_start_to_len,8',     autoTrade
        # 'Bosch':'if_article_not_str_add_zeros_to_start_to_len,10',    autoTrade
        # 'Bosch':'if_article_not_str_add_zero_if_len_less_then_param,12',              autoTrade
        # 'Febi':'if_article_not_str_add_zeros_to_start_to_len,5',      autoTrade
        # 'mahle':'remove_param_from_article,eco',                      autoTrade

        # 'Химия и аксессуары':'set_brand_by_start_of_article,DD__DoneDeal,SP__StepUp,DW__DoneDeal,ER__Energy Release,HG__Hi-Gear,NX__NANOX,SM__SMT2', #bastion

        # 'febi':'if_article_not_str_add_zeros_to_start_to_len,5',          vesna
        # 'febi bilstein':'if_article_not_str_add_zeros_to_start_to_len,5', vesna
        # 'METALCAUCHO':'if_article_not_str_add_zeros_to_start_to_len,5',   vesna
        # 'MAPA':'if_article_not_str_add_zeros_to_start_to_len,9',          vesna
        # 'BOSCH':'if_article_not_str_add_zeros_to_start_to_len,10',        vesna
        # 'MEYLE':'if_article_not_str_add_zeros_to_start_to_len,10',        vesna
        # 'SASIC':'if_article_not_str_add_zeros_to_start_to_len,7',         vesna
        # '3RG':'set_article_not_begin_with_param,3rg',                     vesna

        # 'bsg':'set_article_begin_with_param,BSG,                          azp
        # 'bsg':'set_article_begin_with_param,BSG,                          cardon

        # 'febi':'if_article_not_str_add_zeros_to_start_to_len,5',          lviv
        # 'febi bilstein':'if_article_not_str_add_zeros_to_start_to_len,5', lviv

        # 'Airtex':'set_article_not_begin_with_param,ai',       alexauto
        # 'bsg':'set_article_begin_with_param,BSG',             alexauto

        # 'Ajusa':'set_article_not_begin_with_param,aju',   busParts
        # 'bosal':'set_article_not_begin_with_param,bos',   busParts
        # 'bsg':'set_article_begin_with_param,BSG',         busParts
        # 'LPR':'set_article_not_begin_with_param,lpr',     busParts

        # 'Exide':'multiply_price_by_param,0.95',   ukrAZ
        # 'ISTA':'multiply_price_by_param,0.95',    ukrAZ
        # 'Plazma':'multiply_price_by_param,0.93',  ukrAZ

        # 'BSG':'set_article_begin_with_param,BSG',                     autoDuma
        # 'AG':'if_article_numeric_add_to_start_param,ag',              autoDuma
        # 'AG autoparts':'if_article_numeric_add_to_start_param,ag',    autoDuma
        # 'AGA':'set_brand_by_start_of_article,DD__DoneDeal,SP__StepUp,DW__DoneDeal,ER__Energy Release,HG__Hi-Gear,NX__NANOX,SM__SMT2',  autoDuma
        # 'mahle':'remove_param_from_article,eco',                      autoDuma
        # 'febi':'if_article_not_str_add_zeros_to_start_to_len,5',      autoDuma
        # 'febi bilstein':'if_article_not_str_add_zeros_to_start_to_len,5',   autoDuma
        # 'ossca':'if_article_not_str_add_zeros_to_start_to_len,5',     autoDuma
        # 'honda':'if_article_not_str_add_zeros_to_start_to_len,10',    autoDuma
        # 'REMSA':'if_article_not_str_add_zeros_to_start_to_len,6',     autoDuma
        # 'FISCHER':'if_article_not_str_add_zeros_to_start_to_len,6',   autoDuma
        # 'templin':'if_article_not_str_add_zeros_to_start_to_len,12',  autoDuma
        # 'SSANGYONG':'if_article_not_str_add_zeros_to_start_to_len,9', autoDuma
        # 'BOSCH':'if_article_not_str_add_zeros_to_start_to_len,10',    autoDuma
        # 'MEYLE':'if_article_not_str_add_zeros_to_start_to_len,10',    autoDuma
        # 'SASIC':'if_article_not_str_add_zeros_to_start_to_len,7',     autoDuma
        # 'MAZDA':'set_brand_by_start_of_article,ad__ad',               autoDuma

        # 'bosal':'set_article_not_begin_with_param,bos',           geona
        # 'asmet':'set_article_not_begin_with_param,asm',           geona
        # 'mann-filter':'check_article_mann',                       geona
        # 'bosch':'remove_param_from_article,wyp',                  geona
        # 'bosch':'remove_param_from_article,uc',                   geona
        # 'bosch':'remove_param_from_article,turk',                 geona
        # 'bosch':'set_article_not_begin_with_param,bo',            geona
        # 'Airtex':'remove_param_from_article,air',                 geona
        # 'Airtex':'remove_param_from_article,5c',                  geona
        # 'Airtex':'remove_param_from_article,aw',                  geona
        # 'Alkar':'remove_param_from_article,al',                   geona
        # 'Alkar':'remove_param_from_article,a',                    geona
        # '3RG':'remove_param_from_article,3rg',                    geona
        # '3RG':'remove_param_from_article,in',                     geona
        # '3RG':'remove_param_from_article,rg',                     geona
        # 'AG':'set_brand_by_start_of_article,ag__ag',              geona
        # 'AG autoparts':'set_brand_by_start_of_article,ag__ag',    geona
        # 'mahle/knecht':'remove_param_from_article,eco',           geona
        # 'mahle':'remove_param_from_article,eco',                  geona
        # 'LEMFORDER':'remove_param_from_article,lmi',              geona
        # 'febi':'if_article_not_str_add_zeros_to_start_to_len,5',  geona
        # 'febi bilstein':'if_article_not_str_add_zeros_to_start_to_len,5',             geona
        # 'bsg':'set_article_not_begin_with_param,bsg',                                 geona
        # 'AGA':'set_brand_by_start_of_article,DD__DoneDeal,SP__StepUp,DW__DoneDeal,ER__Energy Release,HG__Hi-Gear,NX__NANOX,SM__SMT2',         geona
        # 'MAZDA':'set_brand_by_start_of_article,ad__ad',           geona

        # 'BOSCH':'',                                       autoTechnics
        # 'OSRAM':'',                                       autoTechnics
        # 'PHILIPS':'set_article_begin_with_param,ps',      autoTechnics
        # 'FERODO':'remove_param_from_article,-1',          autoTechnics
        # 'Mahle':'remove_param_from_article,eco',          autoTechnics
        # 'KROON OIL':'',                                   autoTechnics
        # 'SPIDAN':'',                                      autoTechnics
        # 'WP':'',                                          autoTechnics
        # 'AJUSA':'',                                       autoTechnics
        # 'XX':'',                                          autoTechnics

        # 'AXXIS  Польша':'set_article_from_another_column,1',                                  omega
        # 'Дорожная карта':'if_rus_pattent_in_article_set_article_from_another_column,2',       omega
        # 'Дорожная карта':'multiply_article_price_by_param,DK480-L14__4,DK480-L19__4',         omega
        # 'KNECHT':'remove_param_from_article,eco',                                             omega
        # 'dongil':'delete_if_in_comment,кор',                                                  omega
        # 'искра':'if_param_in_comment_set_param_as_brand,Tes-Lamps,Диалуч',                    omega
        # 'украина':'set_brand_to_article,4533716__gaz',                                        omega

        # 'KYB':'delete_if_in_comment,Защитный ком,Ремонтный комп,опора амарт,Тарелк,подшипник оп', serviceParts
        # 'KYB':'multiply_price_by_param,0.865',                                                    serviceParts
        # 'CTR':'multiply_price_by_param,0.96',                                                     serviceParts

        # 'Bosal':'set_quantity_to_zero',                                   zipAuto

        # 'Febi':'if_article_not_str_add_zeros_to_start_to_len,5',          unic
        # 'febi bilstein':'if_article_not_str_add_zeros_to_start_to_len,5', unic
        # 'AGA':'set_brand_by_start_of_article,DD__DoneDeal,SP__StepUp,DW__DoneDeal,ER__Energy Release,HG__Hi-Gear,NX__NANOX,SM__SMT2', unic         geona

        # 'ajusa':'set_article_not_begin_with_param,aju',                   venAuto
        # 'Alkar':'set_article_not_begin_with_param,al',                    venAuto
        # 'BANDO':'remove_params_from_article,bando,ban',                   venAuto
        # 'bsg':'remove_param_from_article,bsg',                            venAuto
        # 'bsg':'set_article_begin_with_param,bsg',                         venAuto
        # 'febi':'set_article_not_begin_with_param,fe',                     venAuto
        # 'febi':'if_article_not_str_add_zeros_to_start_to_len,5',          venAuto
        # 'febi bilstein':'set_article_not_begin_with_param,fe',            venAuto
        # 'febi bilstein':'if_article_not_str_add_zeros_to_start_to_len,5', venAuto

        # 'bsg':'remove_param_from_article,bsg',                            masterService

        # 'asmet':'set_article_not_begin_with_param,asm',                   liamotors
        # 'BANDO':'remove_param_from_article,ban',                          liamotors

        # 'COMPLEX':'if_article_len_less_param1_set_article_start_param2,6,cx', mTechno

        # 'bosch':'remove_param_from_article,bosch',                            vlad
        # 'KM GERMANY':'set_article_from_split_column1_value_by_param2_and_take_part3,3,km,-1',  vlad
        # 'SSANGYONG':'if_article_not_str_add_zeros_to_start_to_len,10',        vlad
        # 'BOSCH':'if_article_not_str_add_zeros_to_start_to_len,10',            vlad
        # 'MEYLE':'if_article_not_str_add_zeros_to_start_to_len,10',            vlad
        # 'SASIC':'if_article_not_str_add_zeros_to_start_to_len,7',             vlad
        # 'NGK':'if_article_not_str_add_zeros_to_start_to_len,4',               vlad
        # 'AUTOTECHTILE':'if_article_not_str_add_zeros_to_start_to_len,4',      vlad
        # 'ASAM':'if_article_not_str_add_zeros_to_start_to_len,5',              vlad
        # 'mahle':'remove_param_from_article,eco',                              vlad
        # 'LPR':'set_article_from_another_column,3',                            vlad
        # 'LPR':'set_article_not_begin_with_param,lpr',                         vlad
        # 'AG':'set_article_begin_with_param,ag',                               vlad

        # 'Ajusa':'set_article_not_begin_with_param,u',                         alfa
        # 'Airtex':'set_article_not_begin_with_param,pa',                       alfa
        # 'Airtex':'set_article_not_begin_with_param,air',                      alfa
        # 'Bosch':'if_article_not_str_add_zero_if_len_less_then_param,12',      alfa
        # 'Meyle':'if_article_not_str_add_zero_if_len_less_then_param,12',      alfa
        # 'AutoTechteile':'if_article_not_str_add_zeros_to_start_to_len,4',     alfa
        # 'MAHLE ORIGINAL':'alfa_article_shit',                                 alfa
        # 'Metelli':'alfa_article_shit',                                        alfa
        # 'LPR':'set_article_not_begin_with_param, lpr',                        alfa

        # 'Winso':'set_article_from_another_column,4',                              asg
        # 'FEBI BILSTEIN':'if_article_not_str_add_zeros_to_start_to_len,5',         asg
        # 'Johnson Controls Autobatt':'set_brand_value,varta',                      asg
        # 'Yuasa Battery Europe) Gmb':'set_brand_value,yuasa',                      asg
        # 'ELF':'if_param_in_comment_set_param_as_brand,total',                     asg
        # 'ТОСОЛ-СИНТЕЗ':'if_param_in_comment_set_param_as_brand,felix,ROSDOT',     asg
        # 'lpr':'set_article_not_begin_with_param,lpr',                             asg
        # 'Україна':'if_param_in_comment_set_param_as_brand,solar,Лійка__carlife',  asg

        # 'Тайвань':'if_param_in_comment_set_param_as_brand,Geely,Chery', telega

        # 'Тайвань':'if_param_in_comment_set_param_as_brand,Geely,Chery', autoTrend

        # 'elit':'set_brand_by_start_of_article,UNI VL-__Voin',                 elit
        # 'ALKO':'set_article_from_another_column,0',                           elit
        # 'Alkar':'set_article_not_begin_with_param,al',                        elit
        # 'Alkar':'set_article_not_begin_with_param,a',                         elit
        # 'KLOKKERHOLM':'set_article_not_begin_with_param,kh',                  elit

        # '!Avtohimia':'if_param1_in_article_set_brand_to_param2,VENOL,wd-40',      autoNova
    }