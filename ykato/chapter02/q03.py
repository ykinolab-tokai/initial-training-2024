a = [4, 8, 3, 4, 1]

print("リストaの先頭の要素を取り除く")
del a[0]
print(a)


a.insert(0, 4)
print("リストaの末尾の要素を取り除く")
del a[-1]
print(a)


a = a + [1]
print("末尾に100を追加する")
a.append(100)
print(a)
