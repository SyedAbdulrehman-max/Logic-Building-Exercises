# 38. Find smallest number divisible by all numbers 1–n (LCM).
import math
def find_the_lcm(n):
    lcm = 1
    for i in range(1,1+n):
        lcm = (lcm * i) // math.gcd(lcm, i)
    return lcm

n = int(input("Enter a number: "))
print(f"smallest number divisible by 1 to {n} is {find_the_lcm(n)}")