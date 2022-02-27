# Write a program to check if the user likes car or bike.

# Take string as an input and assign it to the choice variable.
# Check if the user input is "Car" or "car". If yes, print "I like Car".
# Also check if the user input is "Bike" or "bike". If yes, print "I like Bike".
# If user input is anything else other than that, print nothing.
choice = input()

# check if user entered "Car" or "car"
if (choice == "Car " or choice == "car"):
    print('I like Car')

# check if user entered "Bike" or "bike"
elif(choice == "Bike" or choice == "bike"):
    print('I like Bike')
