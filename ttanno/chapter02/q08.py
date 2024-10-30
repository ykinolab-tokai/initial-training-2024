list = []
for i in range(2,101):
  result = True

  for x in range(2,i):
    if i % x == 0:
      result = False
      break
  if result:
    list.append(i)
print(list)

    