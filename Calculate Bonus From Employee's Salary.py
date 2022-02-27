# Write a program to calculate bonus from employee's salary.

# Susan decides to give a bonus of 5% to employees if their year of service is more than 5 years.
# Take salary and year of service as input and print the bonus amount.
# Take float input from the user and assign it to the salary variable.
# Take int input from the user and assign it to the years variable.
# Calculate 5% bonus if the years > 5.
# Print bonus.

# take float input for salary
salary = float(input())

# take integer input for years
years = int(input())

# check if years worked is greater than 5 or not
if(years > 5):
    # calculate bonus using 5 * salary / 100
    bonus = salary*0.05
    # print bonus
    print(bonus)
