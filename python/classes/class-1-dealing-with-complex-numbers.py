import math

class Complex(object):
    def __init__(self, r, i):
        self.r = r
        self.i = i
    def __add__(self, no):
        return Complex(self.r + no.r, self.i + no.i)
    def __sub__(self, no):
        return Complex(self.r - no.r, self.i - no.i)
    def __mul__(self, no):
        return Complex(self.r * no.r - no.i * self.i, self.r * no.i + self.i * no.r)
    def __truediv__(self, no):
        try:
            cplex = self * no.conjugate()
            factor = pow(no.r, 2) + pow(no.i, 2)
            return Complex(cplex.r/factor, cplex.i/factor)
        except ZeroDivisionError as e:
            return None
    def conjugate(self):
        return Complex(self.r, (-1)*self.i)
    def mod(self):
        return Complex(math.sqrt(self.r ** 2 + self.i ** 2), 0)
    def mod_real(self):
        return self.mod().r
    def __str__(self):
        if self.i == 0:
            result = "%.2f+0.00i" % (self.r)
        elif self.r == 0:
            if self.i >= 0:
                result = "0.00+%.2fi" % (self.i)
            else:
                result = "0.00-%.2fi" % (abs(self.i))
        elif self.i > 0:
            result = "%.2f+%.2fi" % (self.r, self.i)
        else:
            result = "%.2f-%.2fi" % (self.r, abs(self.i))
        return result