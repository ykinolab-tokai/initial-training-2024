def f(a):
    a = [6, 7, 8]

def g(a):
    a.append(1)

def somefunction():
    a0 = [1, 2, 3]
    f(a0)
    print(a0)

    a1 = [1, 2, 3]
    g(a1)
    print(a1)

somefunction()
#予想:f(a) =[1,2,3],g(a1)=[1,2,3,1]
#理由：fは上書き、gはappendで追加をする関数のため