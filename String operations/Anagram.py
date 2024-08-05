word1 = input("Enter the word1 = ")
word2 = input("Enter the word2 = ")
count = 0
if (len(word1) == len(word2)):
    for x in word2:
        if word1.count(x)>0 :
            count += 1
if count == len(word1):
    print("Its an Anagram words")
else:
    print("Its not an Anagram words")