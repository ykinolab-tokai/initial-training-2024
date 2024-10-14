#5.0  float
1.2+3.8
type(1.2+3.8)

#0  int
10//100
type(10//100)

#True  bool
1>=0
type(1 >= 0)

#True  bool
'Hello World' == 'Hello World'
type('Hello World' == 'Hello World')

#False  bool
not 'Chainer' != 'Tutorial'
type(not 'Chainer' != 'Tutorial')

#False  bool
all([True, True, False])
type(all([True, True, False]))

#True  bool
any([True, True, False])
type(any([True, True, False]))

#3  int
abs(-3)
type(abs(-3))

#エラー
2 // 0
type(2 // 0)