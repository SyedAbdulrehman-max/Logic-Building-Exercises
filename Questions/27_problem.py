# 27. Check if a word exists in a sentence.
word = input("Enter a word to check: ")

with open("27_problem.txt", "r") as f:
    s= f.read()

if word in s:
    print(f"The word '{word}' is found!")
else:
    print(f"The word '{word}' is not found!")