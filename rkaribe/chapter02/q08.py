#2以上の整数 p が素数であるとは、「どんな 2 以上 p-1 以下の整数 k に対しても p は k で割り切れない」が成り立つことを指します。素数を小さい順から列挙すると、2, 3, 5, 7, 11, 13, 17, ... となります。 チュートリアルで学んだ制御構文である if や for を用いて、2 から 100 からまでに含まれる素数を列挙するプログラムを，q08.pyに記述して下さい。

for p in range(2,101):
  for k in range(2,p):
    if p%k==0:
      break
  else:
    print(p)
