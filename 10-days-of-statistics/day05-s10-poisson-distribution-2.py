from math import exp, factorial


def poisson(k, l):
    return ((l ** k) * exp(-1*l)) / (factorial(k))
