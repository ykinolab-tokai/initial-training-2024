a = [4, 8, 3, 4, 1]
answer = [0 if x % 2 == 0 else 1 for x in a]
print(answer)

count = sum(answer)
print(count)

answer3 = [x for x in a if x % 2 != 0]
print(answer3)