for p in range(2, 101):
#pを2から100までの数に設定
    a = True #Trueは素数の可能性がある
    for k in range(2,int(p ** 0.5)+1):
# k を2から sqrt(p)（小数点以下切り捨て）までの範囲で繰り返す
        if p % k == 0:
# p が k で割り切れるときは、p は素数ではない。a = False として素数でないことを示し、break で内側のループを終了する
            a = False
            break
    if a:
        print(p)
