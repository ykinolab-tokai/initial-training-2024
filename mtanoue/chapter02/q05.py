#str.join() を使って、0 から 99 までの数をスペース区切りで並べた文字列 "0 1 2 3 4 ... 99" を構成して下さい。
a = [str(x) for x in range(100)]
print(' '.join(a))
#str.format() を使って float の値 (1.0 / 7.0) の小数点以下9桁までを表示して下さい。
a="{:.9f}".format(1.0/7.0)
print(a)
