# Federal imports
from fed_dicts import *
from fed_utils import *

# State imports
from state_dicts import *
from state_utils import *

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

# Declaring totalStateTax variable
totalStateTax = 0

# ALABAMA bracketed tax
# So far if statements run on Alabama Single Bracket Taxrate info from state_utils
# Need to incorporate varying filing_status complexity
if residence == "ALABAMA":
    if state_dict1sAL["min"] < income < state_dict1sAL["max"]:
        maxTax1 = sbracket1_al.taxrate * income
        totalStateTax = maxTax1
        print(totalStateTax)
    elif state_dict2sAL["min"] < income < state_dict2sAL["max"]:
        maxTax1 = sbracket1_al.taxrate * state_dict1sAL["max"]
        maxTax2 = sbracket2_al.taxrate * income
        totalStateTax = maxTax1 + maxTax2
        print(totalStateTax)
    elif state_dict3sAL["min"] < income:
        maxTax1 = sbracket1_al.taxrate * state_dict1sAL["max"]
        maxTax2 = sbracket2_al.taxrate * state_dict2sAL["max"]
        maxTax3 = sbracket3_al.taxrate * income
        totalStateTax = maxTax1 + maxTax2 + maxTax3
        print(totalStateTax)
    else:
        print("Error in state ALABAMA/SINGLE if statement")
# ALASKA no tax
elif residence == "ALASKA":
    totalStateTax = 0
    print(totalStateTax)
else:
    print("Other states follow same structure")

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

# STATE withholding vs total amount owed
if statetaxWithheld > totalStateTax:
    print("Congratulations! You'll be receiving a refund from your State taxes this year.")
    stateRefund = statetaxWithheld - totalStateTax
    stateRefund = abs(stateRefund)
    stateRefund = str(stateRefund)
    print("Your refund amount is " + stateRefund)
elif statetaxWithheld < totalStateTax:
    print("Congratulations, we're finished your State tax calculations.")
    statetaxOwed = totalStateTax - statetaxWithheld
    statetaxOwed = str(statetaxOwed)
    print("This year you owe " + statetaxOwed + " in State taxes.")
else:
    print("Error in statetaxWithheld vs totalstateTax if statements")


# Social Security tax calculations

# Declare sstaxOwed variable
sstaxOwed = 0

if income < ss_dict["max"]:
    sstaxOwed = social_security.taxrate * income
elif income > ss_dict["max"]:
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
