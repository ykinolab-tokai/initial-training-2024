a=list(range(2,101))
b=[]
for x in a:
  for i in range(1,x+1):
    if i==x:
      b.append(x)
    elif i==1:
      continue
    elif x%i==0:
      break
print(b)