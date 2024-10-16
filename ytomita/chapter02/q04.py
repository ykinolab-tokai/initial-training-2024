a=[4, 8, 3, 4, 1]
result = [0 if x%2==0 else 1 for x in a]
print(result)

print("1の個数",len([x for x in a if x%2!=0]))

a=[4, 8, 3, 4, 1]
list = [x for x in a if x%2!=0]
print(list)