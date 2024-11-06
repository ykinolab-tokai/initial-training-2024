#先頭を削除
a=[4,8,3,4,1]
a.pop(0)
print(a)

a=[4,8,3,4,1]
del a[0]
print(a)

#末尾を削除
a=[4, 8, 3, 4, 1]
a.pop()
print(a)

a=[4, 8, 3, 4, 1]
del a[-1]
print(a)

#末尾に100を追加
a=[4, 8, 3, 4, 1]
a.append(100)
print(a)