#5×4行列をNumPy配列として作成し，以下それぞれの要素を取得するプログラムを作成してください． 配列の要素は自由に決めてOKですが，全部0のような配列は作成したプログラムの動作を確認できないので，場所ごとに異なる値を持つような配列とすること．
#1 2行3列の要素（最も左上の要素は0行0列とする．以下同様）
#2 第2列の要素すべて
#3 奇数番目の行の要素すべて

import numpy as np
#5×4のnumpy配列
array_random =np.random.uniform(0,10,(5,4)).astype(int)
print("5×4の配列を作成\n",array_random)

#1
array_2_3= array_random[2,3]
print("2行3列の要素",array_2_3)

#2
array_2_all= array_random[:,2]
print("2列すべての要素",array_2_all)

#3
array_kisuu= array_random[1::2,:]
print("奇数番目の行すべての要素",array_kisuu)

