for nums in range(2,101):
    i = True
    for x in range(2,nums):
        if (nums%x)== 0:
            i = False
            break
    if i:
        print(nums,end = " ")

# 解説
#for文を二重に利用することで
#　i = Trueにて素数のみを表示するときに利用する
# どんな2以上p-1以下の整数kに対してもpはkで割り切れない→2以上の素数の条件
