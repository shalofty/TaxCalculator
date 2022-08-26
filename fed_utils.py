# Class Utilities
# Federal Brackets and Tax Rates
# Tax Rate is the same throughout Brackets hierarchy. Income is varying factor
class Federal:
    def __init__(self, bracket, taxrate):
        self.bracket = int(bracket)
        self.taxrate = float(taxrate)

    def fedrate(self):
        return self.taxrate


# FEDERAL
fbracket1 = Federal(1, .10)
fbracket2 = Federal(2, .12)
fbracket3 = Federal(3, .22)
fbracket4 = Federal(4, .24)
fbracket5 = Federal(5, .32)
fbracket6 = Federal(6, .35)
fbracket7 = Federal(7, .37)