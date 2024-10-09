# 1. 1.2 + 3.8
result_1 = 1.2 + 3.8
type_1 = type(result_1)

# 2. 10 // 100
result_2 = 10 // 100
type_2 = type(result_2)

# 3. 1 >= 0
result_3 = 1 >= 0
type_3 = type(result_3)

# 4. 'Hello World' == 'Hello World'
result_4 = 'Hello World' == 'Hello World'
type_4 = type(result_4)

# 5. not 'Chainer' != 'Tutorial'
result_5 = not 'Chainer' != 'Tutorial'
type_5 = type(result_5)

# 6. all([True, True, False])
result_6 = all([True, True, False])
type_6 = type(result_6)

# 7. any([True, True, False])
result_7 = any([True, True, False])
type_7 = type(result_7)

# 8. abs(-3)
result_8 = abs(-3)
type_8 = type(result_8)

# 9. 2 // 0 (This will cause a ZeroDivisionError)
try:
    result_9 = 2 // 0
except ZeroDivisionError:
    result_9 = "ZeroDivisionError"
type_9 = "Error" if result_9 == "ZeroDivisionError" else type(result_9)

# Print all results
print(f"1.2 + 3.8 → {result_1}, type: {type_1}")
print(f"10 // 100 → {result_2}, type: {type_2}")
print(f"1 >= 0 → {result_3}, type: {type_3}")
print(f"'Hello World' == 'Hello World' → {result_4}, type: {type_4}")
print(f"not 'Chainer' != 'Tutorial' → {result_5}, type: {type_5}")
print(f"all([True, True, False]) → {result_6}, type: {type_6}")
print(f"any([True, True, False]) → {result_7}, type: {type_7}")
print(f"abs(-3) → {result_8}, type: {type_8}")
print(f"2 // 0 → {result_9}, type: {type_9}")