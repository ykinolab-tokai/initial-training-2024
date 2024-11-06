#(1)
a = [4, 8, 3, 4, 1]
a = [0 if x % 2 == 0 else 1 for x in a]
print(a)
#(2)
a = [4, 8, 3, 4, 1]
a = [0 if x % 2 == 0 else 1 for x in a]
print(f'リストaに含まれる奇数の個数は{sum(a)}個です。')
#(3)
a = [4, 8, 3, 4, 1]
a = [x for x in a if x % 2 != 0]
print(a)