# Write a program to find the smallest among three numbers.

# Take three integer inputs and store them in number1, number2, and number2.
# Print the smallest number between them using if...elif...else statement

number1 = int(input())
number2 = int(input())
number3 = int(input())


# check for smallest number using if...elif...else statement
if (number1 < number2 and number1 < number3):
    print(number1)

elif (number2 < number1 and number2 < number3):
    print(number2)

else:
    print(number3)
