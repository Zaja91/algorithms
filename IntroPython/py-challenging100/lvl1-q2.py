# Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

import math

def factorial(n):
    # take a n and brake it down in range(begin=1, end=n+1)
    fact = 1 #always start at 1
    for i in range(1, n+1): #include the last number in range
        fact *= i
    return fact

print(factorial(10))

print(math.factorial(10)) # using math module
