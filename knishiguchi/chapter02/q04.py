# (1)
a = [4, 8, 3, 4, 1]
ans = [x % 2 for x in a]
print(ans)

# (2)
a = [4, 8, 3, 4, 1]
ans = [x % 2 for x in a]
print(sum(ans))

# (3)
a = [4, 8, 3, 4, 1]
ans = [x for x in a if x % 2 != 0]
print(ans)