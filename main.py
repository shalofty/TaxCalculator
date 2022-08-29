import math

from state_utils import *

# Federal imports
from fed_dicts import *
from fed_utils import *
import json

with open("state_tax_data.json") as state_tax_data:
    data = json.load(state_tax_data)

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

# Declaring totalFedTax variable
totalFedTax = 0

# Declaring withheld tax variables
fedtaxWithheld = input("Please enter the amount of Federal income tax withheld, in Box 2 of your W2: ")
fedtaxWithheld = float(fedtaxWithheld)

statetaxWithheld = input("Please enter the amount of State income tax withheld, in Box 17 of your W2: ")
statetaxWithheld = float(statetaxWithheld)

# Declaring Social Security withholdings variable
sstaxWithheld = input("Please enter the amount of Social Security tax withheld, in Box 4 of your W2: ")
sstaxWithheld = float(sstaxWithheld)

# Declaring Medicare withholdings variable
medtaxWithheld = input("Please enter the amount of Medicare tax withheld, in Box 6 of your W2: ")
medtaxWithheld = float(medtaxWithheld)

# If statement comparing bracket dictionaries minimum and maximum values to user income
# totalFedTax is tax owed

# Federal Tax Calculations
# SINGLE FILERS SECTION
if filing_status == "SINGLE":
    if fed_dict1s["min"] < income < fed_dict1s["max"]:
        maxTax1 = fbracket1.fedrate() * income
        totalFedTax = maxTax1
        print(totalFedTax)

    elif fed_dict2s["min"] < income < fed_dict2s["max"]:
        maxTax1 = fbracket1.fedrate() * fed_dict1s["max"]
        maxTax2 = fbracket2.fedrate() * (income - fed_dict1s["max"])
        totalFedTax = maxTax1 + maxTax2
        print(totalFedTax)

    elif fed_dict3s["min"] < income < fed_dict3s["max"]:
        maxTax1 = fbracket1.fedrate() * fed_dict1s["max"]
        maxTax2 = fbracket2.fedrate() * (fed_dict2s["max"] - fed_dict1s["max"])
        maxTax3 = fbracket3.fedrate() * (income - fed_dict2s["max"])
        totalFedTax = maxTax1 + maxTax2 + maxTax3
        print(totalFedTax)

    elif fed_dict4s["min"] < income < fed_dict4s["max"]:
        maxTax1 = fbracket1.fedrate() * fed_dict1s["max"]
        maxTax2 = fbracket2.fedrate() * (fed_dict2s["max"] - fed_dict1s["max"])
        maxTax3 = fbracket3.fedrate() * (fed_dict3s["max"] - fed_dict2s["max"])
        maxTax4 = fbracket4.fedrate() * (income - fed_dict3s["max"])
        totalFedTax = maxTax1 + maxTax2 + maxTax3 + maxTax4
        print(totalFedTax)

    elif fed_dict5s["min"] < income < fed_dict5s["max"]:
        maxTax1 = fbracket1.fedrate() * fed_dict1s["max"]
        maxTax2 = fbracket2.fedrate() * (fed_dict2s["max"] - fed_dict1s["max"])
        maxTax3 = fbracket3.fedrate() * (fed_dict3s["max"] - fed_dict2s["max"])
        maxTax4 = fbracket4.fedrate() * (fed_dict4s["max"] - fed_dict3s["max"])
        maxTax5 = fbracket5.fedrate() * (income - fed_dict4s["max"])
        totalFedTax = maxTax1 + maxTax2 + maxTax3 + maxTax4 + maxTax5
        print(totalFedTax)

    elif fed_dict6s["min"] < income < fed_dict6s["max"]:
        maxTax1 = fbracket1.fedrate() * fed_dict1s["max"]
        maxTax2 = fbracket2.fedrate() * (fed_dict2s["max"] - fed_dict1s["max"])
        maxTax3 = fbracket3.fedrate() * (fed_dict3s["max"] - fed_dict2s["max"])
        maxTax4 = fbracket4.fedrate() * (fed_dict4s["max"] - fed_dict3s["max"])
        maxTax5 = fbracket5.fedrate() * (fed_dict5s["max"] - fed_dict4s["max"])
        maxTax6 = fbracket6.fedrate() * (income - fed_dict5s["max"])
        totalFedTax = maxTax1 + maxTax2 + maxTax3 + maxTax4 + maxTax5 + maxTax6
        print(totalFedTax)

    elif income > fed_dict7s["min"]:
        maxTax1 = fbracket1.fedrate() * fed_dict1s["max"]
        maxTax2 = fbracket2.fedrate() * (fed_dict2s["max"] - fed_dict1s["max"])
        maxTax3 = fbracket3.fedrate() * (fed_dict3s["max"] - fed_dict2s["max"])
        maxTax4 = fbracket4.fedrate() * (fed_dict4s["max"] - fed_dict3s["max"])
        maxTax5 = fbracket5.fedrate() * (fed_dict5s["max"] - fed_dict4s["max"])
        maxTax6 = fbracket6.fedrate() * (fed_dict6s["max"] - fed_dict5s["max"])
        maxTax7 = fbracket7.fedrate() * (income - fed_dict6s["max"])
        totalFedTax = maxTax1 + maxTax2 + maxTax3 + maxTax4 + maxTax5 + maxTax6 + maxTax7
        print(totalFedTax)

    else:
        print("Error in fed single if statement")

