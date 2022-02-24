# Replace ___ with your code

# take two integer inputs for chocolates and children
choc = int(input('chocolates'))
child = int(input('no. of childrens'))

# find chocolates each children will get and and print it
g_choci = choc/child
g_choc = int(g_choci)
print(g_choc)

# find remaining chocolates and print it
r_choc = choc % child
print(r_choc)
