a=1.2+3.8
print(a)
print(type(a))

a=10//100 #整数部分のみを返すため、0.1の小数点以下が切り捨てられ0になる
print(a)
print(type(a))

a=(1>=0) #真理値を示す型
print(a)
print(type(a))

a='Hello World'=='Hello World'
print(a)
print(type(a))

a=not 'Chainer' != 'Tutorial' #'Chainer' != 'Tutorial'はTrueになるが、not Trueがあるため最終的な結果はFalseになる
print(a)
print(type(a))

a=all([True,True,False]) #all()関数は、与えられたリストやタプルにあるすべての要素がTrueである場合にTrueを返す
print(a)
print(type(a))

a=any([True,True,False]) #リストの中に一つでもTrueがあればTrueを返し、すべての要素がFalseであればFalseを返す
print(a)
print(type(a))

a=abs(-3) #絶対値を返す
print(a)
print(type(a))

#a=2//0 #0で割ることができないため、エラーが発生する
#print(a)
#print(type(a))