# MARRIED FILING JOINTLY SECTION
elif filing_status == "MARRIED FILING JOINTLY":
    if fed_dict1mfj["min"] < income < fed_dict1mfj["max"]:
        maxTax1 = fbracket1.fedrate() * income
        totalFedTax = maxTax1
        print(totalFedTax)

    elif fed_dict2mfj["min"] < income < fed_dict2mfj["max"]:
        maxTax1 = fbracket1.fedrate() * fed_dict1mfj["max"]
        maxTax2 = fbracket2.fedrate() * (income - fed_dict1mfj["max"])
        totalFedTax = maxTax1 + maxTax2
        print(totalFedTax)

    elif fed_dict3mfj["min"] < income < fed_dict3mfj["max"]:
        maxTax1 = fbracket1.fedrate() * fed_dict1mfj["max"]
        maxTax2 = fbracket2.fedrate() * (fed_dict2mfj["max"] - fed_dict1mfj["max"])
        maxTax3 = fbracket3.fedrate() * (income - fed_dict2mfj["max"])
        totalFedTax = maxTax1 + maxTax2 + maxTax3
        print(totalFedTax)

    elif fed_dict4mfj["min"] < income < fed_dict4mfj["max"]:
        maxTax1 = fbracket1.fedrate() * fed_dict1mfj["max"]
        maxTax2 = fbracket2.fedrate() * (fed_dict2mfj["max"] - fed_dict1mfj["max"])
        maxTax3 = fbracket3.fedrate() * (fed_dict3mfj["max"] - fed_dict2mfj["max"])
        maxTax4 = fbracket4.fedrate() * (income - fed_dict3mfj["max"])
        totalFedTax = maxTax1 + maxTax2 + maxTax3 + maxTax4
        print(totalFedTax)

    elif fed_dict5mfj["min"] < income < fed_dict5mfj["max"]:
        maxTax1 = fbracket1.fedrate() * fed_dict1mfj["max"]
        maxTax2 = fbracket2.fedrate() * (fed_dict2mfj["max"] - fed_dict1mfj["max"])
        maxTax3 = fbracket3.fedrate() * (fed_dict3mfj["max"] - fed_dict2mfj["max"])
        maxTax4 = fbracket4.fedrate() * (fed_dict4mfj["max"] - fed_dict3mfj["max"])
        maxTax5 = fbracket5.fedrate() * (income - fed_dict4mfj["max"])
        totalFedTax = maxTax1 + maxTax2 + maxTax3 + maxTax4 + maxTax5
        print(totalFedTax)

    elif fed_dict6mfj["min"] < income < fed_dict6mfj["max"]:
        maxTax1 = fbracket1.fedrate() * fed_dict1mfj["max"]
        maxTax2 = fbracket2.fedrate() * (fed_dict2mfj["max"] - fed_dict1mfj["max"])
        maxTax3 = fbracket3.fedrate() * (fed_dict3mfj["max"] - fed_dict2mfj["max"])
        maxTax4 = fbracket4.fedrate() * (fed_dict4mfj["max"] - fed_dict3mfj["max"])
        maxTax5 = fbracket5.fedrate() * (fed_dict5mfj["max"] - fed_dict4mfj["max"])
        maxTax6 = fbracket6.fedrate() * (income - fed_dict5mfj["max"])
        totalFedTax = maxTax1 + maxTax2 + maxTax3 + maxTax4 + maxTax5 + maxTax6
        print(totalFedTax)

    elif income > fed_dict7mfj["min"]:
        maxTax1 = fbracket1.fedrate() * fed_dict1mfj["max"]
        maxTax2 = fbracket2.fedrate() * (fed_dict2mfj["max"] - fed_dict1mfj["max"])
        maxTax3 = fbracket3.fedrate() * (fed_dict3mfj["max"] - fed_dict2mfj["max"])
        maxTax4 = fbracket4.fedrate() * (fed_dict4mfj["max"] - fed_dict3mfj["max"])
        maxTax5 = fbracket5.fedrate() * (fed_dict5mfj["max"] - fed_dict4mfj["max"])
        maxTax6 = fbracket6.fedrate() * (fed_dict6mfj["max"] - fed_dict5mfj["max"])
        maxTax7 = fbracket7.fedrate() * (income - fed_dict6mfj["max"])
        totalFedTax = maxTax1 + maxTax2 + maxTax3 + maxTax4 + maxTax5 + maxTax6 + maxTax7
        print(totalFedTax)

    else:
        print("Error in fed_mfj if statement")

