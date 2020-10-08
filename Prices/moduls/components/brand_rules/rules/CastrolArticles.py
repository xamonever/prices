from ..basicRule import BasicRule


class CastrolArticlesRule(BasicRule):
    """castrol_articles"""
    
    castrol_dict = {
        'N4-GTX10B4-12X1     ': 'N4-GTX10B4-12X1     ',
        'UR-GTX10B4-4X4L     ': 'UR-GTX10B4-4X4L     ',
        '15A4DE              ': 'RB-GTXUA3-12X1L     ',
        '15A4E0              ': 'RB-GTXUA3-4X4L      ',
        '15A726              ': '15A727',
        '155BA8              ': '155BA9',
        '157E6A              ': 'RB-EDG0334-12X1     ',
        '157E6B              ': 'SWE 108             ',
        '156E8B              ': 'R1-EDG04B4-X1T      ',
        '156E8C              ': 'RB-EDG04B4-4X4L     ',
        '15667C              ': 'RB-EDG53L-12X1L     ',
        '15669A              ': 'RB-EDG53L-4X4L      ',
        '15A001              ': 'R1-EDGE106-12x1     ',
        '15A008              ': 'R1-EDGE106-4x4L     ',
        '156EDC              ': 'RB-MD5DPF-12X1L     ',
        '156EDD              ': 'RB-MD5DPF-4X4L      ',
        'RB-MAG53A3-4X4L     ': 'RB-MAG53A3-4X4L     ',
        '155BA7              ': 'RB-MAG53AP-X1N      ',
        '155BA8              ': 'RB-MAG10B4-12X1     ',
        '156EEC              ': 'RB-MAG10B4-4X4L     ',
        '156EED              ': 'RB-MAGDB4-12X1L     ',
        '156ED9              ': 'RB-MAGDB4-4X4L      ',
        '156ED8              ': 'RB-AXEPX89-12X1     ',
        '154CB7              ': 'RB-SYNUP7-12X1L     ',
        '154F6D              ': 'RB-MEP809-12X1L     ',
        '154FA3              ': 'RB-SYNM759-12X1     ',
        '157F42              ': 'RB-ATFD2M-12X1L     ',
        '157AB3              ': '157AB4',
        '157F3E              ': 'EB-TRANSDL-12x1     ',
        '1585A5              ': 'EB-TRANSZ-12X1L     ',
        '1543AE              ': 'EB-SYNTLL-12X1L     ',
        '156E9D              ': 'RB-MAG54A3-12X1     ',
        '156E9E              ': 'RB-MAG54A3-4X4L     ',
        '157B1B              ': 'RB-EDGE540-12X1     ',
        '157B1C              ': 'RB-EDGE540-4X4L     ',
        '15A16E              ': 'UR-MSS53A5-4X4L     ',
        '156DCF              ': 'RB-MSSE520-X1L      ',
        '15A7C6              ': 'RB-MSSE520-4X4L     ',
        '15A16D              ': 'UR-MSS53A5-12X1     ',
        '15A170              ': 'UR-MSS53AB-4X4L     ',
    }

    def __init__(self, brand, param, columns):
        self.brand = brand.lower()
        self.param = param.lower()
        self.brandCol = columns.brandCol
        self.articleCol = columns.articleCol
    

    def execute(self, row):
        if str(row[self.brandCol]).lower() != self.brand and self.brand !=  'все бренды': return row
        for  key, val in self.castrol_dict.items():            
            if str(row[self.articleCol]).strip().lower() == key.strip().lower():
                row[self.articleCol] = val
                break
        return row

