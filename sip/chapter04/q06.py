import math

def f(x):
    return math.exp(x)

def g(x):
    return math.log(x)

def dfdx_approx(x):
    dh = 0.0001
    return (f(x + dh) - f(x)) / dh

def dfdx_approx2(x):
    dh = 0.0001
    return (g(x + dh) - g(x)) / dh

X =[-3,-2,-1,0,1,2,3]
for i in X:
    print(math.exp(i))
    print(dfdx_approx(i))

print("-----")

X_log=[0.25,0.5,1,2,4,8]
for i in X_log:
    print(1/i)
    print(dfdx_approx2(i))
    