# -----------------------------------------------------------------------------
# Name:                 tip
# Purpose:              calculate the tip amount
# Author:               Roger McClain
# -----------------------------------------------------------------------------
"""
Tip calculator that assumes a 20% tip

Prompt the user for the cost of their meal
Print the tip amount and the total cost (tip + meal)
"""

TIP_RATE = 20 / 100                     #constant for tip rate

user_input = input('Please enter the cost of your meal in $: ')
cost = float(user_input)                #convert input into a float

tip = TIP_RATE * cost                   #tip rate calculation
tip = round(tip, 2)                     #round tip amount to 2 places

print('Tip amount: $', tip, sep='')     #supress space separator

total = cost + tip                      #total cost of meal
total = round(total, 2)                 #round total cost to 2 places

print('Total cost: $', total, sep='')     #supress space separator
