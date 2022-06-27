a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)