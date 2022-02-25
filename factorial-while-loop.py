# replace ___ with your code below

# Take integer input
n = int(input('factorial'))

# The initial value of total is 1
total = 1

i = 1
while i<=n:
    # multiply total and i in each iteration
    total = total * i   
    i=i+1

print(total)