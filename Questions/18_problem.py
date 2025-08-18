# 18. Count consonants in a word.
user = input("Enter a word: ")
word = "aeiouAEIOU"
total = 0
count = 0
for i in user:
    if i.isalpha() and i not in word:
        total+=1
    count+=1

print(f"The total  are {total} in {user}")