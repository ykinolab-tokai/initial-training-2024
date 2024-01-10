import math

def f(x):
    return math.exp(x)

def dfdx_approx(x):
    dh = 0.0001
    return (f(x + dh) - f(x)) / dh

dfdx_approx(-3)

dfdx_approx(-2)

dfdx_approx(-1)

dfdx_approx(0)

dfdx_approx(1)

dfdx_approx(2)

dfdx_approx(3)

dfdx_approx(0.25)

dfdx_approx(0.5)

dfdx_approx(1)

dfdx_approx(2)

dfdx_approx(4)

dfdx_approx(8)
