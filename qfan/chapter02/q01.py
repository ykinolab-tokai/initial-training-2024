a=[4,8,3,4,1]
print(len(a))
print(max(a))
print(min(a))
print(sum(a))
pre=0
def FUNC(x):
    for i in range(5):
        for j in range(5):
            if x[i]<x[j]:
                pre=x[i]
                x[i]=x[j]
                x[j]=pre
    return(x)
res = FUNC(a)
print(res)
