a = input("Enter a word to check palindrom or not = ")
for x in a:
  print(x) 
for y in a[::-1]:
  print(y) 
if x == y:
  print("its a palandrom")
else:
  print("its not a palindrom")