# 12. Find the minimum of three numbers.
print("Enter a number to check smallest number!")
n  = int(input("Enter a number :"))
n2 = int(input("Enter a 2nd number: "))
n3= int(input("Enter a 2nd number: "))
if n<n2 and n<n3:
    print(f"{n} is the smallest valure then the {n2} and {n3}")
elif n2<n and n2<n3:
    print(f"{n2} is the smallest value then the {n} and {n3}")
else:
    print(f"{n3} is the smallest value then the {n} and {n2}") 