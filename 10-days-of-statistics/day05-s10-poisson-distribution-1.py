from math import exp, factorial

expectation = 5/2
number_of_successes = 5

def poisson(k, l):
    return ((l ** k) * exp(-1*l)) / (factorial(k))

p = poisson(number_of_successes, expectation)
print("%.3f" % p)
