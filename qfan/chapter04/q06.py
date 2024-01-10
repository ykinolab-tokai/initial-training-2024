<<<<<<< HEAD
import math  # exp を呼び出すために math モジュールをインポート

def f(x):
    return math.exp(x)

def dfdx_approx(x):
    dh = 0.0001
    return (f(x + dh) - f(x)) / dh

x=[-3,-2,-1,0,1,2,3]
for i in range(len(x)):
    print(dfdx_approx(x[i]))

def g(x):
    return math.log(x)

def dgdx_approx(x):
    dh = 0.0001
    return (g(x + dh) - g(x)) / dh

y=[0.25,0.5,1,2,4,8]
for i in range(len(y)):
    print(dgdx_approx(y[i]))
=======
import math  # exp を呼び出すために math モジュールをインポート

def f(x):
    return math.exp(x)

def dfdx_approx(x):
    dh = 0.0001
    return (f(x + dh) - f(x)) / dh

def g(x):
    return math.log(x)

def dgdx_approx(x):
    dh = 0.0001
    return (g(x + dh) - g(x)) / dh

x=[-3,-2,-1,0,1,2,3]
for i in range(len(x)):
    print(dfdx_approx(x[i]),end=" ")
print("")
y=[0.25,0.5,1,2,4,8]
for i in range(len(y)):
    print(dgdx_approx(y[i]),end=" ")
>>>>>>> 9f5f2dffcc217eee17b62e88f153e0f1a6e5f887
