from .partline_help import PartlineHelp


class BaseHelp(object):
    """docstring for BaseHelp"""

    def __init__(self, helpers, columns):
        self.__helpers_bodies = []
        for another_helper in helpers:
            helper = self.get_helper(another_helper)
            if helper:
                self.__helpers_bodies.append(helper(columns=columns))


    def get_helper(self, helper):
        return {
            'partline_filter': PartlineHelp,
        }.get(helper, None)


    def run(self, data_list):
        for h in self.__helpers_bodies:
            data_list = h.execute(data_list)
        return data_list
        