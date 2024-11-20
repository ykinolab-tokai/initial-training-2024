import math

def f(x):
    return math.exp(x)

def dfdx_approx(x):
    dh = 0.0001
    return (f(x + dh) - f(x)) / dh

X =[-3,-2,-1,0,1,2,3]
for i in X:
    print(dfdx_approx(i))

print("-----")

X_log=[0.25,0.5,1,2,4,8]
for i in X_log:
    print(dfdx_approx(math.log(i)))
    