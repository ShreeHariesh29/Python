given_word = input("Enter a word to check palindrom or not = ")
reversed_word = given_word[::-1]
print("reversed word is ",reversed_word)
if(given_word == reversed_word):
  print("Its a palindrom")
else:
  print("its not a palindrom")