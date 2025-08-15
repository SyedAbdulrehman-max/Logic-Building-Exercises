# Count and display how many vowels (a, e, i, o, u) are in the given string.

text = input("Enter a string : ")
v = "aeiou"

count = 0
for i in text.lower():
    if i in v:
        count += 1

print(f"This number of vowles in give str are {count}")
