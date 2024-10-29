#f(a)がsomefunctionにおいて上書きされているので出力はa0のリストが出力される。
#gも同様で上書きされてa1.append(1)になるのでa1リストの最後に1が追加されて出力される

def f(a):
    a = [6,7,8]
    
def g(a):
    a.append(1)
    
def somefunction():
    a0 = [1,2,3]
    f(a0)
    print(a0)
    
    a1 = [1,2,3]
    g(a1)
    print(a1)
    
somefunction()
