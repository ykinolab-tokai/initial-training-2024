#(1)
print("(1)")
a = [4, 8, 3, 4, 1]

a1 = [0 if a[i] % 2 == 0 else 1 for i in range(len(a))]
print(a1)

#(2)
print("(2)")
a2 = ([0 if a[i] % 2 == 0 else 1 for i in range(len(a))])
a2 = a2.count(a2)
print(f'奇数の数：{a2}')

#(3)
print("(3)")
a3 = [a[i] for i in range(len(a)) if a[i] % 2 == 1]
print(f'奇数だけ抜き出す：{a3}')
