# 39. Print all prime numbers up to n.
n = int(input("get prime numbers: "))
for i in (1,n+1):
    if i%i== 0:
        print(f"The prime number form 1 to {n} are {[i]}",end=" ")