# First iteration through json to see if stateName matches state_input from user
i = 0
for states in data['listStates'][i]['stateName']:
    if residence == data['listStates'][i]['stateName']:
        print("1st for loop works")
        i = i
        print(data['listStates'][i]['stateName'])
        break
    else:
        i += 1

# Second iteration through json to see if status matched filing_status input
j = 0
for status in data['listStates'][i]['filingStatus'][j]['status']:
    if filing_status == data['listStates'][i]['filingStatus'][j]['status']:
        print("2nd for loop works")
        j = j
        print(data['listStates'][i]['filingStatus'][j]['status'])
        break
    else:
        print("2nd loop failed")
        j += 1

# Possible solution for state bracket calculations, similar to how federal was handled

# Comparing income, incomeMin < income < incomeMax
k = 0
for incomes in data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]:
    # bracketMin and bracketMax must be within for loop for k += 1 to work
    bracketMin = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['incomeMin']
    bracketMax = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['incomeMax']
    if bracketMin < income < bracketMax:
        print("bracketMin < income < bracketMax works")
        num_brackets = len(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k])
        print(num_brackets)
        k = k
        break
    else:
        print("bracketMin/Max if statement error")
        print(bracketMin)
        print(bracketMax)
        k += 1


# incomeBrackets array length
bracket_length = len(data['listStates'][i]['filingStatus'][j]['incomeBrackets'])

# Calculating state taxes based on bracket system
if k == 0 and income < bracketMax:
    # Calculating single bracket tax as sbrax1
    sbrax1 = sbracket1.bracketrate()
    totalStateTax = sbrax1
    print(sbrax1)

# 2 bracket states taxRate
elif k == 1:
    # Calculating tax for 2 bracket system
    sbrax1 = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['incomeMax'] * data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['taxRate']
    brack2taxable = income - data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['incomeMax']
    print("2 bracket state error")

# 3 bracket states taxRate
elif k == 2:
    sbracketTax1 = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k - 2]['taxRate']
    print(sbracketTax1)
    sbracketTax2 = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k - 1]['taxRate']
    print(sbracketTax2)
    sbracketTax3 = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['taxRate']
    print(sbracketTax3)
    print(k)

