以下の演算や関数をそれぞれ評価したとき、結果の値と型が何になるか予想してください。

1.2 + 3.8 　予想：5.0 float　結果：5.0 float
10 // 100　予想：0 int 結果：0 int
1 >= 0　予想：True bool 結果：True bool
'Hello World' == 'Hello World'　予想：True bool 結果：True bool
not 'Chainer' != 'Tutorial'　予想：False bool 結果：False bool
all([True, True, False]) (all の定義は公式ドキュメントを参照)　予想：False bool　結果：False bool
any([True, True, False]) (any の定義は公式ドキュメントを参照)　予想：True bool 結果：True bool
abs(-3) (abs の定義は公式ドキュメントを参照)　予想：3 int 結果：3 int
2 // 0　予想：0,int 結果：error 