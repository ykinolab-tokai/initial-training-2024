a = " ".join(str(i) for i in range(100))
print(a)
a = 1.0/7.0
print(f"{a:.9f}")
#str(i) for i in range(100)→ジェネレーター内包表記：str(i)で整数iを文字列に変換
#join()メゾットは、リストやジェネレーター内包表記などからなる複数の要素を1つの文字列にまとめている