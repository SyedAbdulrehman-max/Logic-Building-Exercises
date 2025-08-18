# 34. Find factorial of a number using a while loop.
n = int(input("Enter a number for factorial: "))
i = 1
total = 1

while i<=n:
    total*=i
    i+=1

print(total)
