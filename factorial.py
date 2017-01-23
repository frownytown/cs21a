user_input = input('Please enter a positive interger: ')
number = int(user_input)
result = 1                              # initialize the factorial result to 1
for i in range(1, number + 1):          # omit 0 but include number
    result *= i
print(result)
