# (1) 0から99までの数をスペース区切りで並べた文字列を作成
numbers = " ".join(str(i) for i in range(100))
print(numbers)

# (2) floatの値 (1.0 / 7.0) を小数点以下9桁まで表示
value = 1.0 / 7.0
formatted_value = "{:.9f}".format(value)
print(formatted_value)
