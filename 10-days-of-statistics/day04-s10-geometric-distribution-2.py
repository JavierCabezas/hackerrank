p_defect = 1/3
inspection_n = 5

def geometric(number_events, success_prob):
    return success_prob * (1-success_prob) ** (number_events - 1)

p = 0
for i in range(1, 6):
    p += geometric(i, p_defect)

print("%.3f" % p)
