a = [4, 8, 3, 4, 1]
result = [0 if x % 2 == 0 else 1 for x in a]
print(result)  

odd_count = sum(1 for x in a if x % 2 != 0)
print(odd_count) 


filtered_odd = [x for x in a if x % 2 != 0]
print(filtered_odd)  # => [3, 1]


