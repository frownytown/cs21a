# ----------------------------------------------------------------------------
#  Name:        tax
#  Purpose: To determine the amount of sales tax to be added to an item's cost
#
#  Author: Roger McClain
#  Date: 1/13/2017
#  ---------------------------------------------------------------------------
'''
Tax calculator that assumes sales tax is 8.75%

Prompt the user for the cost of their item.
Print the sales tax cost and the total cost (tax + cost)
'''
TAX_RATE = 8.75 / 100               #constant for tax rate

user_input = input('Please enter the cost of the item in $: ')
cost = float(user_input)            #convert user input to float

sales_tax = TAX_RATE * cost         #calculate sales tax cost
sales_tax = round(sales_tax, 2)     #round sales tax amount to 2 places

#converts sales tax float to string and prints
print('Sales tax amount is: $' + str(sales_tax))

total_cost = sales_tax + cost       #calculates total cost
total_cost = round(total_cost, 2)   #round total to 2 places

#converts total cost float to string and prints
print('Total cost including sales tax for this item is: $' + str(total_cost))
