a = [4, 8, 3, 4, 1]
data = [x % 2 for x in a]
print(data)

count = sum(data)
print(count)

data = [x for x in a if x % 2 != 0]
print(data)
