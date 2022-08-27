import json

with open("state_tax_data.json") as state_tax_data:
    data = json.load(state_tax_data)

alabama = data['listStates'][0]['stateName']

state_input = input("Write Alabama")
state_input = state_input.upper()

filing_status = input("Write Single")
filing_status = filing_status.upper()

income = 327
taxRate = 0

# First iteration through json to see if stateName matches state_input from user
i = 0
for states in data['listStates'][i]['stateName']:
    if state_input == data['listStates'][i]['stateName']:
        print("1st for loop works")
        i = i
        print(data['listStates'][i]['stateName'])
        break
        # End of first iteration, loop passes test
    else:
        i += 1

# Second loop
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
# End of second iteration, loop passes test

# Beginning of third iteration
k = 0
for incomes in data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]:
    if income < data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k + 1]['income']:
        k = k
        print("3rd loop works")
        print(data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['income'])
        break
    else:
        print("3rd loop failed")
        k += 1
# End of third iteration, loop passes test

taxRate = data['listStates'][i]['filingStatus'][j]['incomeBrackets'][k]['taxRate']
print(taxRate)
