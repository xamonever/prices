from .brand_rules.rules import *


class RulesExecutor(object):
    """docstring for RulesExecutor"""


    def __init__(self, rule_list, columns):
        self.__rules = []
        for another_rule in rule_list:
            rule = self.get_rule(another_rule['function'])
            if rule:
                self.__rules.append(rule(brand=another_rule['brand'], param=another_rule['params'], columns=columns))
        # for r in self.__rules:
        #     print(r)


    def get_rule(self, f):
        return {
            'set_article_begin_with_param':                         ArticleStartsWithParamRule,
            'set_article_not_begin_with_param':                     ArticleNotStartsWithParamRule,  
            'set_article_end_with_param':                           ArticleEndsWithParamRule,
            'set_article_not_end_with_param':                       ArticleNotEndsWithParamRule,
            'set_article_from_another_column':                      ArticleGetFromAnotherColumnRule,
            'if_article_not_str_add_zero_if_len_less_then_param':   ArticleAddZeroIfLessThenParamAndNumericRule,
            'if_article_not_str_add_zeros_to_start_to_len':         ArticleAddZerosIfLessThenParamAndNumericRule,
            'if_article_numeric_add_to_start_param':                ArticleAddParamIfNumericRule,
            'if_rus_pattent_in_article_set_article_from_another_column': ArticleIfRusGetFromAnotherColumnRule,
            'if_article_len_less_param1_set_article_start_param2':  ArticleIfLenLessParam1StartsWithParam2Rule,
            'set_article_from_split_column1_value_by_param2_and_take_part3': ArticleGetFromColumn1SplitByParam2TakePart3Rule,
            'remove_param_from_article':                            RemoveParamFromArticleRule, 
            'remove_params_from_article':                           ArticleRemoveParamsRule,
            'cut_article_value_by_param':                           ArticleCutByParamRule,

            'set_brand_value':                                      BrandSetValueRule,
            'set_brand_from_another_column':                        BrandGetFromColumnRule,
            'set_brand_to_article':                                 BrandSetForArticlesRule,
            'set_brand_by_start_of_article':                        BrandSetByArticlePrefixRule,
            'set_brand_if_param_in_article_mult':                   BrandSetForParamInArticleRule,
            'if_param1_in_comment_set_brand_to_param2':             BrandSetForParamInCommentRule,

            'multiply_price_by_param':                              PriceMultiplyByParamRule,
            'multiply_article_price_by_param':                      PriceMultiplyArticleByParamRule,
            'multiply_price_if_param1_in_col2_by_param3':           PriceMultiplyIfParam1InCol2ByParam3Rule,

            'set_quantity_to_zero':                                 QuantitySetZeroRule,
            'set_quantity_to_param':                                QuantitySetParamRule,
            'storage_partition_by_names':                           StoragePartitionByNameRule,

            'clear_comment':                                        ClearCommentRule,

            'delete_if_in_comment':                                 DeleteIfParamInCommentRule,
            'delete_if_not_in_comment':                             DeleteIfParamNotInCommentRule,
            'delete_if_in_column':                                  DeleteIfParamInColumnRule,
            'delete_if_rus_pattent':                                DeleteIfRusInArticleRule,
            'delete_if_RegEx_in_column':                            DeleteIfRegExInColumnRule,
            'delete_if_price_more_than_param':                      DeleteIfPriceMoreThanParamRule,
            'delete_if_value_more_than_param':                      DeleteIfValueMoreThanParamRule,
            'delete_if_value_equal_param':                          DeleteIfValueEqualParamRule,
            'delete_brands':                                        DeleteBrandsRule,

            'remove_letter_at_end':                                 RemoveLetterFromEndRule,

            'replacement':                                          ReplacementColumnOldNewRule,
     
            'check_article_mann':                                   SpecialArticleMannRule,
            'alfa_article_shit':                                    SpecialArticleAlfaSupplierRule,
            'ravenol_article_rule':                                 SpecialArticleRavenolSupplierRule,
            'elit_article_kh_shit':                                 SpecialArticleElitSupKHRule,
            'intertool_price_multiplier':                           SpecialPriceIntertoolMultiplierRule,
            'vesna_zeros_to_code':                                  VesnaZerosToCodeRule,
            'cardon_aral_price':                                    CardonAralPriceRule,

            'castrol_articles':                                     CastrolArticlesRule,
            'ngk_articles':                                         NgkArticlesRule,
            'denso_articles':                                       DensoArticlesRule,


        }.get(f, None)


    def execute_all(self, row):
        for rule in self.__rules:
            row = rule.execute(row)
        return row
        