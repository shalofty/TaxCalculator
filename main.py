# Imports
from fed_dicts import *
from fed_utils import *
import json

# Import json state_tax_data
with open("state_tax_data.json") as state_tax_data:
    data = json.load(state_tax_data)

prompt = 0
while prompt <= 1:
    # Main menu function

    print("""
           Welcome to the Python Powered Income Tax Calculator
        Created by Shalofty, this application works for 2023 taxes

        You have the following options (select a number):
        1) Submit Information
        2) Federal Taxes
        3) State Tax
        4) Social Security and Medicare Taxes
        5) All
        6) Clear User Data
        7) Exit
        """)

    menuSelect = input(">>>")
    menuSelect = str(menuSelect)

    def collectData():
        import json
        # User input for annual income
        print("Please have your W2 information ready.")
        income = input("Please enter your annual income for the fiscal year 2022: ")
        income = float(income)

        # User input for state residence
        residence = input("Please enter which state you will be filing your taxes through: ")
        residence = residence.upper()

        # User input for filing status
        filing_status = input("Please enter your filing status for the fiscal year 2022: ")
        filing_status = filing_status.upper()

        # Declaring withheld tax variables
        fedTax = input("Please enter the amount of Federal income tax withheld, in Box 2 of your W2: ")
        fedTax = float(fedTax)

        stateTax = input("Please enter the amount of State income tax withheld, in Box 17 of your W2: ")
        stateTax = float(stateTax)

        # Declaring Social Security withholdings variable
        ssTax = input("Please enter the amount of Social Security tax withheld, in Box 4 of your W2: ")
        ssTax = float(ssTax)

        # Declaring Medicare withholdings variable
        medTax = input("Please enter the amount of Medicare tax withheld, in Box 6 of your W2: ")
        medTax = float(medTax)

        # Creating dictionary from user input
        userData = {
            "income": income,
            "residence": residence,
            "filing_status": filing_status,
            "fedtax": fedTax,
            "statetax": stateTax,
            "sstax": ssTax,
            "medtax": medTax
        }

        # Writing user data to json file
        userJson = json.dumps(userData)
        with open('userdata.json', 'w') as file:
            file.write(userJson)
            file.close()


    def federalCalc():
        # Declaring totalFedTax variable
        totalFedTax = 0

        # Import user data from json file
        with open('userdata.json') as userData:
            info = json.load(userData)

        filing_status = info['filing_status']
        income = info['income']
        fedtaxWithheld = info['fedtax']

        if filing_status == "SINGLE":
            if fed_dict1s["min"] < income < fed_dict1s["max"]:
                maxTax1 = fbracket1.fedrate() * income
                totalFedTax = maxTax1

            elif fed_dict2s["min"] < income < fed_dict2s["max"]:
                maxTax1 = fbracket1.fedrate() * fed_dict1s["max"]
                maxTax2 = fbracket2.fedrate() * (income - fed_dict1s["max"])
                totalFedTax = maxTax1 + maxTax2

            elif fed_dict3s["min"] < income < fed_dict3s["max"]:
                maxTax1 = fbracket1.fedrate() * fed_dict1s["max"]
                maxTax2 = fbracket2.fedrate() * (fed_dict2s["max"] - fed_dict1s["max"])
                maxTax3 = fbracket3.fedrate() * (income - fed_dict2s["max"])
                totalFedTax = maxTax1 + maxTax2 + maxTax3

            elif fed_dict4s["min"] < income < fed_dict4s["max"]:
                maxTax1 = fbracket1.fedrate() * fed_dict1s["max"]
                maxTax2 = fbracket2.fedrate() * (fed_dict2s["max"] - fed_dict1s["max"])
                maxTax3 = fbracket3.fedrate() * (fed_dict3s["max"] - fed_dict2s["max"])
                maxTax4 = fbracket4.fedrate() * (income - fed_dict3s["max"])
                totalFedTax = maxTax1 + maxTax2 + maxTax3 + maxTax4

            elif fed_dict5s["min"] < income < fed_dict5s["max"]:
                maxTax1 = fbracket1.fedrate() * fed_dict1s["max"]
                maxTax2 = fbracket2.fedrate() * (fed_dict2s["max"] - fed_dict1s["max"])
                maxTax3 = fbracket3.fedrate() * (fed_dict3s["max"] - fed_dict2s["max"])
                maxTax4 = fbracket4.fedrate() * (fed_dict4s["max"] - fed_dict3s["max"])
                maxTax5 = fbracket5.fedrate() * (income - fed_dict4s["max"])
                totalFedTax = maxTax1 + maxTax2 + maxTax3 + maxTax4 + maxTax5

            elif fed_dict6s["min"] < income < fed_dict6s["max"]:
                maxTax1 = fbracket1.fedrate() * fed_dict1s["max"]
                maxTax2 = fbracket2.fedrate() * (fed_dict2s["max"] - fed_dict1s["max"])
                maxTax3 = fbracket3.fedrate() * (fed_dict3s["max"] - fed_dict2s["max"])
                maxTax4 = fbracket4.fedrate() * (fed_dict4s["max"] - fed_dict3s["max"])
                maxTax5 = fbracket5.fedrate() * (fed_dict5s["max"] - fed_dict4s["max"])
                maxTax6 = fbracket6.fedrate() * (income - fed_dict5s["max"])
                totalFedTax = maxTax1 + maxTax2 + maxTax3 + maxTax4 + maxTax5 + maxTax6

            elif income > fed_dict7s["min"]:
                maxTax1 = fbracket1.fedrate() * fed_dict1s["max"]
                maxTax2 = fbracket2.fedrate() * (fed_dict2s["max"] - fed_dict1s["max"])
                maxTax3 = fbracket3.fedrate() * (fed_dict3s["max"] - fed_dict2s["max"])
                maxTax4 = fbracket4.fedrate() * (fed_dict4s["max"] - fed_dict3s["max"])
                maxTax5 = fbracket5.fedrate() * (fed_dict5s["max"] - fed_dict4s["max"])
                maxTax6 = fbracket6.fedrate() * (fed_dict6s["max"] - fed_dict5s["max"])
                maxTax7 = fbracket7.fedrate() * (income - fed_dict6s["max"])
                totalFedTax = maxTax1 + maxTax2 + maxTax3 + maxTax4 + maxTax5 + maxTax6 + maxTax7

            else:
                print("Error in fed single if statement")

        # MARRIED FILING JOINTLY SECTION
        elif filing_status == "MARRIED FILING JOINTLY":
            if fed_dict1mfj["min"] < income < fed_dict1mfj["max"]:
                maxTax1 = fbracket1.fedrate() * income
                totalFedTax = maxTax1

            elif fed_dict2mfj["min"] < income < fed_dict2mfj["max"]:
                maxTax1 = fbracket1.fedrate() * fed_dict1mfj["max"]
                maxTax2 = fbracket2.fedrate() * (income - fed_dict1mfj["max"])
                totalFedTax = maxTax1 + maxTax2

            elif fed_dict3mfj["min"] < income < fed_dict3mfj["max"]:
                maxTax1 = fbracket1.fedrate() * fed_dict1mfj["max"]
                maxTax2 = fbracket2.fedrate() * (fed_dict2mfj["max"] - fed_dict1mfj["max"])
                maxTax3 = fbracket3.fedrate() * (income - fed_dict2mfj["max"])
                totalFedTax = maxTax1 + maxTax2 + maxTax3

            elif fed_dict4mfj["min"] < income < fed_dict4mfj["max"]:
                maxTax1 = fbracket1.fedrate() * fed_dict1mfj["max"]
                maxTax2 = fbracket2.fedrate() * (fed_dict2mfj["max"] - fed_dict1mfj["max"])
                maxTax3 = fbracket3.fedrate() * (fed_dict3mfj["max"] - fed_dict2mfj["max"])
                maxTax4 = fbracket4.fedrate() * (income - fed_dict3mfj["max"])
                totalFedTax = maxTax1 + maxTax2 + maxTax3 + maxTax4

            elif fed_dict5mfj["min"] < income < fed_dict5mfj["max"]:
                maxTax1 = fbracket1.fedrate() * fed_dict1mfj["max"]
                maxTax2 = fbracket2.fedrate() * (fed_dict2mfj["max"] - fed_dict1mfj["max"])
                maxTax3 = fbracket3.fedrate() * (fed_dict3mfj["max"] - fed_dict2mfj["max"])
                maxTax4 = fbracket4.fedrate() * (fed_dict4mfj["max"] - fed_dict3mfj["max"])
                maxTax5 = fbracket5.fedrate() * (income - fed_dict4mfj["max"])
                totalFedTax = maxTax1 + maxTax2 + maxTax3 + maxTax4 + maxTax5

            elif fed_dict6mfj["min"] < income < fed_dict6mfj["max"]:
                maxTax1 = fbracket1.fedrate() * fed_dict1mfj["max"]
                maxTax2 = fbracket2.fedrate() * (fed_dict2mfj["max"] - fed_dict1mfj["max"])
                maxTax3 = fbracket3.fedrate() * (fed_dict3mfj["max"] - fed_dict2mfj["max"])
                maxTax4 = fbracket4.fedrate() * (fed_dict4mfj["max"] - fed_dict3mfj["max"])
                maxTax5 = fbracket5.fedrate() * (fed_dict5mfj["max"] - fed_dict4mfj["max"])
                maxTax6 = fbracket6.fedrate() * (income - fed_dict5mfj["max"])
                totalFedTax = maxTax1 + maxTax2 + maxTax3 + maxTax4 + maxTax5 + maxTax6

            elif income > fed_dict7mfj["min"]:
                maxTax1 = fbracket1.fedrate() * fed_dict1mfj["max"]
                maxTax2 = fbracket2.fedrate() * (fed_dict2mfj["max"] - fed_dict1mfj["max"])
                maxTax3 = fbracket3.fedrate() * (fed_dict3mfj["max"] - fed_dict2mfj["max"])
                maxTax4 = fbracket4.fedrate() * (fed_dict4mfj["max"] - fed_dict3mfj["max"])
                maxTax5 = fbracket5.fedrate() * (fed_dict5mfj["max"] - fed_dict4mfj["max"])
                maxTax6 = fbracket6.fedrate() * (fed_dict6mfj["max"] - fed_dict5mfj["max"])
                maxTax7 = fbracket7.fedrate() * (income - fed_dict6mfj["max"])
                totalFedTax = maxTax1 + maxTax2 + maxTax3 + maxTax4 + maxTax5 + maxTax6 + maxTax7

            else:
                print("Error in fed_mfj if statement")

        # FEDERAL withholding vs total amount owed
        if fedtaxWithheld > totalFedTax:
            print("Congratulations! You'll be receiving a refund from your Federal taxes this year.")
            fedRefund = fedtaxWithheld - totalFedTax
            fedRefund = abs(fedRefund)
            # Round 2 decimal places for output to user
            fedRefund = str(round(fedRefund, 2))
            print("Your refund amount is " + fedRefund)
        elif fedtaxWithheld < totalFedTax:
            print("Congratulations, we're finished your Federal tax calculations.")
            fedtaxOwed = totalFedTax - fedtaxWithheld
            # Round 2 decimal places for output to user
            fedtaxOwed = str(round(fedtaxOwed, 2))
            print("This year you owe " + fedtaxOwed + " in Federal taxes.")
        else:
            print("Error in fedtaxWithheld vs totalFedTax if statements")


    def stateCalc():
        # Import user data from json file
        with open('userdata.json') as userData:
            info = json.load(userData)

        residence = info['residence']
        filing_status = info['filing_status']
        income = info['income']
        statetaxWithheld = info['statetax']

        # First iteration through json to see if stateName matches state_input from user
        i = 0
        for states in data['listStates'][i]['stateName']:
            if residence == data['listStates'][i]['stateName']:
                i = i
                break
            else:
                i += 1

        # Second iteration through json to see if status matched filing_status input
        j = 0
        for status in data['listStates'][i]['filingStatus'][j]['status']:
            if filing_status == data['listStates'][i]['filingStatus'][j]['status']:
                j = j
                break
            else:
                print("2nd loop failed")
                j += 1

        # Comparing income, incomeMin < income < incomeMax
        k = 0
        for incomes in data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]:
            # bracketMin and bracketMax must be within for loop for k += 1 to work
            bracketMin = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['incomeMin']
            bracketMax = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['incomeMax']
            if bracketMin <= income <= bracketMax:
                k = k
                # print(num_brackets)
                break
            else:
                k += 1

        # Creating State class with taxrate, min and max methods
        class State:
            def __init__(self, inmin, inmax, staxrate):
                self.inmin = float(inmin)
                self.inmax = float(inmax)
                self.staxrate = float(staxrate)

            def bracketrate(self):
                return self.staxrate

            def bracketmin(self):
                return self.inmin

            def bracketmax(self):
                return self.inmax

        # BRACKETS

        # Calculating state taxes based on bracket system using State class variables
        # State class variables must be instantiated within if statement
        num_brackets = k + 1
        if num_brackets == 1 and income < bracketMax:
            # Calculating single bracket tax as sbrax1

            sbracket1 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['taxRate'])

            sbrax1 = sbracket1.staxrate * income
            totalStateTax = sbrax1

        # 2 bracket states taxRate
        elif num_brackets == 2:

            sbracket1 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['taxRate'])

            sbracket2 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['taxRate'])

            sbrax1 = sbracket1.staxrate * sbracket1.inmax
            sbrax2 = sbracket2.staxrate * (income - sbracket1.inmax)
            totalStateTax = sbrax1 + sbrax2

        # 3 bracket states taxRate
        elif num_brackets == 3:

            sbracket1 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['taxRate'])

            sbracket2 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['taxRate'])

            sbracket3 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['taxRate'])

            sbrax1 = sbracket1.staxrate * sbracket1.inmax
            sbrax2 = sbracket2.staxrate * sbracket2.inmax
            sbrax3 = sbracket3.staxrate * (income - sbracket2.inmax)
            totalStateTax = sbrax1 + sbrax2 + sbrax3

        # 4 bracket states taxRate
        elif num_brackets == 4:
            # For testing purposes, Arizona is a 4 bracket state

            sbracket1 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['taxRate'])

            sbracket2 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['taxRate'])

            sbracket3 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['taxRate'])

            sbracket4 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['taxRate'])

            sbrax1 = sbracket1.staxrate * sbracket1.inmax
            sbrax2 = sbracket2.staxrate * sbracket2.inmax
            sbrax3 = sbracket3.staxrate * sbracket3.inmax
            sbrax4 = sbracket4.staxrate * (income - sbracket3.inmax)
            totalStateTax = sbrax1 + sbrax2 + sbrax3 + sbrax4

        # 5 bracket states taxRate
        elif num_brackets == 5:

            sbracket1 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['taxRate'])

            sbracket2 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['taxRate'])

            sbracket3 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['taxRate'])

            sbracket4 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['taxRate'])

            sbracket5 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][4]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][4]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][4]['taxRate'])

            sbrax1 = sbracket1.staxrate * sbracket1.inmax
            sbrax2 = sbracket2.staxrate * sbracket2.inmax
            sbrax3 = sbracket3.staxrate * sbracket3.inmax
            sbrax4 = sbracket4.staxrate * sbracket4.inmax
            sbrax5 = sbracket5.staxrate * (income - sbracket4.inmax)
            totalStateTax = sbrax1 + sbrax2 + sbrax3 + sbrax4 + sbrax5

        # 6 bracket states taxRate
        elif num_brackets == 6:

            sbracket1 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['taxRate'])

            sbracket2 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['taxRate'])

            sbracket3 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['taxRate'])

            sbracket4 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['taxRate'])

            sbracket5 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][4]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][4]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][4]['taxRate'])

            sbracket6 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][5]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][5]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][5]['taxRate'])

            sbrax1 = sbracket1.staxrate * sbracket1.inmax
            sbrax2 = sbracket2.staxrate * sbracket2.inmax
            sbrax3 = sbracket3.staxrate * sbracket3.inmax
            sbrax4 = sbracket4.staxrate * sbracket4.inmax
            sbrax5 = sbracket5.staxrate * sbracket5.inmax
            sbrax6 = sbracket6.staxrate * (income - sbracket5.inmax)
            totalStateTax = sbrax1 + sbrax2 + sbrax3 + sbrax4 + sbrax5 + sbrax6

        # 7 bracket states taxRate
        elif num_brackets == 7:

            sbracket1 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['taxRate'])

            sbracket2 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['taxRate'])

            sbracket3 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['taxRate'])

            sbracket4 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['taxRate'])

            sbracket5 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][4]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][4]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][4]['taxRate'])

            sbracket6 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][5]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][5]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][5]['taxRate'])

            sbracket7 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][6]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][6]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][6]['taxRate'])

            sbrax1 = sbracket1.staxrate * sbracket1.inmax
            sbrax2 = sbracket2.staxrate * sbracket2.inmax
            sbrax3 = sbracket3.staxrate * sbracket3.inmax
            sbrax4 = sbracket4.staxrate * sbracket4.inmax
            sbrax5 = sbracket5.staxrate * sbracket5.inmax
            sbrax6 = sbracket6.staxrate * sbracket6.inmax
            sbrax7 = sbracket7.staxrate * (income - sbracket6.inmax)
            totalStateTax = sbrax1 + sbrax2 + sbrax3 + sbrax4 + sbrax5 + sbrax6 + sbrax7

        # 8 bracket states taxRate
        elif num_brackets == 8:

            sbracket1 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['taxRate'])

            sbracket2 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['taxRate'])

            sbracket3 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['taxRate'])

            sbracket4 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['taxRate'])

            sbracket5 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][4]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][4]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][4]['taxRate'])

            sbracket6 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][5]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][5]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][5]['taxRate'])

            sbracket7 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][6]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][6]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][6]['taxRate'])

            sbracket8 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][7]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][7]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][7]['taxRate'])

            sbrax1 = sbracket1.staxrate * sbracket1.inmax
            sbrax2 = sbracket2.staxrate * sbracket2.inmax
            sbrax3 = sbracket3.staxrate * sbracket3.inmax
            sbrax4 = sbracket4.staxrate * sbracket4.inmax
            sbrax5 = sbracket5.staxrate * sbracket5.inmax
            sbrax6 = sbracket6.staxrate * sbracket6.inmax
            sbrax7 = sbracket7.staxrate * sbracket7.inmax
            sbrax8 = sbracket8.staxrate * (income - sbracket7.inmax)
            totalStateTax = sbrax1 + sbrax2 + sbrax3 + sbrax4 + sbrax5 + sbrax6 + sbrax7 + sbrax8

        # 9 bracket states taxRate
        elif num_brackets == 9:

            sbracket1 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['taxRate'])

            sbracket2 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['taxRate'])

            sbracket3 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['taxRate'])

            sbracket4 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['taxRate'])

            sbracket5 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][4]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][4]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][4]['taxRate'])

            sbracket6 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][5]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][5]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][5]['taxRate'])

            sbracket7 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][6]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][6]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][6]['taxRate'])

            sbracket8 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][7]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][7]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][7]['taxRate'])

            sbracket9 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][8]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][8]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][8]['taxRate'])

            sbrax1 = sbracket1.staxrate * sbracket1.inmax
            sbrax2 = sbracket2.staxrate * sbracket2.inmax
            sbrax3 = sbracket3.staxrate * sbracket3.inmax
            sbrax4 = sbracket4.staxrate * sbracket4.inmax
            sbrax5 = sbracket5.staxrate * sbracket5.inmax
            sbrax6 = sbracket6.staxrate * sbracket6.inmax
            sbrax7 = sbracket7.staxrate * sbracket7.inmax
            sbrax8 = sbracket8.staxrate * sbracket8.inmax
            sbrax9 = sbracket9.staxrate * (income - sbracket8.inmax)
            totalStateTax = sbrax1 + sbrax2 + sbrax3 + sbrax4 + sbrax5 + sbrax6 + sbrax7 + sbrax8 + sbrax9

        # 10 bracket states taxRate
        elif num_brackets == 10:

            sbracket1 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['taxRate'])

            sbracket2 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['taxRate'])

            sbracket3 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['taxRate'])

            sbracket4 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['taxRate'])

            sbracket5 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][4]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][4]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][4]['taxRate'])

            sbracket6 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][5]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][5]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][5]['taxRate'])

            sbracket7 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][6]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][6]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][6]['taxRate'])

            sbracket8 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][7]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][7]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][7]['taxRate'])

            sbracket9 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][8]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][8]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][8]['taxRate'])

            sbracket10 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][9]['incomeMin'],
                               data['listStates'][i]['filingStatus'][j]['incomeBrackets'][9]['incomeMax'],
                               data['listStates'][i]['filingStatus'][j]['incomeBrackets'][9]['taxRate'])

            sbrax1 = sbracket1.staxrate * sbracket1.inmax
            sbrax2 = sbracket2.staxrate * sbracket2.inmax
            sbrax3 = sbracket3.staxrate * sbracket3.inmax
            sbrax4 = sbracket4.staxrate * sbracket4.inmax
            sbrax5 = sbracket5.staxrate * sbracket5.inmax
            sbrax6 = sbracket6.staxrate * sbracket6.inmax
            sbrax7 = sbracket7.staxrate * sbracket7.inmax
            sbrax8 = sbracket8.staxrate * sbracket8.inmax
            sbrax9 = sbracket9.staxrate * sbracket9.inmax
            sbrax10 = sbracket10.staxrate * (income - sbracket9.inmax)
            totalStateTax = sbrax1 + sbrax2 + sbrax3 + sbrax4 + sbrax5 + sbrax6 + sbrax7 + sbrax8 + sbrax9 + sbrax10

        # No state has 11 brackets
        # 12 bracket states taxRate - Hawaii
        elif num_brackets == 12:

            sbracket1 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][0]['taxRate'])

            sbracket2 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][1]['taxRate'])

            sbracket3 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][2]['taxRate'])

            sbracket4 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][3]['taxRate'])

            sbracket5 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][4]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][4]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][4]['taxRate'])

            sbracket6 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][5]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][5]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][5]['taxRate'])

            sbracket7 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][6]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][6]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][6]['taxRate'])

            sbracket8 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][7]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][7]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][7]['taxRate'])

            sbracket9 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][8]['incomeMin'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][8]['incomeMax'],
                              data['listStates'][i]['filingStatus'][j]['incomeBrackets'][8]['taxRate'])

            sbracket10 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][9]['incomeMin'],
                               data['listStates'][i]['filingStatus'][j]['incomeBrackets'][9]['incomeMax'],
                               data['listStates'][i]['filingStatus'][j]['incomeBrackets'][9]['taxRate'])

            sbracket11 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][10]['incomeMin'],
                               data['listStates'][i]['filingStatus'][j]['incomeBrackets'][10]['incomeMax'],
                               data['listStates'][i]['filingStatus'][j]['incomeBrackets'][10]['taxRate'])

            sbracket12 = State(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][11]['incomeMin'],
                               data['listStates'][i]['filingStatus'][j]['incomeBrackets'][11]['incomeMax'],
                               data['listStates'][i]['filingStatus'][j]['incomeBrackets'][11]['taxRate'])

            sbrax1 = sbracket1.staxrate * sbracket1.inmax
            sbrax2 = sbracket2.staxrate * sbracket2.inmax
            sbrax3 = sbracket3.staxrate * sbracket3.inmax
            sbrax4 = sbracket4.staxrate * sbracket4.inmax
            sbrax5 = sbracket5.staxrate * sbracket5.inmax
            sbrax6 = sbracket6.staxrate * sbracket6.inmax
            sbrax7 = sbracket7.staxrate * sbracket7.inmax
            sbrax8 = sbracket8.staxrate * sbracket8.inmax
            sbrax9 = sbracket9.staxrate * sbracket9.inmax
            sbrax10 = sbracket10.staxrate * sbracket10.inmax
            sbrax11 = sbracket11.staxrate * sbracket11.inmax
            sbrax12 = sbracket12.staxrate * (income - sbracket11.inmax)
            totalStateTax = sbrax1 + sbrax2 + sbrax3 + sbrax4 + sbrax5 + sbrax6 + sbrax7 + sbrax8 + sbrax9 + sbrax10 + sbrax11 + sbrax12

        else:
            print("Error in num_brackets if statement")

        # Begin totalStateTax calculations using staxRate variable

        if totalStateTax > statetaxWithheld:
            totalstaxOwed = totalStateTax - statetaxWithheld
            # Round 2 decimal places for output to user
            totalstaxOwed = str(round(totalstaxOwed, 2))
            print("Congratulations! We're finished with your State tax calculations.")
            print("You currently owe " + totalstaxOwed + " in State taxes.")
        elif totalStateTax < statetaxWithheld:
            statetaxRefund = statetaxWithheld - totalStateTax
            # Round 2 decimal places for output to user
            statetaxRefund = str(round(statetaxRefund, 2))
            print("Congratulations! We're finished with your State tax calculations.")
            print("You'll be receiving a " + statetaxRefund + " refund!")
        elif totalStateTax == 0:
            print("Congratulations! You don't owe any State taxes!")
        else:
            print("Error in totalStateTax if")


    def ssCalc():
        # Import user data from json file
        with open('userdata.json') as userData:
            info = json.load(userData)

        sstaxWithheld = info['sstax']
        income = info['income']

        # Social Security tax calculations
        if income < ss_dict["max"]:
            # Declare sstaxOwed variable
            sstaxOwed = social_security.taxrate * income
        elif income > ss_dict["max"]:
            # Social Security tax has an income ceiling, no tax on any income past ss_dict["max"]
            sstaxOwed = social_security.taxrate * ss_dict["max"]
        else:
            print("Error in Social Security calculations if statement pt. 2")

        if sstaxOwed > sstaxWithheld:
            sstaxOwed = sstaxOwed - sstaxWithheld
            # Round 2 decimal places for output to user
            sstaxOwed = str(round(sstaxOwed, 2))
            print("You didn't pay enough on Social Security tax this year. You'll need to pay " + sstaxOwed)
        elif sstaxOwed < sstaxWithheld:
            sstaxOwed = sstaxWithheld - sstaxOwed
            # Round 2 decimal places for output to user
            sstaxOwed = str(round(sstaxOwed, 2))
            print("You overpaid on your Social Security tax this year. You'll receive " + sstaxOwed + " as a refund.")
        else:
            print("Error in Social Security calculations if statement pt. 2")


    def medCalc():
        # Import user data from json file
        with open('userdata.json') as userData:
            info = json.load(userData)

        medtaxWithheld = info['medtax']
        income = info['income']

        # Medicare tax calculations
        medtaxOwed = income * medicare.taxrate
        if medtaxOwed > medtaxWithheld:
            medtaxBalance = medtaxOwed - medtaxWithheld
            # Round 2 decimal places for output to user
            medtaxBalance = str(round(medtaxBalance, 2))
            print("You didn't pay enough on Medicare tax this year. You'll need to pay " + medtaxBalance)
        elif medtaxOwed < medtaxWithheld:
            medtaxRefund = medtaxWithheld - medtaxOwed
            # Round 2 decimal places for output to user
            medtaxRefund = str(round(medtaxRefund, 2))
            print("You overpaid on Medicare tax this year. You'll receive " + medtaxRefund + "as a refund.")
        else:
            print("Error in medtax if statement")


    if menuSelect == "1":
        collectData()

    elif menuSelect == "2":
        federalCalc()

    elif menuSelect == "3":
        stateCalc()

    elif menuSelect == "4":
        ssCalc()
        medCalc()

    elif menuSelect == "5":
        federalCalc()
        stateCalc()
        ssCalc()
        medCalc()

    elif menuSelect == "6":
        # Set all userData information to 0.
        zeroData = {
            "income": 0,
            "residence": 0,
            "filing_status": 0,
            "fedtax": 0,
            "statetax": 0,
            "sstax": 0,
            "medtax": 0
        }

        # Writing to json file
        zJson = json.dumps(zeroData)
        with open('userdata.json', 'w') as zfile:
            zfile.write(zJson)
            zfile.close()

    elif menuSelect == "7":
        prompt += 1

    else:
        print("Error: menuSelect")
