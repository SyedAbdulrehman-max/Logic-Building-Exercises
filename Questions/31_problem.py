# 31. Calculate sum of numbers from 1 to n using a while loop.
n = int(input("Enter a number: "))
i  =1
sum = 0
while i <= n:
    sum+=i
    i += 1

print(f"sum of {n} is {sum}")