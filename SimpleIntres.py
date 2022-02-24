# Replace ___ with your code

# take float input for principal, rate, and time
p=float(input('Principal'))
r=float(input('Rate'))
t=float(input('Time'))
# calculate the simple interest
simple_intrest=p*t*r*0.01

# calculate the final amount
f_amt=p+simple_intrest

# print interest and total_sum in separate lines
print(simple_intrest)
print(f_amt)