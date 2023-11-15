a=[4,8,3,4,1]
#1
b=[x%2 for x in a]
print(b)
#2
d=[1 for x in a if x%2==1]
print(len(d))
#3
e=[1 for x in a if x%2==1]
print(e)
