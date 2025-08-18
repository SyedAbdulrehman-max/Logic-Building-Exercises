# 11. Find the maximum of three numbers.
print("Enter a number to check greater!")
n  = int(input("Enter a number :"))
n2 = int(input("Enter a 2nd number: "))
n3= int(input("Enter a 2nd number: "))
if n>n2 and n>n3:
    print(f"{n} is the greater valure then the {n2} and {n3}")
elif n2>n and n2>n3:
    print(f"{n2} is the greater value then the {n} and {n3}")
else:
    print(f"{n3} is the greater value then the {n} and {n2}") 