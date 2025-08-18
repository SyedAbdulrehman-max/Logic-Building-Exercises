# 13. Print multiplication table for a number (1–10).

n = int(input("Enter a number: "))
count = 1
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")
    count+=1