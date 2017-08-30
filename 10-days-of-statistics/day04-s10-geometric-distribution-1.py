p_defect = 1/3
inspection_n = 5

def geometric(number_events, success_prob):
    return success_prob * (1-success_prob) ** (number_events - 1)

p = geometric(5, p_defect)
print("%.3f" % p)