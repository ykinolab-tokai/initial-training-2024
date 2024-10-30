"""素数を小さい順に列挙
2以上の整数 p が素数であるとは、
「どんな 2 以上 p-1 以下の整数 k に対しても p は k で割り切れない」が成り立つことを指します"""
    
for p in range(2,100):　#2以上の整数ｐ
    a=True　#素数かどうかの判別
    for k in range(2,p-1):　#2以上p-1以下の整数ｋ
        if p%k==0:　#pはkで割り切れない
            a=False　
            break
    if a:
        print(p)
