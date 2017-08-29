from math import factorial

p_fail = 0.12
n_piston = 10

def binomial(x, n, p):
    if n<x:
        return 0
    else:
        return (factorial(n)/(factorial(x)*factorial(n-x))) * p**x * (1-p) ** (n-x)

p_no_more_than_2 = binomial(0, n_piston, p_fail) + binomial(1, n_piston, p_fail) + binomial(2, n_piston, p_fail)
p_2_or_more = 1 - binomial(0, n_piston, p_fail) - binomial(1, n_piston, p_fail)

print("%.3f" % p_no_more_than_2)
print("%.3f" % p_2_or_more)