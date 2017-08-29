from math import factorial

p_girl = 1/(1.09+1)
p_boy = 1-p_girl
n_children = 6

def binomial(x, n, p):
    '''
    This function calculates a binomial, that being, with events a and b p(a) + p(b) = 1
    Ex: Having exactly 2 4's with 3 4 sided dices.
    :param x: Number of successful events ( 2 )
    :param n: Number of tries (3)
    :param p: 1/4
    :return: The probability as a float
    '''
    if n<x:
        return 0
    else:
        return (factorial(n)/(factorial(x)*factorial(n-x))) * p**x * (1-p) ** (n-x)

#Probability of at least 3 boys in 6 children: P(3 boys) + P(4 boys) + P(5 boys) + P(6 boys)
p_at_least_3_boys = binomial(3, n_children, p_boy) + binomial(4, n_children, p_boy) + binomial(5, n_children, p_boy) + binomial(6, n_children, p_boy)
print("%.3f" % p_at_least_3_boys)