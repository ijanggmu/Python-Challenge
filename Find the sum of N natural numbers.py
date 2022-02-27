# Program Description
# Write a program to find the sum of first N natural numbers.

# Get an integer input for a variable n.
# Run a loop from 1 to n.
# Inside the loop, find the sum of all numbers from 1 to n.
# Print the result.

n = int(input())

# initialize the sum variable with value 0
sum = 0

# run loop from 1 to n
for i in range(1, n+1):
    # add i to sum
    sum = sum+i

# print the value of sum
print(sum)
