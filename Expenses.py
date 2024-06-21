import numpy as np
with open('Expenses.txt', 'r') as f:
    expenses = f.read().splitlines()
    expenses = [int(i) for i in expenses]
expenses_dif1 = [(2020 - i) for i in expenses]
sum2 = []
for i in expenses_dif1:
    if i in expenses:
        sum2.append(i)
print("The two expenses that sum to 2020 are: " + str(sum2))
print("They multiply together to give: " + str(np.prod(sum2)))
sum3 = []
for i in range(0, len(expenses)):
    for j in range(0, len(expenses)):
        if expenses_dif1[i] - expenses[j] in expenses:
            if expenses[i] not in sum3:
                sum3.append(expenses[i])
print("The three expenses that sum to 2020 are: " + str(sum3))
print("They multiply together to give: " + str(np.prod(sum3)))