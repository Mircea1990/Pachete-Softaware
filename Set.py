thisset = {"apple", "banana", "cherry"}
print(thisset)
for x in thisset:
  print(x)

thisset.add("orange")
print(thisset)
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)
print(z)