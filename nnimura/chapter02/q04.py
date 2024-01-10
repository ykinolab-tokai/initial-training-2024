a = [4,8,3,4,1]

#(1)
squares = [x % 2 for x in a]
print(squares)

#(2)
j = 0
for i in range(len(squares)):
    if squares[i] == 1:
        j = j + 1
print(j)

#(3)
c = [x for x in a if x % 2 == 1]
print(c)
