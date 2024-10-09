a=[4, 8, 3, 4, 1]
a = [0 if i%2 == 0 else 1 for i in a]
print(a)

count=0
for i in a:
    if i == 1:
        count+=1
print(count)

a=[4, 8, 3, 4, 1]
a = [i for i in a if i%2 ==1]
print(a)