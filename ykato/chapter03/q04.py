import numpy as np

a = np.array(
    [[900, 901, 902, 903],
     [910, 911, 912, 913],
     [920, 921, 922, 923],
     [930, 931, 932, 933],
     [940, 941, 942, 943]])

print("2行3列の要素（最も左上の要素は0行0列とする．以下同様）")
print(a[2, 3])

print("第2列の要素すべて")
print(a[:, 2])

print("奇数番目の行の要素すべて")
print((a[::2]))
