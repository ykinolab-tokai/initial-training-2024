a = [4, 8, 3, 4, 1]

a1 = [x % 2 for x in a]
print(a1) 
print()

a2 = sum(a1)
print(a2)
print()

a3 = [x for x in a if x % 2 == 1]
print(a3)
print()