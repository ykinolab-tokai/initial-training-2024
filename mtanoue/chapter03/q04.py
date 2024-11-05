"""5×4行列をNumPy配列として作成し，以下それぞれの要素を取得するプログラムを作成してください． 
配列の要素は自由に決めてOKですが，全部0のような配列は作成したプログラムの動作を確認できないので，
場所ごとに異なる値を持つような配列とすること．

2行3列の要素（最も左上の要素は0行0列とする．以下同様）
第2列の要素すべて
奇数番目の行の要素すべて"""
import numpy as np
a = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16],[17, 18, 19, 20]])
print(a)
#2行3列の要素
print(a[2,3])

#第2列の要素すべて
print(a[:,2])

#奇数番目の行の要素すべて
print(a[:,1::2])