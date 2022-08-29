# State Class Utilities

from main import *


class State:
    def __init__(self, inmin, inmax, taxrate):
        self.inmin = float(inmin)
        self.inmax = float(inmax)
        self.taxrate = float(taxrate)

    def bracketrate(self):
        return self.taxrate

    def bracketmin(self):
        return self.inmin

    def bracketmax(self):
        return self.inmax


# BRACKETS
sbracket1 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['incomeMin'],
                  data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['incomeMax'],
                  data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['taxRate'])

sbracket2 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 1]['incomeMin'],
                  data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 1]['incomeMax'],
                  data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 1]['taxRate'])

sbracket3 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 2]['incomeMin'],
                  data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 2]['incomeMax'],
                  data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 2]['taxRate'])

sbracket4 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 3]['incomeMin'],
                  data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 3]['incomeMax'],
                  data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 3]['taxRate'])

sbracket5 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 4]['incomeMin'],
                  data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 4]['incomeMax'],
                  data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 4]['taxRate'])

sbracket6 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 5]['incomeMin'],
                  data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 5]['incomeMax'],
                  data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 5]['taxRate'])

sbracket7 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 6]['incomeMin'],
                  data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 6]['incomeMax'],
                  data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 6]['taxRate'])

sbracket8 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 7]['incomeMin'],
                  data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 7]['incomeMax'],
                  data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 7]['taxRate'])

sbracket9 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 8]['incomeMin'],
                  data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 8]['incomeMax'],
                  data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 8]['taxRate'])

sbracket10 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 9]['incomeMin'],
                   data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 9]['incomeMax'],
                   data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 9]['taxRate'])

sbracket11 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 10]['incomeMin'],
                   data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 10]['incomeMax'],
                   data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 10]['taxRate'])

sbracket12 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 11]['incomeMin'],
                   data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 11]['incomeMax'],
                   data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 11]['taxRate'])
