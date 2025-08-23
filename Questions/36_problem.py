# 36. Print numbers 1–100 divisible by 3 and 5.

for i in range(1,100):
    if i%3 == 0 and i%5 == 0:
        print(i)