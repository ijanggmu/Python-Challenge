# store the returned value in the total variablest
def compute_factorial(number):
    factorial = 1
    for i in range(1, number+1):
        factorial = factorial*i
    return factorial


number = int(input('numbers'))
total = compute_factorial(number)
print(total)
