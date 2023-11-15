a = [4,8,3,4,1]
squares = [x % 2 for x in a]
print(squares)


squares = [x % 1 for x in squares]
print(squares)
res = len(squares)

b = [x for x in squares if x % 2 == 1]
print(b)

