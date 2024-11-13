a=[4, 8, 3, 4, 1]
a = [0 if i%2 == 0 else 1 for i in a]
print(a)

print(sum(a))

a=[4, 8, 3, 4, 1]
a = [i for i in a if i%2 ==1]
print(a)