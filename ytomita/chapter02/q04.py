# ここにコードを書いてください
a=[4, 8, 3, 4, 1]
list =[0 if x%2==0 else 1 for x in a ]
print(list)
print("長さ",len([x for x in a if x%2!=0]))

a=[4, 8, 3, 4, 1]
list =[x for x in a if x%2==1]
print(list)