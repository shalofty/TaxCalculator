# State Class Utilities
# State Brackets and Tax Rates
# Brackets, Rates and Income vary per state
class State:
    def __init__(self, state, bracket, taxrate):
        self.state = str(state)
        self.bracket = int(bracket)
        self.taxrate = float(taxrate)

    def staterate(self):
        return self.taxrate

    def statename(self):
        return self.state


# ALABAMA
sbracket1_al = State("AL", 1, .02)
sbracket2_al = State("AL", 2, .04)
sbracket3_al = State("AL", 3, .05)

# ALASKA
alaska_bracket1 = State("AR", 1, 0)

# ARIZONA
# ARKANSAS
# CALIFORNIA
# COLORADO
