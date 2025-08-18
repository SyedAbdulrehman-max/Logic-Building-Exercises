# 15. Count down from a number to 1.
n = int(input("Enter a number:"))

count = 0
for i in range(n,-1,-1):
    print(i)
    count+=1

