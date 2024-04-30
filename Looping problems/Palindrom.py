a = input("Enter a word to check palindrom or not = ")
for x in a:
  print(x," ",end="")
for y in a[::-1]:
  print(y," ",end="")
print("\n")
if x == y:
  print("its a palandrom")
else:
  print("its not a palindrom")