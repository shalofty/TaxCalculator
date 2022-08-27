from numpy import arange

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

# Beginning of third iteration
# Need workaround for float precision
k = 0
k_range = (len(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]) + 1)
while k < k_range:
    if income in range(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['income'], data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 1]['income'], 1):
        print("Success in range for loop")
        k = k
        staxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['taxRate']
        break
    elif income > data['listStates'][i]['filingStatus'][j]['incomeBrackets'][-1]['income']:
        print("Negative iteration success")
        k = k
        staxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][-1]['taxRate']
        break
    else:
        print("Range loop failed")
        print(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['income'])
        print(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 1]['income'])
        print(k)
        k += 1

# Begin totalStateTax calculations using staxRate variable
totalStateTax = staxRate * income

if totalStateTax > statetaxWithheld:
    totalstaxOwed = totalStateTax - statetaxWithheld
    totalstaxOwed = str(totalstaxOwed)
    print("Congratulations! We're finished with your State tax calculations.")
    print("You currently owe " + totalstaxOwed + " in State taxes.")
elif totalStateTax < statetaxWithheld:
    statetaxRefund = statetaxWithheld - totalStateTax
    statetaxRefund = str(statetaxRefund)
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
    fedRefund = str(fedRefund)
    print("Your refund amount is " + fedRefund)
elif fedtaxWithheld < totalFedTax:
    print("Congratulations, we're finished your Federal tax calculations.")
    fedtaxOwed = totalFedTax - fedtaxWithheld
    fedtaxOwed = str(fedtaxOwed)
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
    sstaxOwed = str(sstaxOwed)
    print("You didn't pay enough on Social Security tax this year. You'll need to pay " + sstaxOwed)
elif sstaxOwed < sstaxWithheld:
    sstaxOwed = sstaxWithheld - sstaxOwed
    sstaxOwed = str(sstaxOwed)
    print("You overpaid on your Social Security tax this year. You'll receive " + sstaxOwed + " as a refund.")
else:
    print("Error in Social Security calculations if statement pt. 2")

# Medicare tax calculations
