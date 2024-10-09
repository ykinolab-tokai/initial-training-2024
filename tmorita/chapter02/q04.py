#(1)
a = [4, 8, 3, 4, 1]
converted = [0 if x % 2 == 0 else 1 for x in a]
print(f"(1) 偶数なら0, 奇数なら1に変換: {converted}")

#(2)
odd_count = sum([1 for x in a if x % 2 != 0])
print(f"(2) 奇数の個数: {odd_count}")

#(3)
odd_numbers = [x for x in a if x % 2 != 0]
print(f"(3) 奇数の要素だけを残す: {odd_numbers}")