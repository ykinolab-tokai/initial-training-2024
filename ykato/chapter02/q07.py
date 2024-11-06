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


print("予想")
print("f(a) => [6, 7, 8]")
print("g(a) => [1, 2, 3, 1]")
#g(a)は予想通りだったが、f(a)は[1, 2, 3]となった。
#リストの上書きはできないと考えた。
#
#答え
#ポインタという関数ごとに与えられた場所があり、defをして、新たにaに代入するとポインタも新しい場所になる。そのため、元のsomefunctionで呼び出しているポインタと異なり[1, 2, 3]のままになる。
