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

#予想：a0→[1,2,3]、a1→[1,2,3,1]
#f(a0)ではリストの中身が[6,7,8]から[1,2,3]へ上書きされたことによって[1,2,3]となる。
#g(a1)では渡されたa1のリストに1を追加する処理が行われているため、[1,2,3,1]となる。