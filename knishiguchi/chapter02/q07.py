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

# 予想:a0→[1,2,3],a1→[1,2,3,1]
# a0の理由:f(a0)では、aというリストを新しく作成しているだけなのでa0のリストには反映されないため。
# a1の理由:g(a1)では、末尾に1を追加するコードが書かれているのでa1=[1,2,3]の末尾に1を追加するため。