# 4 bracket states taxRate
elif num_brackets == 4:
    # For testing purposes, Arizona is a 4 bracket state
    b1taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['taxRate']
    b2taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 1]['taxRate']
    b3taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 2]['taxRate']
    b4taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 3]['taxRate']
    # maxstateTax is wrong, should be bracket income max * bntaxRate
    print("4 bracket state error")

# 5 bracket states taxRate
elif num_brackets == 5:
    b1taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['taxRate']
    b2taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 1]['taxRate']
    b3taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 2]['taxRate']
    b4taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 3]['taxRate']
    b5taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 4]['taxRate']
    print("5 bracket state error")

# 6 bracket states taxRate
elif num_brackets == 6:
    b1taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['taxRate']
    b2taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 1]['taxRate']
    b3taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 2]['taxRate']
    b4taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 3]['taxRate']
    b5taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 4]['taxRate']
    b6taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 5]['taxRate']
    print("6 bracket state error")

# 7 bracket states taxRate
elif num_brackets == 7:
    b1taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['taxRate']
    b2taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 1]['taxRate']
    b3taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 2]['taxRate']
    b4taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 3]['taxRate']
    b5taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 4]['taxRate']
    b6taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 5]['taxRate']
    b7taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 6]['taxRate']
    print("7 bracket state error")

# 8 bracket states taxRate
elif num_brackets == 8:
    b1taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['taxRate']
    b2taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 1]['taxRate']
    b3taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 2]['taxRate']
    b4taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 3]['taxRate']
    b5taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 4]['taxRate']
    b6taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 5]['taxRate']
    b7taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 6]['taxRate']
    b8taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 7]['taxRate']
    print("8 bracket state error")

# 9 bracket states taxRate
elif num_brackets == 9:
    b1taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['taxRate']
    b2taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 1]['taxRate']
    b3taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 2]['taxRate']
    b4taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 3]['taxRate']
    b5taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 4]['taxRate']
    b6taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 5]['taxRate']
    b7taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 6]['taxRate']
    b8taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 7]['taxRate']
    b9taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 8]['taxRate']
    print("9 bracket state error")

# 10 bracket states taxRate
elif num_brackets == 10:
    b1taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['taxRate']
    b2taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 1]['taxRate']
    b3taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 2]['taxRate']
    b4taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 3]['taxRate']
    b5taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 4]['taxRate']
    b6taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 5]['taxRate']
    b7taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 6]['taxRate']
    b8taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 7]['taxRate']
    b9taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 8]['taxRate']
    b10taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 9]['taxRate']
    print("10 bracket state error")

# 11 bracket states taxRate
# No state has 11 brackets
elif num_brackets == 11:
    b1taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['taxRate']
    b2taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 1]['taxRate']
    b3taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 2]['taxRate']
    b4taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 3]['taxRate']
    b5taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 4]['taxRate']
    b6taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 5]['taxRate']
    b7taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 6]['taxRate']
    b8taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 7]['taxRate']
    b9taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 8]['taxRate']
    b10taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 9]['taxRate']
    b11taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 10]['taxRate']
    print("11 bracket state error")

# 12 bracket states taxRate
elif num_brackets == 12:
    b1taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['taxRate']
    b2taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 1]['taxRate']
    b3taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 2]['taxRate']
    b4taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 3]['taxRate']
    b5taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 4]['taxRate']
    b6taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 5]['taxRate']
    b7taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 6]['taxRate']
    b8taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 7]['taxRate']
    b9taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 8]['taxRate']
    b10taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 9]['taxRate']
    b11taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 10]['taxRate']
    b12taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 11]['taxRate']
    print("12 bracket state error")

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
