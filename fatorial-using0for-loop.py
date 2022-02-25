# replace ___ with your code below

# Take integer input
n = int(input('Factorial using for loop'))

# The initial value of total is 1
total = 1

for i in range(1, n+1):
    # multiply total and i in each iteration
    total = total*i

print(total)
