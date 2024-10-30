2以上の整数 p が素数であるとは、
「どんな 2 以上 p-1 以下の整数 k に対しても p は k で割り切れない」が成り立つことを指します
for p in range(2,100):
    a=True
    for k in range(2,p-1):
        if p%k==0:
            a=False
            break
    if a:
        print(p)
