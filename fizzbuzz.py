# Program Description
# Write a program to print FizzBuzz based on user input.

# Get an integer input from the user.
# If the number is multiple of 3, print "Fizz".
# If the number is multiple of 5, print "Buzz".
# If the number is multiple of both 3 and 5, print "FizzBuzz".
# Else print the original number.

number = int(input())

# get input value of number

# check if number is multiple of 3 or 5 or both
if(number % 3 == 0 and number % 5 == 0):
    print("FizzBuzz")

elif (number % 3 == 0):
    print("Fizz")

elif(number % 5 == 0):
    print('Buzz')

else:
    print(number)
