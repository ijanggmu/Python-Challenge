# Replace ___ with your code

marks = int(input('Marks'))

# check if user has entered valid marks or not
# also check if the student passed or failed
if marks < 0 or marks > 100:
    print('Invalid Marks')
elif marks > 40:
    print('Pass')
else:
    print('Fail')
