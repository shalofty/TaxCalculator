# Federal imports
from fed_dicts import *
from fed_utils import *

# State imports
from state_dicts import *
from state_utils import *

income = input("Please enter your annual income for the fiscal year 2022: ")
income = float(income)

residence = input("Please enter which state you will be filing your taxes through: ")
residence = residence.upper()

filing_status = input("Please enter your filing status for the fiscal year 2022: ")
filing_status = filing_status.upper()

totalFedTax = 0

# If statement comparing bracket dictionaries minimum and maximum values to user income
# totalFedTax is tax owed

# Federal Tax CalculationS
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

    elif fed_dict7s["min"] < income < fed_dict7s["max"]:
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
        print("Error in fed_single.py if statement")

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

    elif fed_dict7mfj["min"] < income < fed_dict7mfj["max"]:
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
        print("Error in fed_mfj.py if statement")

totalStateTax = 0

# Alabama bracketed tax
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
        print("Error in state_single.py, ALABAMA if statement")
# Alaska no tax
elif residence == "ALASKA":
    totalStateTax = 0
    print(totalStateTax)
else:
    print("Other states follow same structure")

totalTax = totalFedTax + totalStateTax
print(totalTax)