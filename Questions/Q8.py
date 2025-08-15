# Check if a given word is a palindrome (reads the same forwards and backwards).

word = input("Enter the word: ")
word = word.lower()
reverse = word[::-1]

if word == reverse:
    print("The give word is palindrome:")
else:
    print("The given word is not palindrome")