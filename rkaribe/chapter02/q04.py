#リスト内包表記は一般に [(式) for (変数) in (iterableオブジェクト)]
#(1) a=[4, 8, 3, 4, 1] というリストに対し、要素が偶数なら 0, 奇数なら 1 に変換するコードをリスト内包表記を用いて書いて下さい。この結果、このリストは [0, 0, 1, 0, 1] に変換されるべきです。

#(2) (1) で書いたコードと組み込み関数を組み合わせて、リスト a に含まれる奇数の個数を数えるコードを書いて下さい。

#(3) リスト内包表記では、if 文を用いることで条件を満たす要素だけをリストに残すことができます。

1 
a = [4, 8, 3, 4, 1]
squares = [0 if x % 2 == 0 else 1 for x in a]
print(squares)  

2
a = [4, 8, 3, 4, 1]
squares_count = sum([ 1 for x in a if x % 2 != 0])
print(squares_count)

3
a = [4, 8, 3, 4, 1]
squares_kisuu = [ x for x in a if x % 2 != 0]
print(squares_kisuu)
