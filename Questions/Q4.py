#Ask the user to enter three numbers and print the largest one.

n1 = int(input("Enter the number: "))
n2 = int(input("Enter the number: "))
n3 = int(input("Enter the number: "))

if n1>n2 and n1>n3:
    print(f"The greater number is  {n1}")
elif n2>n1 and n2>n3:
    print(f"The greater number is  {n2}")
elif n3>n2 and n3>n1:
    print(f"The greater number is  {n3}")