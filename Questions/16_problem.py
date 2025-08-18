# 16. Check word length: print "Short" (<5) or "Long".
n = input("Enter a word to check its length: ")
count=0
if len(n) > 5:
    print(f" the len of {n} is {len(n)} is Long")
else:
    print(f" the len of {n} is {len(n)} is Short")