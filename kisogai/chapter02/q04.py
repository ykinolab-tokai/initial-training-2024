a = [4, 8, 3, 4, 1]
squares = [0 if x%2==0 else 1 for x in a] 
print(squares)  
#0 if x%2==0→もしxが偶数なら、リストに0を追加する
#else 1 →もしxが奇数なら、リストには１を追加する。
#for x in a→リストの各要素をxを順番に取り出す。

a = [4, 8, 3, 4, 1]
squares = [0 if x%2==0 else 1 for x in a]
count=sum(squares)
print(count)  

a = [4, 8, 3, 4, 1]
squares = [x for x in a if x%2!=0]
print(squares)
#最初のxは新しいリストに入れる要素を指定する。
#リストaの各要素がxに対応する。
#if文で条件を指定して、Trueだった場合は新しいリストにその要素を追加する。
#xを2で割った余りが0出ない場合、xは奇数になる。
